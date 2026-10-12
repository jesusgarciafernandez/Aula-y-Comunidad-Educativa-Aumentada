#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera plantillas/17_matriz_cobertura_competencial.xlsx
Matriz de cobertura competencial con sumas y avisos automáticos.

Uso:  python3 tools/gen_matriz_cobertura.py
Requiere openpyxl. Después hay que recalcular con LibreOffice.
"""
import pathlib, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule
from openpyxl.utils import get_column_letter

RAIZ = pathlib.Path(__file__).resolve().parents[1]
DESTINO = RAIZ/"plantillas"/"17_matriz_cobertura_competencial.xlsx"

VERDE   = "1F4F42"
SUAVE   = "E8F0ED"
AMARILLO= "FFF3CD"
BORDE   = Side(style="thin", color="B9C7C1")
CAJA    = Border(left=BORDE, right=BORDE, top=BORDE, bottom=BORDE)

F_TIT   = Font(name="Arial", size=14, bold=True, color=VERDE)
F_SUB   = Font(name="Arial", size=11, bold=True, color=VERDE)
F_CAB   = Font(name="Arial", size=10, bold=True, color="FFFFFF")
F_TXT   = Font(name="Arial", size=10)
F_TXT_B = Font(name="Arial", size=10, bold=True)
F_NOTA  = Font(name="Arial", size=9, italic=True, color="5B6B66")
R_CAB   = PatternFill("solid", fgColor=VERDE)
R_SUAVE = PatternFill("solid", fgColor=SUAVE)
R_EDIT  = PatternFill("solid", fgColor=AMARILLO)

N_CE, N_PROY = 8, 6
FILA_CAB, FILA_INI = 6, 7
FILA_FIN = FILA_INI + N_CE - 1
COL_INI = 2                              # B
COL_FIN = COL_INI + N_PROY - 1           # G
COL_SUMA, COL_DIF, COL_EST = COL_FIN+1, COL_FIN+2, COL_FIN+3

def celda(ws, f, c, valor=None, font=F_TXT, fill=None, fmt=None, alin=None, borde=True):
    cl = ws.cell(row=f, column=c)
    if valor is not None: cl.value = valor
    cl.font = font
    if fill: cl.fill = fill
    if fmt: cl.number_format = fmt
    if alin: cl.alignment = alin
    if borde: cl.border = CAJA
    return cl

def hoja_matriz(wb):
    ws = wb.create_sheet("Matriz")
    ws.sheet_view.showGridLines = False
    celda(ws, 1, 1, "Matriz de cobertura competencial", F_TIT, borde=False)
    celda(ws, 2, 1, "Cada competencia específica debe sumar 100 % a lo largo del curso.", F_NOTA, borde=False)
    celda(ws, 3, 1, "Escribe solo en las celdas amarillas. Las sumas y los avisos se calculan solos.", F_NOTA, borde=False)
    celda(ws, 4, 1, "El porcentaje de cobertura NO es el peso del proyecto en la nota.", Font(name="Arial", size=9, bold=True, italic=True, color="A8500F"), borde=False)

    celda(ws, FILA_CAB, 1, "Competencia específica", F_CAB, R_CAB, alin=Alignment(vertical="center"))
    for i in range(N_PROY):
        celda(ws, FILA_CAB, COL_INI+i, f"P{i+1}", F_CAB, R_CAB, alin=Alignment(horizontal="center"))
    celda(ws, FILA_CAB, COL_SUMA, "Suma", F_CAB, R_CAB, alin=Alignment(horizontal="center"))
    celda(ws, FILA_CAB, COL_DIF,  "Falta", F_CAB, R_CAB, alin=Alignment(horizontal="center"))
    celda(ws, FILA_CAB, COL_EST,  "Estado", F_CAB, R_CAB, alin=Alignment(horizontal="center"))

    for j in range(N_CE):
        f = FILA_INI + j
        celda(ws, f, 1, f"CE{j+1} · escribe aquí el enunciado", F_TXT, R_EDIT)
        for i in range(N_PROY):
            celda(ws, f, COL_INI+i, None, F_TXT, R_EDIT, fmt='0"%"', alin=Alignment(horizontal="center"))
        ini, fin = get_column_letter(COL_INI), get_column_letter(COL_FIN)
        celda(ws, f, COL_SUMA, f"=SUM({ini}{f}:{fin}{f})", F_TXT_B, R_SUAVE, fmt='0"%"', alin=Alignment(horizontal="center"))
        s = get_column_letter(COL_SUMA)
        celda(ws, f, COL_DIF, f"=100-{s}{f}", F_TXT, fmt='0"%"', alin=Alignment(horizontal="center"))
        celda(ws, f, COL_EST,
              f'=IF({s}{f}=0,"Huérfana: no se trabaja",'
              f'IF({s}{f}=100,"Completa",'
              f'IF({s}{f}<100,"Incompleta","Excede")))',
              F_TXT, alin=Alignment(horizontal="left"))

    f = FILA_FIN + 1
    celda(ws, f, 1, "Peso del proyecto (informativo)", F_TXT_B, R_SUAVE)
    for i in range(N_PROY):
        c = get_column_letter(COL_INI+i)
        celda(ws, f, COL_INI+i, f"=SUM({c}{FILA_INI}:{c}{FILA_FIN})", F_TXT_B, R_SUAVE,
              fmt='0"%"', alin=Alignment(horizontal="center"))
    s = get_column_letter(COL_SUMA)
    celda(ws, f, COL_SUMA, f"=SUM({s}{FILA_INI}:{s}{FILA_FIN})", F_TXT_B, R_SUAVE,
          fmt='0"%"', alin=Alignment(horizontal="center"))
    celda(ws, f, COL_EST, "Suma total de la matriz", F_NOTA)

    f2 = f + 2
    e = get_column_letter(COL_EST)
    celda(ws, f2, 1, "Competencias sin cuadrar", F_TXT_B, borde=False)
    celda(ws, f2, COL_INI, f'=COUNTIF({e}{FILA_INI}:{e}{FILA_FIN},"Incompleta")'
                           f'+COUNTIF({e}{FILA_INI}:{e}{FILA_FIN},"Excede")'
                           f'+COUNTIF({e}{FILA_INI}:{e}{FILA_FIN},"Huérfana: no se trabaja")',
          F_TXT_B, alin=Alignment(horizontal="center"))
    celda(ws, f2, COL_INI+1, "Debe ser 0 antes de dar por buena la programación", F_NOTA, borde=False)

    # Avisos de color en la columna Estado
    rango = f"{e}{FILA_INI}:{e}{FILA_FIN}"
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"Completa"'],
        fill=PatternFill("solid", fgColor="D6F0E2"), font=Font(name="Arial", size=10, color="1F6F4A")))
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"Incompleta"'],
        fill=PatternFill("solid", fgColor="FFF3CD"), font=Font(name="Arial", size=10, color="8A6100")))
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"Excede"'],
        fill=PatternFill("solid", fgColor="FBE0DC"), font=Font(name="Arial", size=10, color="9B2C1C")))
    ws.conditional_formatting.add(rango, CellIsRule(operator="equal", formula=['"Huérfana: no se trabaja"'],
        fill=PatternFill("solid", fgColor="FBE0DC"), font=Font(name="Arial", size=10, bold=True, color="9B2C1C")))

    ws.column_dimensions["A"].width = 46
    for i in range(N_PROY): ws.column_dimensions[get_column_letter(COL_INI+i)].width = 7
    ws.column_dimensions[get_column_letter(COL_SUMA)].width = 9
    ws.column_dimensions[get_column_letter(COL_DIF)].width = 8
    ws.column_dimensions[get_column_letter(COL_EST)].width = 26
    ws.freeze_panes = ws.cell(row=FILA_INI, column=COL_INI)
    return ws

def hoja_ejemplo(wb):
    ws = wb.create_sheet("Ejemplo")
    ws.sheet_view.showGridLines = False
    celda(ws, 1, 1, "Ejemplo ficticio · cómo se lee la matriz", F_TIT, borde=False)
    celda(ws, 2, 1, "Materia y proyectos inventados. Sirve para ver los cuatro estados posibles.", F_NOTA, borde=False)
    cab = ["Competencia", "P1 · Investigación", "P2 · Producto", "P3 · Difusión", "Suma", "Estado"]
    for i, x in enumerate(cab):
        celda(ws, 4, 1+i, x, F_CAB, R_CAB, alin=Alignment(horizontal="center"))
    datos = [("CE1 · Buscar y contrastar información", 50, 30, 20),
             ("CE2 · Elaborar un producto propio", 20, 60, 20),
             ("CE3 · Comunicar resultados", 40, 40, None),
             ("CE4 · Trabajar en equipo con criterio", None, None, None)]
    for j, (nombre, a, b, c) in enumerate(datos):
        f = 5 + j
        celda(ws, f, 1, nombre, F_TXT)
        for i, v in enumerate((a, b, c)):
            celda(ws, f, 2+i, v if v is not None else "—", F_TXT,
                  fmt='0"%"' if v is not None else None, alin=Alignment(horizontal="center"))
        celda(ws, f, 5, f"=SUM(B{f}:D{f})", F_TXT_B, R_SUAVE, fmt='0"%"', alin=Alignment(horizontal="center"))
        celda(ws, f, 6, f'=IF(E{f}=0,"Huérfana: no se trabaja",IF(E{f}=100,"Completa",IF(E{f}<100,"Incompleta","Excede")))', F_TXT)
    f = 9
    celda(ws, f, 1, "Peso del proyecto", F_TXT_B, R_SUAVE)
    for i in range(3):
        c = get_column_letter(2+i)
        celda(ws, f, 2+i, f"=SUM({c}5:{c}8)", F_TXT_B, R_SUAVE, fmt='0"%"', alin=Alignment(horizontal="center"))
    celda(ws, f, 5, "=SUM(E5:E8)", F_TXT_B, R_SUAVE, fmt='0"%"', alin=Alignment(horizontal="center"))
    celda(ws, 11, 1, "Qué se ve de un vistazo:", F_SUB, borde=False)
    for i, txt in enumerate([
        "CE3 se queda corta: falta un 20 % por repartir.",
        "CE4 es huérfana: no se trabaja en ningún proyecto del curso.",
        "El tercer proyecto está muy descargado frente a los otros dos.",
        "Son tres decisiones del docente, no un cálculo del sistema."]):
        celda(ws, 12+i, 1, "· " + txt, F_TXT, borde=False)
    ws.column_dimensions["A"].width = 42
    for c in "BCD": ws.column_dimensions[c].width = 18
    ws.column_dimensions["E"].width = 9
    ws.column_dimensions["F"].width = 26
    return ws

def hoja_diversidad(wb):
    ws = wb.create_sheet("Diversidad y accesibilidad")
    ws.sheet_view.showGridLines = False
    celda(ws, 1, 1, "Atención a la diversidad y accesibilidad, por proyecto", F_TIT, borde=False)
    celda(ws, 2, 1, "Se diseña por barreras, nunca por etiquetas ni diagnósticos.", F_NOTA, borde=False)
    celda(ws, 3, 1, "No escribas aquí nombres, diagnósticos ni datos de salud.",
          Font(name="Arial", size=9, bold=True, italic=True, color="A8500F"), borde=False)
    cab = ["Proyecto", "Barreras previsibles", "Acceso (representación)",
           "Participación", "Expresión", "Ampliación", "Formato alternativo", "Deriva a orientación"]
    for i, x in enumerate(cab):
        celda(ws, 5, 1+i, x, F_CAB, R_CAB, alin=Alignment(horizontal="center", wrap_text=True))
    for j in range(N_PROY):
        f = 6 + j
        celda(ws, f, 1, f"P{j+1}", F_TXT_B, R_SUAVE, alin=Alignment(horizontal="center"))
        for i in range(1, 8):
            celda(ws, f, 1+i, None, F_TXT, R_EDIT, alin=Alignment(vertical="top", wrap_text=True))
        ws.row_dimensions[f].height = 46
    f = 6 + N_PROY + 2
    celda(ws, f, 1, "Recordatorio", F_SUB, borde=False)
    for i, txt in enumerate([
        "Las medidas generales de diseño se proponen aquí y las decide el docente.",
        "Las medidas específicas (adaptaciones significativas, apoyos especializados) las determina",
        "el equipo de orientación con su procedimiento. Aquí solo se anota la derivación."]):
        celda(ws, f+1+i, 1, "· " + txt, F_TXT, borde=False)
    ws.column_dimensions["A"].width = 12
    for c in "BCDEFGH": ws.column_dimensions[c].width = 26
    return ws

def hoja_pesos(wb):
    """Suma 1: el peso de cada competencia especifica en el curso. Debe sumar 100 %."""
    ws = wb.create_sheet("Pesos por competencia")
    ws.sheet_view.showGridLines = False
    celda(ws, 1, 1, "Peso de cada competencia específica en el curso", F_TIT, borde=False)
    celda(ws, 2, 1, "Suma 1: todos los pesos juntos deben sumar 100 %.", F_NOTA, borde=False)
    celda(ws, 3, 1, "Es lo que hace que la programación esté completa.", F_NOTA, borde=False)
    celda(ws, 4, 1, "Ponderar la programación es una decisión del departamento. Calificar a una persona no se hace aquí.",
          Font(name="Arial", size=9, bold=True, italic=True, color="A8500F"), borde=False)

    cab = ["CE", "Enunciado (cópialo del currículo)", "Peso", "Criterios de evaluación", "Instrumento de evaluación"]
    anchos = [6, 52, 9, 24, 30]
    for i, x in enumerate(cab):
        celda(ws, 6, 1+i, x, F_CAB, R_CAB, alin=Alignment(horizontal="center", wrap_text=True))
    for j in range(N_CE):
        f = 7 + j
        celda(ws, f, 1, f"CE{j+1}", F_TXT_B, R_SUAVE, alin=Alignment(horizontal="center"))
        celda(ws, f, 2, None, F_TXT, R_EDIT)
        celda(ws, f, 3, None, F_TXT, R_EDIT, fmt='0"%"', alin=Alignment(horizontal="center"))
        celda(ws, f, 4, None, F_TXT, R_EDIT)
        celda(ws, f, 5, None, F_TXT, R_EDIT)
    f = 7 + N_CE
    celda(ws, f, 2, "TOTAL", F_TXT_B, R_SUAVE, alin=Alignment(horizontal="right"))
    celda(ws, f, 3, f"=SUM(C7:C{6+N_CE})", F_TXT_B, R_SUAVE, fmt='0"%"', alin=Alignment(horizontal="center"))
    celda(ws, f, 4, f'=IF(C{f}=100,"Correcto: la programación cuadra",'
                    f'IF(C{f}<100,"Falta "&(100-C{f})&"% por repartir",'
                    f'"Sobra "&(C{f}-100)&"%: algo está contado dos veces"))', F_TXT_B)
    ws.conditional_formatting.add(f"C{f}", CellIsRule(operator="equal", formula=["100"],
        fill=PatternFill("solid", fgColor="D6F0E2"), font=Font(name="Arial", size=10, bold=True, color="1F6F4A")))
    ws.conditional_formatting.add(f"C{f}", CellIsRule(operator="notEqual", formula=["100"],
        fill=PatternFill("solid", fgColor="FBE0DC"), font=Font(name="Arial", size=10, bold=True, color="9B2C1C")))
    celda(ws, f+2, 2, "Recuerda: este peso es de la programación, no la nota de nadie.", F_NOTA, borde=False)
    for i, a in enumerate(anchos):
        ws.column_dimensions[get_column_letter(1+i)].width = a
    return ws

def hoja_unidades(wb):
    """Resumen por unidad, con la estructura de una ficha de programacion."""
    ws = wb.create_sheet("Unidades")
    ws.sheet_view.showGridLines = False
    celda(ws, 1, 1, "Unidades de programación", F_TIT, borde=False)
    celda(ws, 2, 1, "Una fila por unidad. Los códigos, separados por comas.", F_NOTA, borde=False)
    celda(ws, 3, 1, "Coherencia: un criterio n.m exige que la competencia específica n esté en la columna de competencias.",
          Font(name="Arial", size=9, bold=True, italic=True, color="A8500F"), borde=False)
    cab = ["UD", "Título", "Trimestre", "Fechas", "Sesiones", "Competencias clave",
           "Competencias específicas", "Descriptores operativos", "Criterios de evaluación",
           "Saberes", "Instrumento", "ODS", "Diversidad prevista"]
    anchos = [6, 26, 10, 18, 9, 20, 20, 24, 24, 12, 22, 12, 30]
    for i, x in enumerate(cab):
        celda(ws, 5, 1+i, x, F_CAB, R_CAB, alin=Alignment(horizontal="center", wrap_text=True))
    for j in range(10):
        f = 6 + j
        celda(ws, f, 1, f"UD{j+1}", F_TXT_B, R_SUAVE, alin=Alignment(horizontal="center"))
        for i in range(1, len(cab)):
            celda(ws, f, 1+i, None, F_TXT, R_EDIT, alin=Alignment(vertical="top", wrap_text=True))
        ws.row_dimensions[f].height = 34
    f = 6 + 10 + 1
    celda(ws, f, 2, "Total de sesiones", F_TXT_B, R_SUAVE)
    celda(ws, f, 5, "=SUM(E6:E15)", F_TXT_B, R_SUAVE, alin=Alignment(horizontal="center"))
    celda(ws, f+2, 2, "Antes de dar la programación por buena, comprueba también:", F_SUB, borde=False)
    for i, txt in enumerate([
        "· que ninguna competencia específica se quede fuera de todas las unidades;",
        "· que cada criterio citado corresponda a una competencia declarada en esa misma unidad;",
        "· que cada descriptor operativo tenga marcada su competencia clave;",
        "· que todos los bloques de saberes aparezcan en algún momento del curso;",
        "· que cada unidad lleve su previsión de diversidad y accesibilidad."]):
        celda(ws, f+3+i, 2, txt, F_TXT, borde=False)
    for i, a in enumerate(anchos):
        ws.column_dimensions[get_column_letter(1+i)].width = a
    ws.freeze_panes = ws.cell(row=6, column=3)
    return ws

def hoja_instrucciones(wb):
    ws = wb.active; ws.title = "Cómo se usa"
    ws.sheet_view.showGridLines = False
    celda(ws, 1, 1, "Matriz de cobertura competencial", F_TIT, borde=False)
    celda(ws, 2, 1, "Sistema Aula y Comunidad Educativa Aumentada · plantilla 17", F_NOTA, borde=False)
    bloques = [
        ("Para qué sirve", [
            "Para comprobar que ninguna competencia específica se queda sin trabajar,",
            "y que ninguna ocupa el sitio de otra, cuando programas por proyectos."]),
        ("Las dos sumas, que no son lo mismo", [
            "SUMA 1 · hoja «Pesos por competencia»: cuánto pesa cada competencia específica en la",
            "materia. Todos los pesos juntos deben sumar 100 %. Es lo que hace que la programación",
            "esté completa.",
            "SUMA 2 · hoja «Matriz»: cómo se reparte cada competencia entre las unidades. Cada",
            "competencia debe llegar a su propio 100 %. Es lo que evita que una se quede sin trabajar."]),
        ("Qué se escribe y dónde", [
            "Solo en las celdas amarillas de la hoja «Matriz»:",
            "· en la columna A, el enunciado de cada competencia específica, copiado del currículo;",
            "· en las columnas P1 a P6, el porcentaje que aporta cada proyecto.",
            "Escribe el número sin el símbolo: 25, no 25%. La hoja ya lo muestra como porcentaje.",
            "Las columnas Suma, Falta y Estado se calculan solas: no las toques."]),
        ("Cómo se lee", [
            "Fila (por competencia): debe sumar 100 %. Es la comprobación que importa.",
            "Columna (por proyecto): es informativa. Dice si el curso está equilibrado.",
            "La celda «Competencias sin cuadrar» debe llegar a 0 antes de dar la programación por buena."]),
        ("Los cuatro estados", [
            "Completa: suma 100 %. Correcto.",
            "Incompleta: suma menos de 100 %. Falta cobertura.",
            "Excede: pasa del 100 %. Está ocupando espacio de otra competencia.",
            "Huérfana: suma 0 %. No se trabaja en ningún proyecto del curso."]),
        ("Dónde está la frontera", [
            "Ponderar la programación es una decisión de planificación del departamento, y esta",
            "hoja te ayuda a repartir y a comprobar que cuadra.",
            "Calificar a una persona es otra cosa: eso no se hace aquí ni con esta hoja.",
            "El sistema no calcula la nota de nadie, no aplica estos pesos a un trabajo concreto",
            "y no compara ni ordena alumnado."]),
        ("Las otras hojas", [
            "«Unidades»: una fila por unidad, con competencias, criterios, saberes, descriptores y ODS.",
            "«Ejemplo»: un caso ficticio con los cuatro estados, para ver cómo se lee la matriz.",
            "«Diversidad y accesibilidad»: qué barreras prevés en cada proyecto y qué medidas pones.",
            "Nunca escribas ahí nombres, diagnósticos ni datos de salud."]),
        ("Comprobaciones de coherencia", [
            "Un criterio de evaluación n.m exige que la competencia específica n esté declarada",
            "en esa misma unidad. Es el fallo más habitual y el más fácil de pasar por alto.",
            "Lo mismo con los descriptores operativos: si citas CD2, la competencia clave CD",
            "debe estar marcada en esa unidad."]),
    ]
    f = 4
    for titulo, lineas in bloques:
        celda(ws, f, 1, titulo, F_SUB, borde=False); f += 1
        for l in lineas:
            celda(ws, f, 1, l, F_TXT, borde=False); f += 1
        f += 1
    ws.column_dimensions["A"].width = 100
    return ws

def main():
    wb = Workbook()
    hoja_instrucciones(wb)
    hoja_pesos(wb)
    hoja_matriz(wb)
    hoja_unidades(wb)
    hoja_ejemplo(wb)
    hoja_diversidad(wb)
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    wb.save(DESTINO)
    print("Generado:", DESTINO)

if __name__ == "__main__":
    main()
