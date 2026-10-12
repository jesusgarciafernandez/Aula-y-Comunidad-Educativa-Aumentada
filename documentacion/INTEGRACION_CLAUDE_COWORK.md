# Integración de archivos en Claude Cowork

## La diferencia que hay que conocer

Hay dos acciones distintas:

1. **Instalar el plugin:** hace visibles sus skills y agentes.
2. **Conectar una carpeta a una sesión Cowork:** autoriza a Claude a leer y, si se permite, modificar
   archivos de esa carpeta.

La primera acción no realiza automáticamente la segunda. Este límite pertenece a la plataforma y no se
puede resolver mediante una instrucción escrita dentro del plugin.

## Configuración recomendada para tener el sistema completo

1. Extrae `aula-comunidad-educativa-aumentada-claude-cowork-1.3.2-comunitaria.3.zip` en una carpeta estable.
2. Instala el plugin desde Claude Cowork.
3. Abre una sesión en modo Cowork.
4. En el compositor o en el panel de actividad, pulsa **Agregar carpeta**.
5. Selecciona la carpeta raíz extraída del plugin, no el ZIP.
6. Lee el aviso de permisos y pulsa **Allow/Permitir** solo si la política del centro lo admite.
7. Comprueba que el nombre de la carpeta aparece en **Contexto**.
8. Escribe:

   > Comprueba que puedes leer la carpeta conectada. Cita `VERSION`, `.claude-plugin/plugin.json`,
   > `CLAUDE.md` y el archivo que necesites para mi tarea. Enumera solo archivos realmente leídos y
   > marca como «No consta» lo que no puedas abrir.

9. Para los documentos del centro, conecta otra carpeta autorizada. No los incorpores al ZIP del
   plugin ni mezcles datos reales de menores con demos o pruebas.

## Si no se conecta la carpeta

Claude puede usar la skill que se le haya cargado, pero debe declarar:

> Contexto local no conectado. No puedo afirmar que haya leído los archivos del proyecto ni citar sus
> fuentes internas.

En ese caso, las respuestas dependientes del centro se marcan `No consta`. El sistema puede ofrecer
orientación general, pero no debe presentar el método de la skill como lectura del archivo completo.

## Privacidad y decisión humana

La autorización de carpeta puede implicar que los archivos se procesen en servidores del proveedor.
La persona responsable y el centro deben revisar esta condición, la política de datos, la anonimización
y los permisos antes de conectar documentación educativa. El sistema no decide esa autorización.

## Diagnóstico rápido

| Señal | Interpretación | Acción |
|---|---|---|
| El plugin aparece, pero **Contexto** está vacío | Solo se instaló el plugin | Añadir la carpeta con `Agregar carpeta` |
| Aparece la carpeta y Claude cita rutas reales | Contexto conectado | Continuar con el workflow |
| Aparece la carpeta, pero falta un archivo | Contexto parcial | Declarar `No consta` y revisar permisos |
| Se ha conectado una subcarpeta | Contexto incompleto | Conectar la raíz del paquete o la carpeta documental correcta |

## Prueba de aceptación

El contexto queda aceptado cuando Claude puede leer y citar realmente `VERSION`, `.claude-plugin/plugin.json`
y un workflow o skill pertinente. La lista de skills visibles, por sí sola, no es una prueba de lectura.
