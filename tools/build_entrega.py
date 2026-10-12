#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construye el paquete de desarrollo y mantenimiento y prepara la carpeta de entrega.
Debe ejecutarse DESPUÉS de tools/build_adapters.py.

Uso:  python3 tools/build_entrega.py [--src <fuente>] [--build <dir build>] [--entrega <dir>]
"""
import argparse, pathlib, shutil, subprocess, sys, hashlib, zipfile, datetime, os

SLUG = "aula-comunidad-educativa-aumentada"
IGNORAR = shutil.ignore_patterns("._*", ".DS_Store", "__pycache__", "*.pyc", ".git",
                                "outputs", "build", "paquetes")

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def zipdir(carpeta, destino_zip):
    destino_zip.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destino_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(carpeta.rglob("*")):
            if p.is_file() and not any(part.startswith("._") or part in (".DS_Store", "__pycache__", ".git") for part in p.relative_to(carpeta).parts):
                info = zipfile.ZipInfo(p.relative_to(carpeta.parent).as_posix(), (1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                z.writestr(info, p.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
    return destino_zip

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=None)
    ap.add_argument("--build", default=None)
    ap.add_argument("--entrega", default=None)
    ap.add_argument("--fecha", default=None, help="Fecha ISO para reproducir los informes de una entrega")
    a = ap.parse_args()

    src = pathlib.Path(a.src).resolve() if a.src else pathlib.Path(__file__).resolve().parents[1]
    version = (src/"VERSION").read_text(encoding="utf-8").strip()
    build = pathlib.Path(a.build).resolve() if a.build else src/"outputs"/f"build-{version}"
    hoy = datetime.date.fromisoformat(a.fecha).isoformat() if a.fecha else datetime.date.today().isoformat()
    entrega = pathlib.Path(a.entrega).resolve() if a.entrega else \
        src/"outputs"/f"entrega-{version}"
    if entrega == src or entrega in src.parents:
        ap.error("La entrega no puede ser la fuente ni un directorio que la contenga.")
    if entrega.exists() and any(entrega.iterdir()):
        ap.error("La entrega debe ser nueva o vacía; no se ha sobrescrito nada.")

    zips_usuario = sorted(z for z in (build/"paquetes").glob(f"{SLUG}-*-{version}.zip")
                          if "desarrollo-mantenimiento" not in z.name)
    if len(zips_usuario) != 4:
        print(f"ERROR: se esperaban 4 paquetes de usuario y hay {len(zips_usuario)}. "
              f"Ejecuta antes tools/build_adapters.py"); return 2

    # ---------- paquete de desarrollo y mantenimiento ----------
    dev = build/f"{SLUG}-desarrollo-mantenimiento"
    if dev.exists():
        ap.error("La carpeta de mantenimiento ya existe; usa un build nuevo.")
    (dev/"src").mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dev/"src"/SLUG, ignore=IGNORAR)
    shutil.copytree(src/"tools", dev/"tools", dirs_exist_ok=True, ignore=IGNORAR)
    shutil.copytree(src/"tests", dev/"tests", dirs_exist_ok=True, ignore=IGNORAR)
    (dev/"VERSION").write_text(version + "\n", encoding="utf-8")
    (dev/"paquetes").mkdir(parents=True, exist_ok=True)
    for z in zips_usuario:
        shutil.copy2(z, dev/"paquetes"/z.name)

    # evidencias: validador sobre extracción limpia de cada ZIP
    ev = dev/"evidencias"; ev.mkdir(parents=True, exist_ok=True)
    tmp = build/"_verif"
    if tmp.exists():
        ap.error("La carpeta temporal de verificación ya existe; usa un build nuevo.")
    tmp.mkdir(parents=True)
    salidas = []
    for z in zips_usuario:
        destino = tmp/z.stem
        with zipfile.ZipFile(z) as zf: zf.extractall(destino)
        raiz = next(destino.iterdir())
        r = subprocess.run([sys.executable, str(src/"tests"/"validador_estructura.py"), str(raiz)],
                           capture_output=True, text=True)
        salida = r.stdout + r.stderr
        # Las evidencias no deben contener rutas del equipo de construccion.
        salida = salida.replace(str(raiz), f"<extraccion-limpia>/{raiz.name}")
        salida = salida.replace(str(tmp), "<extraccion-limpia>")
        salida = salida.replace(str(src), "<fuente-canonica>")
        salidas.append((z.name, r.returncode, salida))
        (ev/f"validador_{z.stem}.txt").write_text(
            f"# Validación sobre extracción limpia\nZIP: {z.name}\nSHA-256: {sha256(z)}\n"
            f"Fecha: {hoy}\nCódigo de salida: {r.returncode}\n\n{salida}", encoding="utf-8")

    if any(codigo != 0 for _, codigo, _ in salidas):
        print("ERROR: al menos un ZIP no superó la validación. No se ha creado una entrega final.")
        return 2

    (dev/"README_DESARROLLADOR.md").write_text(f"""# README para desarrollo y mantenimiento

**Sistema:** Aula y Comunidad Educativa Aumentada · **Versión:** `{version}` · **Fecha:** {hoy}
**Estado:** PREPARADO (pruebas de plataforma pendientes para esta evolución)

## Qué hay aquí

| Ruta | Contenido |
|---|---|
| `src/{SLUG}/` | **Fuente canónica.** La única verdad. Todo cambio empieza aquí |
| `tools/build_adapters.py` | Genera los cuatro paquetes de usuario |
| `tools/build_entrega.py` | Genera este paquete y la carpeta de entrega con hashes |
| `tests/validador_estructura.py` | Validación estática de estructura, frontmatter, versión y datos |
| `tests/PLAN_DE_PRUEBAS.md` | Batería completa: estática, común, funcional y negativa |
| `tests/GUION_PRUEBAS_PLATAFORMA.md` | Guion para ejecutar las pruebas pendientes |
| `tests/fixtures/` | Material **ficticio** para las pruebas |
| `paquetes/` | Los cuatro ZIP de usuario de esta misma versión |
| `evidencias/` | Salida del validador sobre extracción limpia de cada ZIP |
| `src/{SLUG}/mantenimiento/` | Arquitectura, dependencias, decisiones, plan de pruebas y evolución |
| `MANIFIESTO.txt` | Inventario completo de archivos con tamaño |
| `SHA256SUMS_INTERNO.txt` | SHA-256 de cada archivo de este paquete |

## Reconstruir todo desde cero

```bash
cd src/{SLUG}
python3 tools/build_adapters.py            # regenera los cuatro paquetes
python3 tools/build_entrega.py             # regenera este paquete y la entrega
python3 tests/validador_estructura.py .    # valida la fuente canónica
```

Requisitos de reconstrucción: **Python 3.8+** para adaptadores y validadores. El generador opcional de
la matriz `.xlsx` necesita `openpyxl` y LibreOffice para recalcular fórmulas.

## Reglas que no se rompen

1. **Nunca** se edita un adaptador a mano. Se edita la fuente y se reconstruye.
2. **Nunca** se certifica un ZIP con evidencia de la fuente, de un adaptador en construcción o de una
   versión anterior.
3. **Nunca** se cambia el contenido de un paquete conservando versión y hash anteriores.
4. Los datos de una entidad usuaria no entran jamás en el paquete distribuible.

## Qué falta para `{version}`

Ejecutar `tests/GUION_PRUEBAS_PLATAFORMA.md` en ChatGPT Work, Claude Cowork y Antigravity sobre los ZIP
finales, registrar el resultado en `tests/REGISTRO_DE_PRUEBAS.md` y, si todo pasa, subir la versión,
reconstruir y recalcular hashes. Ver `src/{SLUG}/mantenimiento/REGISTRO_DECISIONES.md` (D07).

## Edición comunitaria

Esta entrega se ha adaptado desde la fuente 1.3.2. Las instrucciones y la gobernanza JGF se han
consultado en el workspace de mantenimiento, sin incorporarlas como archivos del sistema.
El registro histórico D11 se conserva; no describe la disponibilidad actual de esos documentos.
La skill de portabilidad figura en el índice JGF, pero no estaba instalada en este workspace.
Se aplicó el protocolo maestro y la verificación transversal.

La adaptación no renueva la fecha de corte normativa. Consulta las condiciones comunitarias en
`src/{SLUG}/documentacion/CONDICIONES_DE_USO.md` y el registro comunitario en mantenimiento.
Las evidencias de esta entrega son estáticas: no equivalen a ejecutar conversaciones en cada plataforma.

Los constructores requieren destinos nuevos o vacíos. No borran ni sustituyen entregas anteriores.
""", encoding="utf-8")

    # manifiesto + hashes internos
    lineas, hashes = [], []
    for p in sorted(dev.rglob("*")):
        if p.is_file() and not p.name.startswith("._") and p.name not in ("MANIFIESTO.txt","SHA256SUMS_INTERNO.txt", ".DS_Store"):
            rel = p.relative_to(dev)
            lineas.append(f"{p.stat().st_size:>10}  {rel}")
            hashes.append(f"{sha256(p)}  {rel}")
    (dev/"MANIFIESTO.txt").write_text(
        f"# Manifiesto · {SLUG} · desarrollo y mantenimiento · {version} · {hoy}\n"
        f"# {len(lineas)} archivos\n\n" + "\n".join(lineas) + "\n", encoding="utf-8")
    (dev/"SHA256SUMS_INTERNO.txt").write_text("\n".join(hashes) + "\n", encoding="utf-8")

    zdev = zipdir(dev, build/"paquetes"/f"{SLUG}-desarrollo-mantenimiento-{version}.zip")
    print(f"  ✔ {zdev.name}  ({zdev.stat().st_size/1024:.0f} KB)")

    # ---------- carpeta de entrega ----------
    entrega.mkdir(parents=True, exist_ok=True)
    finales = zips_usuario + [zdev]
    for z in finales:
        shutil.copy2(z, entrega/z.name)

    # Dossier legal y territorial visible sin tener que abrir un ZIP.
    docs_entrega = []
    for nombre in (
        "REFERENCIAS_NORMATIVAS.md",
        "MARCO_LEGAL_FAMILIAS_Y_TUTORIA.md",
        "FUENTES_AUTONOMICAS_EDUCACION_FAMILIAS_TUTORIA.md",
        "GUIA_MAESTRA_DE_USO.md",
        f"GUIA_MAESTRA_DE_USO_AULA_Y_COMUNIDAD_EDUCATIVA_AUMENTADA_{version}.docx",
        "MATRIZ_TRAZABILIDAD_SISTEMA.md",
    ):
        origen = src/"documentacion"/nombre
        if not origen.exists():
            print(f"ERROR: falta el documento de entrega {origen}"); return 2
        nombre_destino = origen.name if origen.stem.endswith(version) else f"{origen.stem}_{version}{origen.suffix}"
        destino = entrega/nombre_destino
        shutil.copy2(origen, destino)
        docs_entrega.append(destino)

    for nombre in ("README_DEMOSTRACIONES.md", "caso_familia_autonomia.md",
                   "caso_tutoria_familia.md", "caso_contraste_autonomico.md",
                   "caso_inicio_curso.md"):
        origen = src/"demo"/nombre
        destino = entrega/f"DEMO_{origen.stem}_{version}{origen.suffix}"
        shutil.copy2(origen, destino)
        docs_entrega.append(destino)

    readme_entrega = entrega/"README_ENTREGA.md"
    readme_entrega.write_text(f"""# Entrega · Aula y Comunidad Educativa Aumentada {version}

Fecha: {hoy}

Origen: Jesús García Fernández · Edición Comunitaria gratuita mediante repositorio oficial.
Sin compra, cupón ni registro en tienda. Público principal:
dirección de institutos, docentes de Secundaria, padres/madres y tutores legales, y tutoría
docente/orientación.

## Paquetes

- ChatGPT Work
- Claude Cowork
- Google Antigravity
- Genérico
- Desarrollo y mantenimiento

## Documentación normativa visible

- `REFERENCIAS_NORMATIVAS_{version}.md`: índice normativo único.
- `MARCO_LEGAL_FAMILIAS_Y_TUTORIA_{version}.md`: marco estatal y europeo desarrollado.
- `FUENTES_AUTONOMICAS_EDUCACION_FAMILIAS_TUTORIA_{version}.md`: fuentes oficiales de las 17 CCAA,
  Ceuta y Melilla, con método de contraste.
- `GUIA_MAESTRA_DE_USO_{version}.md` y su versión DOCX: recorrido completo de adopción y uso.
- `MATRIZ_TRAZABILIDAD_SISTEMA_{version}.md`: requisitos, agentes, workflows, skills, plantillas y pruebas.
- `DEMO_*_{version}.md`: demostraciones sintéticas de inicio de curso, familia, tutoría y contraste autonómico.

Las aplicaciones prácticas son **Sugerencias operativas a revisar y contrastar**. Estos documentos no
certifican vigencia, legalidad ni cumplimiento y no sustituyen al centro, inspección, DPD o asesoría.

Comprueba todos los archivos mediante `SHA256SUMS.txt`.
""", encoding="utf-8")
    docs_entrega.append(readme_entrega)

    sums = [f"{sha256(entrega/z.name)}  {z.name}" for z in finales]
    sums.extend(f"{sha256(p)}  {p.name}" for p in docs_entrega)
    (entrega/"SHA256SUMS.txt").write_text("\n".join(sums) + "\n", encoding="utf-8")
    print("\nEntrega en:", entrega)
    for s in sums: print("   ", s)
    return 0

if __name__ == "__main__":
    sys.exit(main())
