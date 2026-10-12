# Matriz de dependencias

## Mapa fuente → adaptador

| Archivo de la fuente canónica | ChatGPT Work | Claude Cowork | Antigravity | Genérico |
|---|---|---|---|---|
| `instruccion_maestra.md` | `references/` | raíz | raíz | raíz |
| `01_MODOS_Y_PERFILES.md` | `references/` | raíz | raíz | raíz |
| `00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md` | `references/` | raíz | raíz | raíz |
| `INICIO_UNIVERSAL.md` | `references/` | raíz | raíz | raíz |
| `agentes/` | `references/agentes/` | `agentes/` + `agents/` **transformados** (nombre con guiones + frontmatter, sin `_LEEME`) | `agentes/` | `agentes/` |
| `workflows/` | `references/workflows/` | `workflows/` | `workflows/` | `workflows/` |
| `skills/` | `SKILL.md` principal + `references/skills/` | `skills/` | `.agents/skills/` | `skills/` |
| `plantillas/` (incluye el `.xlsx` de la matriz) | `assets/plantillas/` | `plantillas/` | `plantillas/` | `plantillas/` |
| `conocimiento/` | `references/conocimiento/` | `conocimiento/` | `conocimiento/` | `conocimiento/` |
| `documentacion/` | `references/documentacion/` | `documentacion/` | `documentacion/` | `documentacion/` |
| `resultados/` | — (según capacidad) | `resultados/` | `resultados/` | `resultados/` |
| `demo/` | excluido | excluido | excluido | **incluido** |
| `tests/`, `tools/`, `mantenimiento/` | excluidos | excluidos | excluidos | excluidos |
| `AGENTS.md` | — | — | raíz | raíz |
| `CLAUDE.md` | — | raíz | — | raíz |
| `GEMINI.md` | — | — | raíz | raíz |
| — (generado) | `agents/openai.yaml` | `.claude-plugin/plugin.json` | — | — |

## Referencias cruzadas internas

| Origen | Depende de | Si cambias el origen, revisa |
|---|---|---|
| `instruccion_maestra.md` §4 | Nombres de archivo de `workflows/` | Tabla de enrutamiento |
| Cada workflow | Agentes citados y plantilla de salida | Nombres de archivo exactos |
| Cada skill | Workflow y agentes que ejecuta | Rutas dentro del `SKILL.md` |
| `skills/_LEEME.md` | Las treinta y una skills | Tabla de derivaciones |
| `agentes/_LEEME.md` | Los veintidós agentes | Tabla de bloqueo |
| `plantillas/_LEEME.md` | Las cincuenta y ocho plantillas | Numeración y tabla |
| `tests/PLAN_DE_PRUEBAS.md` | A10 (B1–B19) y §7 del núcleo | Pruebas negativas |
| `documentacion/FUENTE_GUIA_INTEGRAL_TUTORIA.md` | Trazabilidad de requisitos tutoriales | Revisar al añadir o cambiar capacidades |
| `documentacion/MARCO_LEGAL_FAMILIAS_Y_TUTORIA.md` | A17–A22, W20–W32 y RN-17–RN-36 | Revisar en cada cambio normativo o territorial |
| `documentacion/FUENTES_AUTONOMICAS_EDUCACION_FAMILIAS_TUTORIA.md` | A20, W26, RN-36 y plantilla 53 | Revisar trimestralmente y ante cambios territoriales |
| `documentacion/GUIA_MAESTRA_DE_USO.md` | Núcleo, A17–A22, W20–W32 y matriz de trazabilidad | Revisar cuando cambie una ruta, salvaguarda o fecha de corte |
| `documentacion/MATRIZ_TRAZABILIDAD_SISTEMA.md` | Todos los agentes, workflows, skills y plantillas; pruebas F18–F20 | Revisar con cada cambio funcional |
| `demo/README_DEMOSTRACIONES.md` y `demo/caso_*.md` | Guía Maestra y pruebas F20/F22–F26 | Mantener datos ficticios y revisar con cada evolución |

## Dependencias externas

| Dependencia | Uso | Riesgo si cambia | Dónde se ajusta |
|---|---|---|---|
| Formato de skill de ChatGPT | Adaptador 1 | El paquete deja de descubrirse | `tools/build_adapters.py` |
| Formato de plugin de Claude | Adaptador 2 | El plugin no carga | `tools/build_adapters.py` |
| Ruta `.agents/skills` de Antigravity | Adaptador 3 | Las skills no se detectan | `tools/build_adapters.py` |
| Fuentes educativas y normativas | Contenido | Afirmaciones desactualizadas | `conocimiento/00_INDICE_FUENTES.md` |
| Python 3 estándar | Build y validador | — | Sin dependencias externas |
| `openpyxl` | Solo para regenerar `17_...xlsx` con `tools/gen_matriz_cobertura.py` | El `.xlsx` ya generado viaja en el paquete | `tools/gen_matriz_cobertura.py` |

**El build de adaptadores y el validador no requieren bibliotecas externas.** El generador opcional
de la matriz necesita `openpyxl` y LibreOffice para recalcular el `.xlsx`.
