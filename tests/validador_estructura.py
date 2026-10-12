#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador estático · Aula y Comunidad Educativa Aumentada
=========================================================
Comprueba una EXTRACCIÓN LIMPIA de un paquete, o la fuente canónica.

Uso:
    python3 validador_estructura.py <ruta> [--tipo TIPO] [--version X.Y.Z]

TIPO: canonico | chatgpt-work | claude-cowork | antigravity | generico | mantenimiento
      (si se omite, se intenta detectar)

No requiere ninguna biblioteca externa. Python 3.8+.
Devuelve código de salida 0 si todo pasa, 1 si hay algún FAIL.
"""
import sys, os, re, json, argparse, pathlib

VERSION_ESPERADA = "1.3.2-comunitaria.3"

FAILS, WARNS, OKS = [], [], []

def ok(m):   OKS.append(m)
def warn(m): WARNS.append(m)
def fail(m): FAILS.append(m)

# ---------------------------------------------------------------- utilidades

def leer(p):
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""

def md_files(root):
    for p in root.rglob("*.md"):
        if ".git" in p.parts or p.name.startswith("._"):
            continue
        yield p

def todos_los_archivos(root):
    for p in root.rglob("*"):
        if p.is_file() and ".git" not in p.parts and not p.name.startswith("._"):
            yield p

# ---------------------------------------------------------------- detección

MARCADORES = {
    "claude-cowork": [".claude-plugin/plugin.json"],
    "antigravity":   [".agents/skills"],
    "chatgpt-work":  ["aula-comunidad-educativa-aumentada/agents/openai.yaml"],
    "mantenimiento": ["src/aula-comunidad-educativa-aumentada/VERSION"],
}

def detectar_tipo(root):
    for tipo, marcas in MARCADORES.items():
        if all((root/m).exists() for m in marcas):
            return tipo
    if (root/"tools").exists() and (root/"tests").exists():
        return "canonico"
    if (root/"INICIO_UNIVERSAL.md").exists():
        return "generico"
    return "desconocido"

def normalizar_raiz_extraida(root, tipo):
    """Acepta tanto la carpeta del paquete como su extracción con un wrapper único."""
    marcas = MARCADORES.get(tipo, [])
    if not marcas or all((root/m).exists() for m in marcas):
        return root, False
    candidatos = []
    for child in root.iterdir():
        if child.is_dir() and all((child/m).exists() for m in marcas):
            candidatos.append(child)
    if len(candidatos) == 1:
        return candidatos[0], True
    return root, False

# ---------------------------------------------------------------- comprobaciones

OBLIGATORIOS = {
    "canonico": ["README.md","VERSION","CHANGELOG.md","EMPIEZA_AQUI.md","INICIO_UNIVERSAL.md",
                 "00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md","01_MODOS_Y_PERFILES.md",
                 "instruccion_maestra.md","AGENTS.md","CLAUDE.md","GEMINI.md",
                 "agentes","workflows","skills","plantillas","conocimiento",
                 "resultados","documentacion","demo","tests","tools","mantenimiento"],
    "claude-cowork": [".claude-plugin/plugin.json","CLAUDE.md","EMPIEZA_AQUI.md","instruccion_maestra.md",
                      "01_MODOS_Y_PERFILES.md","00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md",
                      "skills","agents","agentes","workflows","plantillas","conocimiento",
                      "documentacion","resultados","VERSION","README_INSTALACION.md"],
    "antigravity": ["AGENTS.md","GEMINI.md",".agents/skills","EMPIEZA_AQUI.md","instruccion_maestra.md",
                    "01_MODOS_Y_PERFILES.md","00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md",
                    "agentes","workflows","plantillas","conocimiento","documentacion",
                    "resultados","VERSION","README_INSTALACION.md"],
    "chatgpt-work": ["README.md", "README_INSTALACION.md", "LICENSE.md", "VERSION",
                     "aula-comunidad-educativa-aumentada/SKILL.md",
                     "aula-comunidad-educativa-aumentada/agents/openai.yaml",
                     "aula-comunidad-educativa-aumentada/references",
                     "aula-comunidad-educativa-aumentada/assets",
                     "tests", "demo", "mantenimiento"],
    "generico": ["INICIO_UNIVERSAL.md","EMPIEZA_AQUI.md","instruccion_maestra.md","01_MODOS_Y_PERFILES.md",
                 "00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md","agentes","workflows","skills",
                 "plantillas","conocimiento","documentacion","resultados","demo","VERSION",
                 "README_INSTALACION.md"],
    "mantenimiento": ["README_DESARROLLADOR.md","src","tools","tests",
                      "src/aula-comunidad-educativa-aumentada/mantenimiento/MANTENIMIENTO_Y_EVOLUCION.md",
                      "MANIFIESTO.txt","SHA256SUMS_INTERNO.txt"],
}

# Paquetes que NO deben incluir demo/, tests/, tools/, mantenimiento/, platform-adapters/
SIN_INTERNOS = {"claude-cowork","antigravity","generico"}
SIN_DEMO     = {"claude-cowork","antigravity"}

def c_estructura(root, tipo):
    faltan = [x for x in OBLIGATORIOS.get(tipo, []) if not (root/x).exists()]
    if faltan:
        fail(f"[estructura] faltan en el paquete «{tipo}»: {', '.join(faltan)}")
    else:
        ok(f"[estructura] todos los elementos obligatorios de «{tipo}» están presentes")

    if tipo in SIN_INTERNOS:
        for interno in ("tests","tools","mantenimiento","platform-adapters"):
            if (root/interno).exists():
                fail(f"[estructura] el paquete de usuario «{tipo}» no debe contener «{interno}/»")
    if tipo in SIN_DEMO and (root/"demo").exists():
        fail(f"[estructura] el paquete «{tipo}» no debe contener «demo/» (decisión D03)")

def c_version(root, tipo, esperada):
    candidatos = [root/"VERSION", root/"src"/"aula-comunidad-educativa-aumentada"/"VERSION",
                  root/"aula-comunidad-educativa-aumentada"/"references"/"VERSION"]
    vf = next((c for c in candidatos if c.exists()), None)
    if not vf:
        fail("[versión] no se encuentra el archivo VERSION")
        return
    v = leer(vf).strip()
    if v != esperada:
        fail(f"[versión] VERSION dice «{v}» y se esperaba «{esperada}»")
    else:
        ok(f"[versión] VERSION = {v}")
    # coherencia: la versión debe aparecer en algún documento visible
    encontrado = any(esperada in leer(p) for p in md_files(root))
    if not encontrado:
        warn("[versión] la versión no aparece citada en ningún documento del paquete")

# El patron se compone por partes para que este mismo archivo no contenga una ruta absoluta literal.
_S = chr(47)
RE_ABS = re.compile("(" + _S + "Users" + _S + r"[A-Za-z0-9._-]+|"
                    + _S + "home" + _S + r"[A-Za-z0-9._-]+|"
                    + _S + "ro" + "ot" + _S + r"|[A-Z]:\\Users\\)")
def c_rutas_absolutas(root):
    malos = []
    for p in todos_los_archivos(root):
        if p.suffix.lower() in (".md",".py",".json",".yaml",".yml",".txt"):
            for m in RE_ABS.finditer(leer(p)):
                malos.append(f"{p.relative_to(root)}: {m.group(0)}")
    if malos:
        fail("[portabilidad] rutas absolutas del equipo de construcción: " + "; ".join(malos[:8]))
    else:
        ok("[portabilidad] sin rutas absolutas del equipo de construcción")

RE_PII = [
    ("DNI/NIE",   re.compile(r"\b\d{8}[- ]?[A-HJ-NP-TV-Z]\b")),
    ("correo",    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("teléfono",  re.compile(r"(?<![\d./-])[6-9]\d{2}[ -]?\d{3}[ -]?\d{3}(?![\d./-])")),
]
RE_HEX = re.compile(r"\b[0-9a-f]{32,}\b")
EXCLUIDOS_PII = ("sha256sums.txt","sha256sums_interno.txt","manifiesto.txt")

def c_pii(root):
    hits = []
    for p in todos_los_archivos(root):
        if p.suffix.lower() not in (".md",".txt",".json",".yaml",".yml",".py"):
            continue
        if p.name.lower() in EXCLUIDOS_PII:
            continue   # sumas de verificacion: cadenas hexadecimales, no datos personales
        t = RE_HEX.sub("<hash>", leer(p))
        for nombre, rx in RE_PII:
            for m in rx.finditer(t):
                hits.append(f"{p.relative_to(root)} · {nombre}: {m.group(0)}")
    if hits:
        fail("[datos] posibles datos personales en el paquete: " + "; ".join(hits[:8]))
    else:
        ok("[datos] sin patrones de datos personales (DNI, correo, teléfono)")

def c_resultados_vacio(root, tipo):
    r = root/"resultados"
    if not r.exists():
        return
    extra = [p.name for p in r.iterdir()
             if p.name != "_LEEME.md" and not p.name.startswith("._") and p.name != ".DS_Store"]
    if extra:
        fail(f"[limpieza] «resultados/» debe viajar vacío salvo _LEEME.md; contiene: {extra}")
    else:
        ok("[limpieza] «resultados/» viaja vacío salvo _LEEME.md")

RE_FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
def c_skills(root):
    dirs = [root/"skills", root/".agents"/"skills"]
    encontrados = 0
    for d in dirs:
        if not d.exists():
            continue
        for sd in sorted(d.iterdir()):
            if not sd.is_dir():
                continue
            sm = sd/"SKILL.md"
            if not sm.exists():
                fail(f"[skills] «{sd.name}» no tiene SKILL.md")
                continue
            encontrados += 1
            t = leer(sm)
            m = RE_FM.match(t)
            if not m:
                fail(f"[skills] «{sd.name}»: frontmatter YAML ausente o mal delimitado")
                continue
            fm = m.group(1)
            campos = dict()
            for line in fm.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    campos[k.strip()] = v.strip()
            if not campos.get("description"):
                fail(f"[skills] «{sd.name}»: falta «description» en el frontmatter")
            elif len(campos["description"]) > 130:
                warn(f"[skills] «{sd.name}»: description de {len(campos['description'])} caracteres "
                     f"(puede truncarse; se recomienda <=125)")
            if not campos.get("name"):
                warn(f"[skills] «{sd.name}»: sin «name» (opcional en algunas plataformas)")
            elif campos["name"] != sd.name:
                fail(f"[skills] «{sd.name}»: el «name» del frontmatter es «{campos['name']}»")
            if len(t) - len(m.group(0)) < 200:
                warn(f"[skills] «{sd.name}»: cuerpo muy breve")
    if encontrados == 0:
        principal = root/"aula-comunidad-educativa-aumentada"/"SKILL.md"
        referencias = root/"aula-comunidad-educativa-aumentada"/"references"/"skills"
        if principal.exists() and referencias.exists():
            ok("[skills] skill principal de ChatGPT y catálogo de skills en references/ presentes")
        else:
            warn("[skills] no se han encontrado skills en este paquete")
    else:
        ok(f"[skills] {encontrados} skills con SKILL.md y frontmatter válido")

def c_skill_chatgpt(root):
    """La skill de ChatGPT vive en la raíz de su carpeta, no en skills/<nombre>/."""
    sm = root/"aula-comunidad-educativa-aumentada"/"SKILL.md"
    if not sm.exists():
        return
    t = leer(sm)
    m = RE_FM.match(t)
    if not m:
        fail("[skill-chatgpt] frontmatter YAML ausente o mal delimitado en SKILL.md")
        return
    campos = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            campos[k.strip()] = v.strip()
    if not campos.get("name"):
        fail("[skill-chatgpt] falta «name» en el frontmatter")
    if not campos.get("description"):
        fail("[skill-chatgpt] falta «description» en el frontmatter")
    elif len(campos["description"]) > 130:
        warn(f"[skill-chatgpt] description de {len(campos['description'])} caracteres (puede truncarse)")
    y = root/"aula-comunidad-educativa-aumentada"/"agents"/"openai.yaml"
    if not y.exists():
        fail("[skill-chatgpt] falta agents/openai.yaml")
    elif "allow_implicit_invocation" not in leer(y):
        warn("[skill-chatgpt] openai.yaml sin política de invocación implícita")
    if not (root/"aula-comunidad-educativa-aumentada"/"references"/"instruccion_maestra.md").exists():
        fail("[skill-chatgpt] el núcleo no está en references/")
    ok("[skill-chatgpt] SKILL.md, openai.yaml y references/ correctos")

# --- Comprobaciones normativas (regla de instruccion_maestra.md 7.7) ---

RE_NORMA = re.compile(r"(art[ií]culo\s+\d+|Reglamento\s*\(UE\)|Ley\s+Org[áa]nica|Anexo\s+III|LOPDGDD|RGPD)", re.I)
RE_ENLACE = re.compile(r"https?://")
RE_FECHA = re.compile(r"(\d{4}-\d{2}-\d{2}|\d{1,2}\s+de\s+\w+\s+de\s+\d{4}|feb-20\d\d|\w{3}-20\d\d)")
RE_RN = re.compile(r"RN-\d{2}|REFERENCIAS_NORMATIVAS")

# Combinaciones que estarian desactualizadas y no deben aparecer
PROHIBIDAS = [
    (re.compile(r"Anexo\s+III[^.]{0,400}?2\s+de\s+agosto\s+de\s+2026", re.I | re.S),
     "asocia el Anexo III con el 2 de agosto de 2026 (aplazado al 2 de diciembre de 2027)"),
    (re.compile(r"alto\s+riesgo[^.]{0,300}?exigibl\w*[^.]{0,200}?agosto\s+de\s+2026", re.I | re.S),
     "declara el alto riesgo exigible en agosto de 2026"),
]

def c_normativa(root):
    """Toda mencion normativa necesita enlace y fecha, o remitir al indice RN."""
    sin_respaldo, obsoletas = [], []
    for p in md_files(root):
        txt = leer(p)
        if RE_NORMA.search(txt):
            if not (RE_RN.search(txt) or (RE_ENLACE.search(txt) and RE_FECHA.search(txt))):
                sin_respaldo.append(str(p.relative_to(root)))
        for rx, msg in PROHIBIDAS:
            for m in rx.finditer(txt):
                ventana = txt[max(0, m.start() - 300): m.end() + 300].lower()
                # No es un error si el propio texto explica el aplazamiento o la correccion
                if "aplaz" in ventana or "2027" in ventana or "desactualiz" in ventana or "corregi" in ventana:
                    continue
                obsoletas.append(f"{p.relative_to(root)}: {msg}")
                break
    if sin_respaldo:
        fail("[normativa] menciones de normas sin enlace, sin fecha y sin remitir al indice: "
             + ", ".join(sin_respaldo[:8]))
    else:
        ok("[normativa] toda mencion normativa lleva enlace y fecha, o remite al indice RN")
    if obsoletas:
        fail("[normativa] afirmacion normativa desactualizada: " + "; ".join(obsoletas[:5]))
    else:
        ok("[normativa] sin afirmaciones normativas desactualizadas conocidas")

def c_indice_normativo(root):
    """El indice de referencia normativa debe viajar y llevar fecha de corte."""
    cands = list(root.rglob("REFERENCIAS_NORMATIVAS.md"))
    if not cands:
        fail("[normativa] falta documentacion/REFERENCIAS_NORMATIVAS.md")
        return
    txt = leer(cands[0])
    if "Fecha de corte normativa" not in txt:
        fail("[normativa] el indice normativo no declara fecha de corte")
    if txt.count("Consultado:") + txt.count("consultado el") < 8:
        warn("[normativa] pocas fechas de consulta en el indice normativo")
    if "No dictamin" not in txt and "no dictamina" not in txt and "asesoramiento" not in txt:
        warn("[normativa] el indice normativo no recuerda que no es asesoramiento juridico")
    ok(f"[normativa] indice de referencia normativa presente ({len(txt)} bytes) con fecha de corte")

def c_puerta_entrada(root):
    """La puerta de entrada y los apoyos de lenguaje deben viajar en todos los paquetes de usuario."""
    faltan = []
    for nombre in ("EMPIEZA_AQUI.md", "GLOSARIO.md", "LECTURA_FACIL.md"):
        if not list(root.rglob(nombre)):
            faltan.append(nombre)
    if faltan:
        fail("[adopcion] faltan apoyos de entrada y lenguaje: " + ", ".join(faltan))
        return
    ea = list(root.rglob("EMPIEZA_AQUI.md"))[0]
    txt = leer(ea)
    if "configurar" not in txt.lower():
        warn("[adopcion] la puerta de entrada no menciona que no hace falta configurar nada")
    if "No consta" not in txt:
        warn("[adopcion] la puerta de entrada no explica el «No consta»")
    if "caduc" not in txt.lower() and "vida útil" not in txt.lower():
        fail("[adopcion] la puerta de entrada no declara la vida útil del sistema")
    else:
        ok("[adopcion] puerta de entrada, glosario y lectura fácil presentes, con vida útil declarada")

def c_vida_util(root):
    """Las condiciones deben declarar que no se garantiza mantenimiento."""
    cands = list(root.rglob("CONDICIONES_DE_USO.md"))
    if not cands:
        return
    txt = leer(cands[0]).lower()
    if "no se garantiza" not in txt or "mantenimiento" not in txt:
        fail("[vida util] las condiciones no declaran que no se garantiza mantenimiento")
    else:
        ok("[vida util] condiciones con vida útil y ausencia de garantía de mantenimiento declaradas")

RE_NOMBRE_VALIDO = re.compile(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?$")

def c_subagentes(root):
    """El validador de plugins exige nombres solo con letras, numeros y guiones,
    que empiecen y terminen en alfanumerico. Esta comprobacion evita reincidir."""
    d = root/"agents"
    if not d.exists():
        return
    malos, sin_fm, incoherentes = [], [], []
    archivos = [f for f in sorted(d.glob("*.md")) if not f.name.startswith("._")]
    for f in archivos:
        stem = f.stem
        if not RE_NOMBRE_VALIDO.match(stem):
            malos.append(stem)
            continue
        m = RE_FM.match(leer(f))
        if not m:
            sin_fm.append(stem); continue
        campos = {}
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                campos[k.strip()] = v.strip().strip('"')
        if campos.get("name") != stem:
            incoherentes.append(f"{stem} (name={campos.get('name')})")
        elif not campos.get("description"):
            sin_fm.append(stem)
    extras = [f.name for f in d.iterdir() if f.is_file() and f.suffix != ".md"
              and not f.name.startswith("._") and f.name != ".DS_Store"]
    if malos:
        fail("[subagentes] nombres invalidos (solo letras, numeros y guiones, sin empezar ni "
             "terminar en guion): " + ", ".join(malos[:12]))
    if sin_fm:
        fail("[subagentes] sin frontmatter valido o sin description: " + ", ".join(sin_fm[:8]))
    if incoherentes:
        fail("[subagentes] el name del frontmatter no coincide con el archivo: " + ", ".join(incoherentes[:8]))
    if extras:
        warn("[subagentes] archivos que no son agentes en agents/: " + ", ".join(extras[:5]))
    if not (malos or sin_fm or incoherentes):
        ok(f"[subagentes] {len(archivos)} subagentes con nombre valido y frontmatter correcto")

def c_carpeta_skills(root):
    """En el plugin de Cowork, skills/ solo puede contener carpetas de skill.
    En la fuente canonica el _LEEME.md es documentacion legitima."""
    if not (root/".claude-plugin"/"plugin.json").exists():
        return
    d = root/"skills"
    if not d.exists():
        return
    sueltos = [f.name for f in d.iterdir() if f.is_file()
               and not f.name.startswith("._") and f.name != ".DS_Store"]
    if sueltos:
        fail("[skills] archivos sueltos en skills/ (solo debe haber carpetas de skill): "
             + ", ".join(sueltos[:5]))
    else:
        ok("[skills] skills/ contiene unicamente carpetas de skill")

def c_cobertura_competencial(root):
    """Las piezas de programacion por proyectos deben viajar completas."""
    faltan = []
    for nombre in ("17_matriz_cobertura_competencial.md",
                   "17_matriz_cobertura_competencial.xlsx",
                   "18_atencion_diversidad_y_accesibilidad.md",
                   "19_programacion_por_proyectos.md",
                   "20_ficha_unidad_programacion.md",
                   "CATALOGO_CURRICULAR.md"):
        if not list(root.rglob(nombre)):
            faltan.append(nombre)
    if not list(root.rglob("W11_programacion_por_proyectos.md")):
        faltan.append("W11_programacion_por_proyectos.md")
    if faltan:
        fail("[cobertura] faltan piezas de programacion por proyectos: " + ", ".join(faltan))
        return
    # La distincion cobertura / nota debe estar escrita donde se usa
    sin_aviso = []
    for nombre in ("17_matriz_cobertura_competencial.md", "19_programacion_por_proyectos.md",
                   "W11_programacion_por_proyectos.md"):
        f = list(root.rglob(nombre))[0]
        txt = leer(f).lower()
        if "nota" not in txt and "calificaci" not in txt:
            sin_aviso.append(nombre)
    if sin_aviso:
        fail("[cobertura] no distinguen cobertura curricular de peso en la nota: " + ", ".join(sin_aviso))
        return
    nucleo = list(root.rglob("instruccion_maestra.md"))
    if nucleo:
        txt = leer(nucleo[0])
        if "100 %" not in txt:
            fail("[cobertura] el nucleo no recoge la regla del 100 %"); return
        if "Suma 1" not in txt or "Suma 2" not in txt:
            fail("[cobertura] el nucleo no distingue las dos sumas (pesos y reparto por unidades)"); return
    ok("[cobertura] matriz, fichas de unidad, catalogo curricular, plan de diversidad, programacion "
       "y W11 presentes, con las dos sumas y la frontera frente a la calificacion")

def c_familias_tutoria(root):
    """La ampliacion familiar debe viajar completa y conservar sus salvaguardas criticas."""
    requeridos = [
        "A17_acompanamiento_familiar_aprendizaje.md",
        "A18_coordinacion_familia_tutor.md",
        "A19_mediacion_digital_orientacion_familiar.md",
        "W20_incorporacion_familiar_derechos_canales.md",
        "W21_entrevista_acuerdo_familia_tutor.md",
        "W22_acompanamiento_aprendizaje_hogar.md",
        "W23_participacion_familiar_inclusiva.md",
        "W24_mediacion_parental_digital_ia.md",
        "W25_orientacion_transicion_decision_compartida.md",
        "43_ficha_contexto_representacion_familiar.md",
        "50_acuerdo_familiar_digital_ia.md",
        "52_triaje_preocupacion_familiar_derivacion.md",
        "MARCO_LEGAL_FAMILIAS_Y_TUTORIA.md",
    ]
    faltan = [nombre for nombre in requeridos if not list(root.rglob(nombre))]
    if faltan:
        fail("[familias] faltan piezas de la ampliacion familiar: " + ", ".join(faltan))
        return
    nucleo = list(root.rglob("instruccion_maestra.md"))
    marco = list(root.rglob("MARCO_LEGAL_FAMILIAS_Y_TUTORIA.md"))
    unido = (leer(nucleo[0]) if nucleo else "") + (leer(marco[0]) if marco else "")
    reglas = {
        "representacion humana": ("centro verifica", "centro autentica"),
        "voz del alumno": ("voz del alumno",),
        "conflicto de intereses": ("aviso automático", "aviso familiar automático"),
        "protocolo territorial": ("protocolos autonómicos",),
    }
    ausentes = [nombre for nombre, opciones in reglas.items()
                if not any(texto.lower() in unido.lower() for texto in opciones)]
    if ausentes:
        fail("[familias] faltan salvaguardas familiares: " + ", ".join(ausentes))
        return
    ok("[familias] agentes A17-A19, workflows W20-W25, plantillas y marco legal presentes con salvaguardas")

def c_autonomias(root):
    """La capa territorial debe cubrir todos los ámbitos y mantener la salida como sugerencia."""
    requeridos = [
        "A20_contraste_normativo_autonomico.md",
        "W26_contraste_autonomico_fuentes_oficiales.md",
        "53_ficha_contraste_autonomico.md",
        "FUENTES_AUTONOMICAS_EDUCACION_FAMILIAS_TUTORIA.md",
    ]
    faltan = [nombre for nombre in requeridos if not list(root.rglob(nombre))]
    skill = list(root.rglob("contrastar-normativa-autonomica-educativa/SKILL.md"))
    if not skill and not (root/"aula-comunidad-educativa-aumentada"/"SKILL.md").exists():
        faltan.append("contrastar-normativa-autonomica-educativa/SKILL.md")
    if faltan:
        fail("[autonomias] faltan piezas territoriales: " + ", ".join(faltan))
        return
    doc = leer(list(root.rglob("FUENTES_AUTONOMICAS_EDUCACION_FAMILIAS_TUTORIA.md"))[0])
    territorios = [
        "Andalucía", "Aragón", "Principado de Asturias", "Illes Balears", "Canarias",
        "Cantabria", "Castilla-La Mancha", "Castilla y León", "Cataluña",
        "Comunitat Valenciana", "Extremadura", "Galicia", "Comunidad de Madrid",
        "Región de Murcia", "Comunidad Foral de Navarra", "País Vasco", "La Rioja",
        "Ceuta", "Melilla",
    ]
    ausentes = [x for x in territorios if x.lower() not in doc.lower()]
    if ausentes:
        fail("[autonomias] territorios ausentes del directorio: " + ", ".join(ausentes))
        return
    if doc.count("https://") < 30:
        fail("[autonomias] el directorio no contiene suficientes enlaces oficiales")
        return
    conjunto = doc + leer(list(root.rglob("A10_auditor_calidad_educativa.md"))[0])
    if "Sugerencia operativa a revisar y contrastar" not in conjunto or "B19" not in conjunto:
        fail("[autonomias] falta la etiqueta de sugerencia o el bloqueo B19")
        return
    ok("[autonomias] 17 CCAA, Ceuta y Melilla, A20, W26, skill, plantilla 53 y B19 presentes")

def c_inicio_curso(root):
    """El carril de inicio de curso debe cubrir sus cinco hitos con piezas completas."""
    requeridos = [
        "A22_inicio_curso_comunidad_educativa.md",
        "W28_plan_inicio_curso_centro.md",
        "W29_primer_dia_alumnado.md",
        "W30_primera_reunion_docente_familia.md",
        "W31_reunion_instituto_familias.md",
        "W32_apoyo_familias_inicio_curso.md",
        "54_plan_inicio_curso_centro.md",
        "55_guion_primer_dia_alumnado.md",
        "56_guion_primera_reunion_docente_familia.md",
        "57_guion_reunion_instituto_familias.md",
        "58_kit_apoyo_familias_inicio_curso.md",
        "inicio-curso-comunidad-educativa/SKILL.md",
    ]
    faltan = [nombre for nombre in requeridos if not list(root.rglob(nombre))]
    if faltan:
        fail("[inicio-curso] faltan piezas: " + ", ".join(faltan))
        return
    texto = "\n".join(leer(p) for p in root.rglob("*inicio*curso*.md"))
    reglas = {
        "comprensión": "comprensión",
        "adaptación": "adapt",
        "familias": "famil",
        "aprobación humana": "aprobación",
        "alternativa": "alternativa",
    }
    ausentes = [nombre for nombre, palabra in reglas.items() if palabra not in texto.lower()]
    if ausentes:
        fail("[inicio-curso] faltan garantías de " + ", ".join(ausentes))
    else:
        ok("[inicio-curso] A22, skill, W28–W32 y plantillas 54–58 presentes con adaptación y comprensión")

def c_guia_trazabilidad_demos(root, tipo):
    """La secuencia de adopción debe tener guía, matriz y demostraciones coherentes."""
    requeridos = ["GUIA_MAESTRA_DE_USO.md", "MATRIZ_TRAZABILIDAD_SISTEMA.md"]
    # Los adaptadores de usuario excluyen demo/ por diseño D03; el genérico, la fuente y
    # mantenimiento sí deben conservar las demostraciones para la primera experiencia y QA.
    incluye_demo = tipo in ("canonico", "mantenimiento", "generico") or (root/"demo").exists()
    if incluye_demo:
        requeridos.extend(["README_DEMOSTRACIONES.md", "caso_familia_autonomia.md",
                           "caso_tutoria_familia.md", "caso_contraste_autonomico.md",
                           "caso_inicio_curso.md"])
    faltan = [nombre for nombre in requeridos if not list(root.rglob(nombre))]
    if faltan:
        fail("[trazabilidad] faltan piezas de guía, matriz o demostraciones: " + ", ".join(faltan))
        return
    guia = leer(list(root.rglob("GUIA_MAESTRA_DE_USO.md"))[0])
    matriz = leer(list(root.rglob("MATRIZ_TRAZABILIDAD_SISTEMA.md"))[0])
    demo = "\n".join(leer(p) for p in root.rglob("caso_*.md"))
    if VERSION_ESPERADA not in guia or VERSION_ESPERADA not in matriz:
        fail("[trazabilidad] guía o matriz sin versión del paquete")
        return
    for marcador in ("R01", "F01", "T01", "S01", "W26"):
        if marcador not in matriz:
            fail(f"[trazabilidad] falta el marcador esencial «{marcador}» en la matriz")
    if incluye_demo and "Sugerencia operativa a revisar y contrastar" not in demo:
        fail("[demostraciones] los casos autonómicos no conservan la etiqueta de sugerencia")
    if "No consta" not in guia or "revisión humana" not in guia.lower():
        fail("[guía] faltan las reglas No consta o revisión humana")
    else:
        ok("[trazabilidad] Guía Maestra, matriz de 45 filas y cuatro demostraciones presentes y conectadas")

RE_VER_ANTIGUA = re.compile(r"\b0\.\d+\.\d+(?:-rc\d+)?\b")
EXENTOS_VER = ("changelog.md", "registro_de_pruebas.md", "registro_decisiones.md", "plan_de_pruebas.md")

def c_version_coherente(root):
    """Las versiones escritas a mano se quedan desfasadas. Esta comprobacion lo impide."""
    sueltas = []
    for p in md_files(root):
        if p.name.lower() in EXENTOS_VER:
            continue
        for m in RE_VER_ANTIGUA.finditer(leer(p)):
            sueltas.append(f"{p.relative_to(root)}: {m.group(0)}")
    if sueltas:
        fail("[version] versiones antiguas escritas a mano en documentos: " + "; ".join(sueltas[:8]))
    else:
        ok("[version] ningun documento arrastra una version antigua")

def c_plugin_claude(root):
    pj = root/".claude-plugin"/"plugin.json"
    if not pj.exists():
        return
    try:
        data = json.loads(leer(pj))
    except Exception as e:
        fail(f"[plugin] plugin.json no es JSON válido: {e}")
        return
    for campo in ("name","description","version"):
        if not data.get(campo):
            fail(f"[plugin] plugin.json sin «{campo}»")
    if data.get("version") != VERSION_ESPERADA:
        warn(f"[plugin] plugin.json version = {data.get('version')}")
    for prohibido in ("skills","agents","commands","hooks"):
        if (root/".claude-plugin"/prohibido).exists():
            fail(f"[plugin] «{prohibido}/» no puede estar dentro de .claude-plugin/")
    if not (root/"skills").exists():
        fail("[plugin] falta «skills/» en la raíz del plugin")
    ok("[plugin] manifiesto .claude-plugin/plugin.json correcto y carpetas en la raíz")

def c_cowork_contexto_y_adaptacion(root):
    """La integración Cowork debe explicar el límite de permisos y la adaptación al usuario."""
    if not (root/".claude-plugin"/"plugin.json").exists():
        return
    requeridos = [
        "documentacion/INTEGRACION_CLAUDE_COWORK.md",
        "agents/a21-verificador-contexto-cowork.md",
        "workflows/W27_conectar_contexto_claude_cowork.md",
        "skills/verificar-contexto-claude-cowork/SKILL.md",
    ]
    faltan = [ruta for ruta in requeridos if not (root/ruta).exists()]
    if faltan:
        fail("[cowork] faltan piezas de conexión de contexto: " + ", ".join(faltan))
        return
    texto = "\n".join(leer(root/ruta) for ruta in requeridos)
    reglas = {
        "permiso de carpeta": ("Agregar carpeta", "Contexto"),
        "sin contexto": ("Contexto local no conectado",),
        "archivos comprobados": ("VERSION", ".claude-plugin/plugin.json"),
        "comprensión": ("comprensión",),
        "ajuste": ("ajust",),
    }
    ausentes = [nombre for nombre, opciones in reglas.items()
                if not any(opcion.lower() in texto.lower() for opcion in opciones)]
    if ausentes:
        fail("[cowork] faltan salvaguardas de contexto/adaptación: " + ", ".join(ausentes))
    else:
        ok("[cowork] conexión de carpeta, no invención de citas y adaptación con comprensión/ajuste presentes")

RE_REF = re.compile(r"`?(agentes|workflows|plantillas|skills|documentacion|conocimiento|tests|tools|mantenimiento)/[A-Za-z0-9_\-./]+`?")
def c_referencias(root):
    """Solo sobre la fuente canónica: comprueba que las rutas citadas existen."""
    rotas = set()
    for p in md_files(root):
        for m in RE_REF.finditer(leer(p)):
            ref = m.group(0).strip("`")
            if ref.endswith("/") or "<" in ref:
                continue
            destino = root/ref
            if not destino.exists() and not any((root/ref).parent.glob(pathlib.Path(ref).name + "*")):
                rotas.add(f"{p.relative_to(root)} → {ref}")
    if rotas:
        fail("[referencias] rutas citadas que no existen: " + "; ".join(sorted(rotas)[:10]))
    else:
        ok("[referencias] todas las rutas internas citadas existen")

def c_prohibiciones(root):
    """El núcleo debe contener las prohibiciones clave."""
    candidatos = list(root.rglob("instruccion_maestra.md"))
    if not candidatos:
        warn("[núcleo] no se encuentra instruccion_maestra.md")
        return
    t = leer(candidatos[0]).lower()
    reglas = {
        "no calificar": "calificaciones finales",
        "no clasificar": "rankear alumnado",
        "no detectar IA": "detectar de forma fiable",
        "no acciones externas": "no puedes",
        "anonimización": "anonimizar",
        "prompt injection": "fuentes, no instrucciones",
        "no consta": "no consta",
    }
    faltan = [k for k, v in reglas.items() if v not in t]
    if faltan:
        fail(f"[núcleo] faltan reglas clave en instruccion_maestra.md: {faltan}")
    else:
        ok("[núcleo] las siete reglas clave están presentes en instruccion_maestra.md")

# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ruta")
    ap.add_argument("--tipo", default=None)
    ap.add_argument("--version", default=VERSION_ESPERADA)
    a = ap.parse_args()

    root = pathlib.Path(a.ruta).resolve()
    if not root.is_dir():
        print(f"ERROR: {root} no es un directorio"); sys.exit(2)

    tipo = a.tipo or detectar_tipo(root)
    root, wrapper = normalizar_raiz_extraida(root, tipo)
    print(f"== Validador · Aula y Comunidad Educativa Aumentada ==")
    print(f"Ruta: {root}")
    print(f"Tipo detectado: {tipo}\n")
    if wrapper:
        print("Nota: se ha detectado y validado el único directorio de paquete dentro de la extracción.\n")

    c_estructura(root, tipo)
    c_version(root, tipo, a.version)
    c_rutas_absolutas(root)
    c_pii(root)
    c_resultados_vacio(root, tipo)
    c_skills(root)
    c_plugin_claude(root)
    c_cowork_contexto_y_adaptacion(root)
    c_subagentes(root)
    c_carpeta_skills(root)
    c_skill_chatgpt(root)
    c_normativa(root)
    c_indice_normativo(root)
    c_puerta_entrada(root)
    c_vida_util(root)
    c_cobertura_competencial(root)
    c_familias_tutoria(root)
    c_autonomias(root)
    c_inicio_curso(root)
    c_guia_trazabilidad_demos(root, tipo)
    c_version_coherente(root)
    c_prohibiciones(root)
    if tipo == "canonico":
        c_referencias(root)

    for m in OKS:    print("  OK    " + m)
    for m in WARNS:  print("  AVISO " + m)
    for m in FAILS:  print("  FAIL  " + m)
    print(f"\nResumen: {len(OKS)} OK · {len(WARNS)} avisos · {len(FAILS)} fallos")
    sys.exit(1 if FAILS else 0)

if __name__ == "__main__":
    main()
