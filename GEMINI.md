# GEMINI.md

Instrucciones para Gemini y Google Antigravity al trabajar dentro del sistema
**Aula y Comunidad Educativa Aumentada** `1.3.2`.

## Punto de entrada

Este archivo complementa a `AGENTS.md`, que es el punto de entrada principal del workspace. Si ambos
están disponibles, aplica primero `instruccion_maestra.md`, después `AGENTS.md` y después este archivo.

## Orden de lectura

1. `instruccion_maestra.md`
2. `01_MODOS_Y_PERFILES.md`
3. `00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md`
4. `conocimiento/00_INDICE_FUENTES.md`
5. Workflow correspondiente + agentes invocados + plantilla de salida.

## Skills

Las skills nativas están en `.agents/skills/`. Cada una declara en su `description` cuándo debe
activarse y cuándo no. La activación por lenguaje natural es el modo previsto de uso.

## Reglas específicas de este entorno

- Declara al arrancar qué archivos has leído y qué puedes hacer realmente en esta sesión.
- Escribe los resultados en `resultados/` con la convención `AAAA-MM-DD_tipo_asunto_vN`.
- No dependas de ninguna ruta del workspace de desarrollo original. Todo el paquete es autocontenido.
- No ejecutes acciones externas ni navegación no solicitada.

## Límites que no se negocian

Sin notas, sin ranking, sin detección de uso de IA, sin sanciones, sin diagnósticos, sin decisiones de
acceso o promoción, sin datos reales de menores, y sin inferir emociones. Ver `instruccion_maestra.md` §7.

**Normativa:** nunca afirmes Derecho. Cita con enlace y fecha desde
`documentacion/REFERENCIAS_NORMATIVAS.md` y di a quién corresponde validar cada implicación (§7.7).

En modo familia, el centro verifica representación y acceso. Usa W20–W32 y
`documentacion/MARCO_LEGAL_FAMILIAS_Y_TUTORIA.md`; no interpretes resoluciones ni compartas datos de terceros.

Para respuestas autonómicas, consulta el directorio de fuentes, activa A20 y entrega solo una
**Sugerencia operativa a revisar y contrastar**, con fuente, fecha, vigencia o `No consta` y validación humana.

Si la plataforma es Claude Cowork, la instalación del plugin no concede acceso a sus archivos. Comprueba
`Contexto`; si no hay carpeta conectada, declara `Contexto local no conectado` y usa W27/A21. Las técnicas
se adaptan al rol, conocimientos previos, tiempo, barrera y acceso de la persona, con comprobación de
comprensión y ajuste posterior.
