> Workflow del sistema **Aula y Comunidad Educativa Aumentada**. Subordinado a `instruccion_maestra.md`.

# W27 · Conectar el contexto de archivos en Claude Cowork

**Disparador:** «Cowork no lee el proyecto», «¿por qué no ve los archivos?», instalación o actualización
del plugin, o cualquier tarea que dependa de documentación local en Claude Cowork.

## Qué resuelve

Claude Cowork mantiene separadas la instalación de un plugin y la autorización de una carpeta para una
sesión. El plugin aporta método, skills y agentes; la carpeta de contexto aporta los archivos que se
pueden leer. No hay una instrucción del plugin que pueda conceder ese permiso automáticamente.

## Fases

1. **Estado real (A21).** Comprobar si el panel **Contexto** de la sesión muestra una carpeta. No
   confundir la lista de skills instaladas con archivos leídos.
2. **Preparar carpeta.** Extraer el ZIP en una carpeta estable. Para el conocimiento del sistema,
   elegir la raíz extraída del plugin Claude Cowork, no el ZIP y no una subcarpeta aislada.
3. **Autorizar.** En el compositor o en el panel de actividad, pulsar `Agregar carpeta`, seleccionar
   la raíz y aceptar el aviso de acceso. No marcar el permiso para futuras sesiones salvo que la
   política del centro lo haya aprobado.
4. **Separar contextos.** Añadir los documentos propios del centro desde otra carpeta autorizada. No
   mezclar documentación real con `demo/`, pruebas ni el paquete de distribución.
5. **Comprobación mínima.** Leer `VERSION`, `.claude-plugin/plugin.json`, `CLAUDE.md` y el índice o
   workflow que corresponda. Si alguno no se puede leer, marcarlo `No consta`.
6. **Tarea.** Ejecutar el workflow solicitado, declarando al inicio qué contexto se ha usado.
7. **Auditoría (A10).** Comprobar rutas, privacidad, adaptación al usuario, comprensión y trazabilidad.

## Si la persona no autoriza la carpeta

Se puede continuar con las instrucciones de la skill activa, pero la respuesta debe decir:
«Contexto local no conectado: no puedo afirmar que haya leído los archivos del proyecto». Las fuentes
locales y las afirmaciones dependientes del centro quedan en `No consta`; no se fabrican citas.

## Salida

Estado del contexto · carpeta autorizada · archivos realmente leídos · limitaciones · acción siguiente ·
trazabilidad.

## Puertas humanas

La persona responsable decide si conecta la carpeta y si los archivos pueden salir del dispositivo. El
centro decide qué documentación incorpora, con qué datos y durante cuánto tiempo.

## Criterios de terminado

La sesión muestra la carpeta en **Contexto**, Claude confirma mediante lectura real al menos los tres
archivos de comprobación, las rutas citadas existen y cualquier documento no disponible aparece como
`No consta`.
