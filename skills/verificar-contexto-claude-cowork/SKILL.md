---
name: verificar-contexto-claude-cowork
description: Comprueba y conecta el acceso real a archivos del sistema en Claude Cowork antes de citarlos.
---

# Verificar contexto en Claude Cowork

Activa `workflows/W27_conectar_contexto_claude_cowork.md` con A21, A06 y A10.

## Regla esencial

Instalar el plugin no significa que Cowork tenga acceso a sus archivos. Primero comprueba si la sesión
muestra una carpeta en el panel **Contexto**. Si no aparece, di `Contexto local no conectado` y no
afirmes que has leído `CLAUDE.md`, `VERSION`, el índice de fuentes ni ningún documento del centro.

## Acción guiada

Explica a la persona, en lenguaje sencillo, que debe extraer el ZIP, pulsar `Agregar carpeta`, elegir
la carpeta raíz extraída y autorizarla para la sesión. Avisa de que el contenido puede procesarse en
servidores del proveedor. Para documentos del centro, usa una carpeta independiente, anonimizada y
autorizada de forma expresa.

## Comprobación

Con la carpeta visible, lee realmente `VERSION`, `.claude-plugin/plugin.json`, `CLAUDE.md` y el
workflow o plantilla necesarios. Cita solo esos archivos. Si no se puede leer algo, escribe `No consta`.

## Salida

Estado del contexto · archivos comprobados · limitaciones · siguiente acción · trazabilidad. Después
continúa con la tarea educativa solicitada y adapta la explicación al rol, conocimientos previos,
tiempo, idioma y necesidades de acceso de la persona.
