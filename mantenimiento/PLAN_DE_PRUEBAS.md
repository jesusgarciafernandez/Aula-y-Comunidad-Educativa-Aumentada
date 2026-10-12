# Plan de pruebas (vista de mantenimiento)

El plan operativo está en `tests/PLAN_DE_PRUEBAS.md`. Este documento explica **cuándo** se ejecuta cada
nivel y **quién** responde de él.

## Niveles

| Nivel | Qué comprueba | Automatizable | Cuándo se ejecuta |
|---|---|---|---|
| N1 · Validación estática | Estructura, frontmatter, versión, PII, rutas absolutas | Sí (`tests/validador_estructura.py`) | En cada build |
| N2 · Coherencia de referencias | Que agentes, workflows, skills y plantillas se citen entre sí correctamente | Sí (mismo validador) | En cada build |
| N3 · Batería común de conducta | C1–C10 en cada plataforma | No | Antes de cada release |
| N4 · Casos funcionales | F1–F12 | No | Antes de cada release |
| N5 · Pruebas negativas | N1–N7 | No | Antes de cada release **y** tras cualquier cambio en el §7 del núcleo |
| N6 · Puerta educativa | B1–B19 de A10 | No | En cada entrega al usuario final |

## Matriz de regresión

Cuando cambia… hay que repetir…

| Cambio | N1 | N2 | N3 | N4 | N5 | N6 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| Una plantilla | ✔ | ✔ | | | | ✔ |
| Un agente | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| El §7 del núcleo | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| El build de un adaptador | ✔ | ✔ | ✔ (esa plataforma) | ✔ | | ✔ |
| Una fuente externa | ✔ | | | | | ✔ |
| La guía Word | | | | | | ✔ |

## Criterio de release

- `1.0.0` requiere N1–N6 en `PASS` en las tres plataformas de escritorio, más el paquete genérico y el
  de mantenimiento.
- Si un nivel queda `BLOCKED`, la versión es `0.x.y-rcN` y el veredicto es `NO CERRADO`.
- Si el uso previsto está cubierto pero queda una limitación no crítica y declarada, el veredicto es
  `VERIFICADO CON LÍMITES`, y esa limitación se escribe en el registro de pruebas.
- Un `FAIL` se corrige en **la etapa causal** de la fuente canónica, no en el paquete, y obliga a
  repetir la regresión completa de esa fila.

## Estado actual (1.0.0)

N1 y N2 en `PASS` (automáticas, sobre extracción limpia de los cinco ZIP).
N3 y N4 confirmadas de forma **global** por el titular en ChatGPT Work, Claude Cowork y Antigravity el
2026-09-03: instalación y funcionamiento correctos. El registro ítem por ítem no está cumplimentado.
N5 sin registro individual. N6 aplicado sobre los entregables.

Veredicto: **VERIFICADO CON LÍMITES**. El límite está declarado en `tests/REGISTRO_DE_PRUEBAS.md` §3,
junto con lo que haría falta para pasar a `VERIFICADO`.
