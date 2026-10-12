#!/usr/bin/env python3
"""Comprueba preservación y ZIP comunitarios; no sustituye pruebas de plataforma."""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import zipfile
from urllib.parse import unquote

SLUG = "aula-comunidad-educativa-aumentada"

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def materiales(root):
    return {p.relative_to(root).as_posix(): sha(p) for p in root.rglob("*")
            if p.is_file() and not any(x.startswith("._") or x in
              (".DS_Store", ".git", "__pycache__", "outputs", "build", "paquetes")
              for x in p.relative_to(root).parts)}

def main():
    ap = argparse.ArgumentParser()
    for nombre in ("original", "repositorio", "paquetes", "evidencia"):
        ap.add_argument("--" + nombre, type=pathlib.Path, required=True)
    a = ap.parse_args()
    version = (a.repositorio / "VERSION").read_text().strip()
    fallos, pruebas = [], []
    def comprobar(condicion, detalle):
        (pruebas if condicion else fallos).append(detalle)
    anterior, actual = materiales(a.original), materiales(a.repositorio)
    ausentes = sorted(set(anterior) - set(actual))
    modificados = sorted(p for p in anterior if p in actual and anterior[p] != actual[p])
    comprobar(not ausentes, "Todos los archivos materiales originales se conservan")
    catalogo = {}
    for carpeta, patron, esperado in (("agentes", "A*.md", 22), ("workflows", "W*.md", 32),
                                     ("skills", "*/SKILL.md", 31), ("plantillas", "[0-9]*", 59)):
        archivos = sorted((a.original / carpeta).glob(patron))
        archivos = [p for p in archivos if p.is_file()]
        catalogo[carpeta] = len(archivos)
        comprobar(len(archivos) == esperado, f"Inventario original {carpeta}: {len(archivos)}")
        comprobar(all(sha(p) == sha(a.repositorio / p.relative_to(a.original)) for p in archivos),
                   f"Hashes íntegros de {carpeta} en la fuente comunitaria")
    comprobar(all(p.read_bytes()[:4] == bytes.fromhex("00051607")
                   for p in a.original.rglob("._*") if p.is_file()),
               "Los auxiliares omitidos del origen son AppleDouble")
    comprobar("1.3.2-comunitaria.3" == version, "Versión comunitaria identificada")
    paquetes = sorted(p for p in a.paquetes.glob(f"{SLUG}-*-{version}.zip") if not p.name.startswith("._"))
    comprobar(len(paquetes) == 5, "Se incluyen cuatro adaptadores y mantenimiento")
    resultados = []
    for z in paquetes:
        with tempfile.TemporaryDirectory(prefix="aula-comunitaria-qa-") as temporal:
            destino = pathlib.Path(temporal)
            with zipfile.ZipFile(z) as archivo:
                nombres = archivo.namelist()
                comprobar(archivo.testzip() is None, f"CRC íntegro: {z.name}")
                seguros = all(not pathlib.PurePosixPath(n).is_absolute() and ".." not in pathlib.PurePosixPath(n).parts
                              and "\\" not in n for n in nombres)
                comprobar(seguros, f"Rutas de archivo seguras: {z.name}")
                comprobar(not any(any(x.startswith("._") or x in (".DS_Store", ".git", "__pycache__")
                                      for x in pathlib.PurePosixPath(n).parts) for n in nombres),
                           f"Sin auxiliares de macOS, Git ni cachés: {z.name}")
                if not seguros:
                    continue
                archivo.extractall(destino)
            raiz = next(destino.iterdir())
            prueba = subprocess.run([sys.executable, str(a.repositorio / "tests/validador_estructura.py"), str(raiz)],
                                    capture_output=True, text=True)
            salida = prueba.stdout.replace(str(raiz), "<extraccion-limpia>") + prueba.stderr
            comprobar(prueba.returncode == 0, f"Validador de extracción limpia: {z.name}")
            if "chatgpt-work" in z.name:
                base = raiz / SLUG / "references"
                skills = base / "skills"
                comprobar(materiales(a.original / "plantillas") == materiales(raiz / SLUG / "assets/plantillas"),
                           "ChatGPT Work conserva las plantillas de assets por hash")
            elif "desarrollo-mantenimiento" in z.name:
                base = raiz / "src" / SLUG
                skills = base / "skills"
                for linea in (raiz / "SHA256SUMS_INTERNO.txt").read_text().splitlines():
                    digest, nombre = linea.split("  ", 1)
                    comprobar(sha(raiz / nombre) == digest, f"Hash interno: {nombre}")
            else:
                base = raiz
                skills = raiz / ".agents/skills" if "antigravity" in z.name else raiz / "skills"
            for carpeta in ("agentes", "workflows", "plantillas"):
                comprobar(materiales(a.original / carpeta) == materiales(base / carpeta),
                           f"Catálogo íntegro de {carpeta}: {z.name}")
            originales_skills = list((a.original / "skills").glob("*/SKILL.md"))
            comprobar(len(list(skills.glob("*/SKILL.md"))) == 31, f"31 skills: {z.name}")
            for p in originales_skills:
                original = p.read_text()
                copia = (skills / p.relative_to(a.original / "skills")).read_text()
                comprobar(copia.startswith(original) if "claude-cowork" in z.name else copia == original,
                           f"Skill preservada {p.parent.name}: {z.name}")
            comprobar("Licencia Comunitaria" in (base / "documentacion/CONDICIONES_DE_USO.md").read_text(),
                       f"Condiciones comunitarias: {z.name}")
            if "claude-cowork" in z.name:
                plugin = json.loads((raiz / ".claude-plugin/plugin.json").read_text())
                comprobar(plugin["version"] == version and "Comunitaria" in plugin["license"],
                           "Manifiesto Cowork coherente con edición y licencia")
                comprobar(len(list((raiz / "agents").glob("*.md"))) == 22, "22 subagentes Cowork")
            resultados.append({"zip": z.name, "sha256": sha(z), "codigo_validador": prueba.returncode,
                               "salida_validador": salida})
    readme = (a.repositorio / "README.md").read_text()
    for enlace in re.findall(r"\[[^\]]+\]\(([^)]+)\)", readme):
        if not enlace.startswith(("http:", "https:", "#")):
            comprobar((a.repositorio / unquote(enlace.split("#")[0])).exists(), f"Enlace README: {enlace}")
    informe = {"version": version, "catalogo": catalogo, "archivos_originales": len(anterior),
               "archivos_actuales": len(actual), "ausentes": ausentes, "modificados": modificados,
               "anadidos": sorted(set(actual) - set(anterior)), "pruebas_superadas": len(pruebas),
               "fallos": fallos, "paquetes": resultados,
               "limites": "Verificación estática y de integridad; sin ejecución conversacional ni validación independiente."}
    a.evidencia.parent.mkdir(parents=True, exist_ok=True)
    a.evidencia.write_text(json.dumps(informe, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: informe[k] for k in ("version", "catalogo", "archivos_originales", "archivos_actuales",
                     "ausentes", "modificados", "pruebas_superadas", "fallos")}, ensure_ascii=False, indent=2))
    return 1 if fallos else 0

if __name__ == "__main__":
    sys.exit(main())
