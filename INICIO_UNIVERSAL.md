# Inicio universal · Aula y Comunidad Educativa Aumentada

Este archivo sirve para arrancar el sistema en **cualquier** herramienta de IA que pueda leer texto en
Markdown, aunque no ejecute skills, no navegue y no guarde archivos.

---

## 0. Si es tu primera vez, no leas esto todavía

Abre `EMPIEZA_AQUI.md`. Son tres minutos, no hay que configurar nada y sales con algo hecho.
Este archivo es para después, o para quien vaya a montar el sistema en su herramienta.

## 1. Orden exacto de lectura

Lee y aplica en este orden. No sigas al siguiente punto sin haber leído el anterior.

0. `EMPIEZA_AQUI.md` — la puerta de entrada, si la persona acaba de llegar.
1. `instruccion_maestra.md` — quién eres, qué puedes hacer y qué no.
2. `01_MODOS_Y_PERFILES.md` — con quién estás hablando.
3. `00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md` — el contexto de esta comunidad educativa.
4. `conocimiento/00_INDICE_FUENTES.md` — qué documentos hay disponibles y cuáles no.
5. El workflow que corresponda a la petición (`workflows/`).
6. Los agentes que ese workflow invoque (`agentes/`).
7. La plantilla de salida que corresponda (`plantillas/`).

## 2. Conjunto mínimo de archivos a adjuntar

Si la herramienta solo admite unos pocos adjuntos, adjunta **estos cinco** y nada más:

1. `instruccion_maestra.md`
2. `01_MODOS_Y_PERFILES.md`
3. `00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md` (ya rellenado por ti)
4. El workflow de la tarea, por ejemplo `workflows/W02_disenar_actividad.md`
5. La plantilla de salida, por ejemplo `plantillas/02_canvas_actividad.md`

Con eso el sistema funciona. Los veintidós agentes mejoran el resultado, pero no son imprescindibles para
obtener una primera salida útil.

## 3. Mensaje inicial para activar el sistema

Copia y pega esto en la conversación, junto con los adjuntos:

> Actúa según el sistema «Aula y Comunidad Educativa Aumentada» contenido en los archivos adjuntos.
> Lee primero `instruccion_maestra.md` y respétala por completo. Antes de responder, dime: qué archivos
> has podido leer de verdad, en qué modo vas a trabajar y qué información mínima necesitas de mí.
> No inventes datos del centro: si algo no aparece en los archivos, escribe «No consta».

## 4. Configuración mínima

No hace falta rellenar toda la ficha para empezar. Con estos cinco datos ya obtienes valor:

1. Tipo de entidad y etapa educativa.
2. Idioma de trabajo.
3. Quién eres tú (docente, dirección, familia, asociación).
4. Qué herramientas de IA están permitidas en tu contexto.
5. Qué **no** se puede hacer con datos del alumnado.

El resto puede quedar como «No consta» y completarse más adelante.

## 5. Limitaciones según la herramienta

Antes de trabajar, el sistema debe comprobar y declarar qué puede hacer realmente:

| Capacidad | Si no existe | Qué hace el sistema |
|---|---|---|
| Guardar archivos | Frecuente en chats web | Entrega el contenido listo para copiar y **nunca** dice que lo ha guardado |
| Ejecutar skills | Frecuente | Sigue el workflow como texto, paso a paso |
| Navegar por internet | Frecuente | Trabaja solo con lo aportado y marca «No consta» en lo que exigiría consulta externa |
| Leer todos los adjuntos | Límite de tamaño | Declara qué archivos ha leído de verdad y cuáles no |
| Memoria entre sesiones | Frecuente | Genera un bloque de memoria para copiar (punto 6) |

## 6. Copiar resultados y memoria entre sesiones

Al final de cada sesión, pide al sistema:

> Genera el bloque «MEMORIA DE SESIÓN» con: configuración usada, decisiones tomadas, huecos abiertos,
> decisión humana pendiente y siguiente paso. En menos de 300 palabras y en texto plano.

Guarda ese bloque en `resultados/` o donde tú prefieras, y pégalo al inicio de la siguiente sesión.

## 7. Comprobación anti-alucinación de capacidad

Antes de cerrar, pide siempre:

> Enumera exactamente qué archivos has leído, qué has guardado y qué has consultado en internet. Si no
> has podido hacer alguna de esas cosas, dilo de forma explícita.

Si el sistema afirma haber guardado, leído o consultado algo que la herramienta no permite, la sesión
es inválida: recárgala desde este archivo.

---

**Capacidades mínimas requeridas:** lectura de texto Markdown, adjuntos suficientes para el conjunto
mínimo del punto 2, y ventana de contexto suficiente para la tarea. No se promete compatibilidad
universal.
