---
name: auditar-material-educativo-con-ia
description: Audita un material educativo ya elaborado: alineación, evidencia, feedback, accesibilidad, datos y trazabilidad.
---

# Auditar un material educativo hecho con IA

Ejecuta la puerta de `agentes/A10_auditor_calidad_educativa.md` sobre un material existente.

## Cuándo se usa
«Revisa este material que he hecho con ChatGPT», «¿esto está bien planteado?», «¿puedo usar esto con
mi grupo?», antes de compartir un material con el claustro o con familias.

## Cuándo NO se usa
- Para revisar el trabajo de un alumno → `revisar-trabajo-con-feedback`.
- Para crear el material desde cero → `disenar-actividad-aprendizaje`.

## Entradas
El material completo y, si consta, para quién es y con qué objetivo.

## Pasos
1. **Alineación:** ¿hay resultado de aprendizaje y evidencia? ¿El material sirve para eso?
2. **Práctica:** ¿el alumnado hace algo o solo recibe contenido?
3. **Feedback:** ¿hay criterios visibles antes de producir?
4. **Accesibilidad:** ¿lo esencial llega por más de una vía? (A08)
5. **Datos:** ¿aparece algún dato personal evitable? (A06)
6. **Trazabilidad:** ¿hay cifras, normativa o citas sin origen comprobable? (A09)
7. **Riesgos:** ¿hay evaluación, perfilado, vigilancia o acción externa encubierta?
8. **Rigor:** errores conceptuales, simplificaciones falsas, afirmaciones sin matiz.

## Contrato de salida
```
Veredicto: APTO | APTO CON AVISOS | BLOQUEADO
Bloqueos activados: B1..B9
Correcciones concretas propuestas: ...
Qué debe revisar una persona antes de usarlo: ...
```

## Límite
La auditoría no reescribe el material entero por su cuenta: señala, propone y devuelve la decisión.
