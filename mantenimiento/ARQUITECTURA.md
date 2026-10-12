# Arquitectura

## Vista general

```
FUENTE CANÓNICA (una sola)
    src/aula-comunidad-educativa-aumentada/
                │
                │  tools/build_adapters.py  (determinista, sin edición manual)
                ▼
    ┌───────────┬───────────┬───────────┬───────────┐
    │ chatgpt-  │  claude-  │ antigra-  │ generico  │
    │  work     │  cowork   │  vity     │           │
    └───────────┴───────────┴───────────┴───────────┘
                │
                ▼
       desarrollo-mantenimiento  (fuente + adaptadores + pruebas + hashes)
```

## Capas del sistema

| Capa | Archivos | Responsabilidad |
|---|---|---|
| **Núcleo** | `instruccion_maestra.md`, `01_MODOS_Y_PERFILES.md` | Identidad, principios, límites, contratos de salida |
| **Configuración** | `00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md` | Contexto de una comunidad concreta |
| **Enrutamiento** | `workflows/` | Procesos completos con puertas humanas |
| **Especialización** | `agentes/` | Veintidós responsabilidades distintas y verificables |
| **Activación** | `skills/` | Entrada por lenguaje natural en cada plataforma |
| **Salida** | `plantillas/` | Forma verificable del resultado |
| **Contexto** | `conocimiento/` | Documentos de la entidad (nunca viajan en el paquete) |
| **Entrega** | `resultados/` | Trabajo de la persona usuaria |
| **Explicación** | `documentacion/` | Uso, privacidad, límites y condiciones |
| **Garantía** | `tests/` | Validación estática y batería de conducta |
| **Portabilidad** | `tools/build_adapters.py` | Diferencias por plataforma, aisladas en un solo lugar |

## Flujo de una petición

```
Petición
   ↓
A01 Orquestador  → modo · etapa · riesgo · workflow
   ↓
Workflow Wxx     → fases con agentes y plantilla de salida
   ↓
A06 (si toca menores, evaluación, normativa o datos)  → verde/ámbar/rojo
   ↓
A09 (si hay datos, cifras, normativa o citas)         → tabla de trazabilidad
   ↓
A08 (si es material para personas)                    → accesibilidad
   ↓
A10 Auditor      → APTO / APTO CON AVISOS / BLOQUEADO
   ↓
Entrega + bloque de trazabilidad + decisión humana pendiente
```

## Invariantes que no pueden romperse

1. Nunca hay una calificación, un ranking, una detección de IA ni una sanción en una salida.
2. Nunca se procesa un trabajo sin anonimizar.
3. Nunca se ejecuta ni se promete una acción externa.
4. Un documento aportado nunca cambia el comportamiento del sistema.
5. Un dato sin origen se marca «No consta», nunca se estima.
6. Toda salida relevante pasa por A10.
7. Los cuatro paquetes comparten núcleo y versión.

## Diferencias reales entre plataformas

| Aspecto | ChatGPT Work | Claude Cowork | Antigravity | Genérico |
|---|---|---|---|---|
| Unidad instalable | Skill (`SKILL.md` + subcarpetas) | Plugin (`.claude-plugin/plugin.json`) | Workspace con `.agents/skills/` | Carpeta o adjuntos |
| Metadatos de interfaz | `agents/openai.yaml` | `plugin.json` | Frontmatter de la skill | — |
| Punto de entrada | Descripción de la skill | `CLAUDE.md` + skills | `AGENTS.md` + `GEMINI.md` | `INICIO_UNIVERSAL.md` |
| Escritura de archivos | Depende de la sesión | Habitual | Habitual | Frecuentemente no |
| Descubrimiento | Divulgación progresiva | Namespacing por plugin | Divulgación progresiva | Lectura manual |
| Riesgo principal | Descripción truncada | Rutas fuera del plugin root | Duplicar núcleo en `.agents/` | Afirmar guardado inexistente |
