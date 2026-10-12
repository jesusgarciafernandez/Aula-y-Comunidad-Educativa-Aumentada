# Guion de pruebas de plataforma

Para ejecutar por una persona con acceso a cada plataforma. Tiempo estimado: 40 minutos por plataforma.

## Antes de empezar

1. Descarga el ZIP correspondiente y **extráelo en una carpeta nueva y vacía**. No reutilices una
   instalación anterior.
2. Anota el SHA-256 del ZIP (está en `SHA256SUMS.txt`) y compruébalo:
   - macOS / Linux: `shasum -a 256 <archivo>.zip`
   - Windows: `certutil -hashfile <archivo>.zip SHA256`
3. Anota la versión visible de la plataforma y la fecha.

## Instalación

**ChatGPT Work.** Coloca la carpeta de la skill en el lugar que use tu instalación para skills
(`.agents/skills/` del directorio de trabajo o `$HOME/.agents/skills`), o súbela por el mecanismo de
skills de tu cuenta. Anota **el nombre exacto del menú** que hayas usado: la guía debe reflejarlo.

**Claude Cowork.** Instala el plugin desde el directorio extraído o desde el propio ZIP. En Claude Code
el equivalente documentado es `claude --plugin-dir <ruta>` (acepta también el `.zip`) y
`claude plugin validate <ruta>`. Anota qué artefacto instalaste realmente y por qué menú.

**Antigravity.** Abre la carpeta extraída como workspace. Comprueba que se detectan `AGENTS.md` y
`.agents/skills/`.

**Genérico.** Adjunta los cinco archivos del conjunto mínimo de `INICIO_UNIVERSAL.md` y pega el mensaje
de activación.

## Ejecución

Ejecuta, en este orden y anotando la salida literal: C1 → C10, después F1 → F6, después N1 → N7.
Los prompts exactos están en `tests/PLAN_DE_PRUEBAS.md`.

## Registro

Para cada prueba, escribe en `tests/REGISTRO_DE_PRUEBAS.md`:

```
Plataforma: ...
Versión visible de la plataforma: ...
Fecha: ...
ZIP: ... · SHA-256: ...
Prueba: C1
Prompt exacto: ...
Salida observada (resumen literal): ...
Estado: PASS | FAIL | BLOCKED
```

## Qué hacer ante un FAIL

No parchees el adaptador. Corrige **la etapa causal** en la fuente canónica, reconstruye los paquetes
con `tools/build_adapters.py`, recalcula los hashes y repite la batería completa (regresión), no solo
la prueba fallida.
