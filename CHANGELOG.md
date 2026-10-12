# Changelog

## [1.3.2-comunitaria.3] · 2026-10-09

**Adaptador ChatGPT Work autocontenido y verificable.**

- Se simplifica el inicio para el flujo recomendado: proyecto local, carpeta asociada, conversación
  nueva y petición en lenguaje natural.
- Se explicita que los pesos y porcentajes sin currículo o decisión del centro son ejemplos o propuestas
  provisionales, nunca decisiones curriculares oficiales.
- Se incorpora al registro la última evidencia conversacional: C01 **PASS** y C03 **PASS CON LÍMITE**.
- El adaptador ChatGPT Work incorpora en su raíz `tests/`, `demo/`, `mantenimiento/`, `LICENSE.md`,
  `VERSION`, `CHANGELOG.md` y un README específico de la entrega.
- Se añade un validador estático ejecutable sobre la extracción limpia del adaptador, con fixtures
  ficticios y documentación de pruebas.
- La instalación documenta el uso local y diferencia lectura de archivos, descubrimiento de skill y
  ejecución runtime realmente observada.
- La skill aplica los criterios de A10 cuando el agente runtime no está disponible, sin afirmar una
  ejecución que no pueda demostrarse.
- Se actualiza el constructor de adaptadores; la versión `1.3.2-comunitaria.1` queda preservada.

## [1.3.2] · 2026-09-04

**Carril de inicio de curso para centro, alumnado, docentes y familias.**

- Se incorpora A22, la skill `inicio-curso-comunidad-educativa` y W28–W32.
- Se añaden cinco plantillas para plan de centro, primer día, primera reunión docente-familia,
  reunión general del instituto y apoyo familiar inicial.
- La Guía Maestra y la matriz conectan los cinco hitos con responsables, accesibilidad, comprensión,
  ajuste, privacidad y aprobación humana.
- Se añade una demostración sintética de inicio de curso; las orientaciones siguen siendo sugerencias
  a revisar y contrastar por el centro.

## [1.3.1] · 2026-09-04

**Corrección de contexto en Claude Cowork y adaptación efectiva al usuario.**

- Se documenta y operacionaliza la diferencia entre plugin instalado y carpeta autorizada en una sesión
  Cowork; se incorporan A21, W27 y `verificar-contexto-claude-cowork`.
- Las skills del adaptador Cowork llevan una salvaguarda de contexto para no presentar skills visibles
  como archivos leídos y para declarar `Contexto local no conectado` cuando corresponda.
- Se añade una guía de conexión con `Agregar carpeta`, autorización, separación de documentación del
  centro y comprobación de `VERSION`, manifiesto y workflow.
- Las recomendaciones dejan de enumerar técnicas sin contexto: seleccionan una o dos, justifican su
  encaje, proponen una prueba corta, comprueban comprensión y definen cómo ajustar o retirar la medida.
- Se actualiza la matriz de trazabilidad y se añaden F21/N21 al plan de pruebas.

## [1.3.0] · 2026-09-03

**Capa autonómica contrastable para familias y tutoría.** Se incorporan:

- Directorio oficial de las diecisiete comunidades autónomas y del ámbito de gestión ministerial de
  Ceuta y Melilla, con boletín, portal educativo y referencias curriculares de partida.
- Agente A20, workflow W26, skill `contrastar-normativa-autonomica-educativa` y plantilla 53.
- Referencia RN-36 y conexión con el marco legal familiar, configuración, índice de fuentes y W20/W25.
- Control explícito de modificaciones y sustituciones detectadas, entre ellas Illes Balears 2025, La
  Rioja 2025 y Comunidad de Madrid 2024.
- Bloqueo B19: ninguna aplicación autonómica sin territorio, fuente oficial, fecha, control de vigencia,
  protocolo o hueco explícito, validación humana y etiqueta de sugerencia.
- **Guía Maestra** en Markdown y DOCX, con índice, rutas, carril familiar/autonómico, contrato de salida,
  privacidad, prompts y ciclo de revisión.
- **Matriz de trazabilidad** de 38 requisitos, capacidades y salvaguardas conectados con agentes, workflows,
  skills, plantillas, demostraciones y pruebas.
- **Tres demostraciones sintéticas** para familia–autonomía, entrevista familia–tutor y contraste autonómico,
  con checklist de revisión humana.

Todas las consecuencias territoriales se expresan como **Sugerencia operativa a revisar y contrastar**.
El directorio facilita la verificación; no certifica vigencia, legalidad ni cumplimiento.

## [1.2.0] · 2026-09-03

**Evolución para familias, representantes legales y tutores docentes.** Se incorporan:

- Tres agentes A17–A19: acompañamiento familiar del aprendizaje, coordinación familia–tutor y mediación
  digital/orientación familiar.
- Seis workflows W20–W25 y seis skills para incorporación, entrevistas, apoyo en el hogar, participación
  accesible, acuerdos digitales e IA, y decisiones de orientación o transición.
- Diez plantillas 43–52, incluida verificación de representación, acuerdos, aprendizaje en el hogar,
  accesibilidad, mediación digital y triaje de preocupaciones.
- `documentacion/MARCO_LEGAL_FAMILIAS_Y_TUTORIA.md`, con normativa estatal y europea, fuentes oficiales,
  fecha de consulta, implicación funcional, responsables de validación y lista territorial obligatoria.
- Referencias RN-17–RN-35 y actualización de RN-06 con su enlace oficial.
- Salvaguardas para progenitores separados, alumnado mayor de edad, voz del menor, datos de terceros y la
  excepción de no avisar automáticamente a la familia cuando puede ser origen de la violencia.

La versión mantiene autoridad humana: no autentica representación, no concede acceso a expedientes, no
interpreta resoluciones, no diagnostica, no decide itinerarios y no envía comunicaciones.

## [1.1.0] · 2026-09-03

**Evolución tutorial para Educación Secundaria**, derivada de la guía integral aportada por la
persona usuaria. Se incorporan:

- Seis agentes nuevos (A11–A16) para tutoría, protección, juntas/absentismo, convivencia/sociograma,
  ciberconvivencia y transición/acogida.
- Ocho skills nuevas y ocho workflows W12–W19 con preguntas de contexto, tiempos, protocolos y
  puertas humanas.
- Veintidós plantillas tutoriales para NEAE/DUA, crisis, reuniones, absentismo, convivencia,
  ciberconvivencia, acogida, entrevistas y autocuidado.
- Matriz de trazabilidad en `documentacion/FUENTE_GUIA_INTEGRAL_TUTORIA.md`.
- Corrección de referencias RN-01/RN-05 y de la salida generada por los builders.

Formato basado en Keep a Changelog. Versionado SemVer (ver `mantenimiento/MANTENIMIENTO_Y_EVOLUCION.md`).

## [1.0.0] · 2026-09-03

**Primera versión estable, lista para distribución.**
Veredicto: `VERIFICADO CON LÍMITES` (ver `tests/REGISTRO_DE_PRUEBAS.md` §3).

### Qué desbloquea esta versión
El titular ha **instalado los paquetes en ChatGPT Work, Claude Cowork y Antigravity** y ha confirmado
su correcto funcionamiento el 2026-09-03. Era lo único que faltaba: desde la primera entrega, el estado
`NO CERRADO` señalaba exactamente esta ausencia.

### Cambiado
- Versión `1.0.0` en todo el sistema. Retirados los avisos de «no verificado» de los README de
  instalación de los tres adaptadores, sustituidos por la confirmación fechada.
- `tests/REGISTRO_DE_PRUEBAS.md` reescrito: qué se ha confirmado, en qué plataformas, con qué fecha, y
  **qué parte del registro no se ha cumplimentado**.
- Retirada la coletilla de versión de las cabeceras de agentes y workflows, que se quedaba desfasada.
  La versión vive en `VERSION`, el README y este changelog.

### Límite declarado
La confirmación del titular es **global**, no ítem por ítem. El registro detallado de las baterías
C1–C16, F1–F10 y N1–N14, con prompt exacto y salida observada, no está cumplimentado. Por eso el
veredicto es `VERIFICADO CON LÍMITES` y no `VERIFICADO`. Cómo pasar de uno a otro: `REGISTRO_DE_PRUEBAS.md` §3.

### Lo que trajo cada versión hasta aquí
`0.9.0` construcción completa · `0.9.1` corrección normativa y regla de tres niveles ·
`0.10.0` puerta de entrada y carriles por nivel de conocimiento · `0.10.1` arreglo del plugin de Cowork,
detectado en una instalación real · `0.11.0` cobertura competencial y diversidad por barreras ·
`0.12.0` fichas de unidad, las dos sumas y coherencia criterio–competencia, a partir de una programación
real.

---

## [0.12.0-rc1] · 2026-09-02

**Fichas de unidad de programación y corrección del modelo de porcentajes.** A partir de una
programación didáctica real facilitada por el titular.

### Corregido
- **El modelo de porcentajes de la versión anterior era incompleto.** La 0.11.0 solo contemplaba una
  suma: que cada competencia llegase al 100 % repartida entre proyectos. Una programación real maneja
  **dos**:
  - **Suma 1 · pesos:** cuánto pesa cada competencia específica en la materia. **Todos los pesos
    juntos suman 100 %.** Es lo que hace que la programación esté completa.
  - **Suma 2 · reparto:** cómo se reparte cada competencia entre las unidades. **Cada competencia
    llega a su propio 100 %.**
- **La frontera con la calificación se ha afinado.** La regla anterior —«el porcentaje no es peso en la
  nota»— era demasiado amplia y dejaba fuera algo legítimo. Ahora se distingue: **ponderar la
  programación** es planificación del departamento, y el sistema ayuda a repartir y comprobar;
  **calificar a una persona** sigue prohibido, y eso incluye aplicar esos pesos al trabajo de un alumno
  concreto.

### Añadido
- **`plantillas/20_ficha_unidad_programacion.md`**: ficha con la estructura completa de una unidad —
  objetivos de aprendizaje, competencias clave, competencias específicas, descriptores operativos,
  saberes básicos, criterios de evaluación con su porcentaje e instrumento, situación de aprendizaje,
  elementos transversales, ODS, diversidad y papel de la IA.
- **`documentacion/CATALOGO_CURRICULAR.md`**: nomenclatura de las ocho competencias clave, cómo se
  codifican los descriptores operativos y los criterios, y las siete comprobaciones que hace el
  sistema. **Sin enunciados del currículo**: los aporta la persona.
- **Tres hojas nuevas en el Excel**: «Pesos por competencia» con la suma 1 y su aviso, «Unidades» con
  una fila por unidad, y las comprobaciones de coherencia en las instrucciones.
- **Comprobación de coherencia interna**, que es la que más disgustos ahorra: un criterio `n.m` exige
  que la competencia específica `n` esté declarada en esa unidad; un descriptor operativo exige su
  competencia clave. Bloqueo **B14** en el auditor.

### Cambiado
- B12 vigila ahora **las dos** sumas. B13 pasa a vigilar la calificación de personas, no el uso del
  porcentaje.
- W11 incorpora las fases de pesos, coherencia y generación de fichas de unidad.

### Nota
Los enunciados de competencias, criterios, saberes y descriptores **no se inventan nunca**: se copian
del currículo aplicable, que depende de la etapa, la materia y la administración educativa.

## [0.11.0-rc1] · 2026-09-02

**Cobertura competencial, atención a la diversidad y accesibilidad.** A partir de una prueba real
haciendo una programación.

### Añadido
- **Regla del 100 %** (`instruccion_maestra.md` §6 bis): cada competencia específica debe sumar 100 %
  a lo largo del curso, repartida entre los proyectos. Con las dos lecturas de la matriz —por
  competencia y por proyecto— y los tres problemas nombrados: **huérfana**, **incompleta** e **inflada**.
- **`plantillas/17_matriz_cobertura_competencial.xlsx`**: hoja de cálculo que **hace las sumas sola**,
  marca el estado de cada competencia con color y avisa de cuántas quedan sin cuadrar. Cuatro hojas:
  cómo se usa, matriz, ejemplo ficticio y diversidad por proyecto. También en `.md` para herramientas
  que no abren hojas de cálculo.
- **`plantillas/18_atencion_diversidad_y_accesibilidad.md`**: plan **por barreras, no por etiquetas**,
  con acceso, participación, expresión y **ampliación** para quien va sobrado.
- **`plantillas/19_programacion_por_proyectos.md`**.
- **`workflows/W11_programacion_por_proyectos.md`** y la skill **`programar-por-proyectos`** (la
  decimocuarta).
- Tabla de barreras y medidas generales en `agentes/A08`, y separación explícita entre **medidas
  generales de diseño** (las propone el sistema, las decide el docente) y **medidas específicas** (las
  determina el equipo de orientación).
- Bloqueos **B12** (matriz que no cuadra sin decirlo) y **B13** (cobertura presentada como peso en la
  nota) en el auditor A10. B3 pasa a bloquear también si falta el bloque de diversidad.
- Casos de prueba **F7** y **F8**, y pruebas negativas **N13** y **N14**.

### Cambiado
- El contrato de salida de actividad incorpora **competencias específicas con su porcentaje** y el
  bloque de **atención a la diversidad y accesibilidad**, que pasa a ser obligatorio.
- Las plantillas 02 y 03 incorporan ambos bloques.
- A02 sitúa el trabajo desde el principio: actividad suelta o parte de una programación.

### Límite reforzado
El **porcentaje de cobertura no es el peso en la nota**. Dice cuánto se trabaja y se evidencia una
competencia, no cuánto vale un proyecto en la calificación. El sistema sigue sin calcular
calificaciones ni proponer ponderaciones.

## [0.10.1-rc1] · 2026-09-02

**Corrección de empaquetado del plugin de Claude Cowork.** Detectada al intentar instalarlo: el
validador de plugins rechazó el paquete con once errores.

### Corregido
- **Nombres de los subagentes.** La carpeta `agents/` del plugin llevaba los nombres de archivo de la
  fuente canónica (`A01_orquestador_educativo.md`), con guiones bajos y mayúsculas. El validador exige
  nombres que empiecen y terminen en carácter alfanumérico y que solo contengan letras, números y
  guiones. Ahora el build los transforma: `a01-orquestador-educativo`.
- **`agentes/_LEEME.md` ya no se copia a `agents/`.** Es documentación, no un agente, y su nombre
  empieza por guion bajo.
- **Frontmatter en los subagentes.** Antes se copiaban sin cabecera YAML, así que el nombre se deducía
  del archivo. Ahora cada subagente del plugin lleva `name` y `description`, esta última extraída de su
  propia sección «Misión».
- **El catálogo de skills sale de `skills/`** en el paquete de Cowork y pasa a la carpeta de
  documentación: dentro de `skills/` solo deben vivir carpetas de skill.
- Se retira la versión fija de la cabecera de los archivos de agente, que se había quedado en
  `0.9.0-rc1`. La versión vive solo en `VERSION`, el README y el changelog.

### Añadido
- Dos comprobaciones nuevas en el validador para que esto no vuelva a pasar: nombres y frontmatter de
  los subagentes, y ausencia de archivos sueltos en `skills/`.

**Nota:** la fuente canónica conserva `agentes/` con sus nombres actuales, porque así los citan los
workflows y las skills. La transformación ocurre solo en el momento de construir el paquete.

## [0.10.0-rc1] · 2026-09-02

**Adopción por niveles de conocimiento.** Fase 1 del plan. Estado: sigue `NO CERRADO`.

### Añadido
- **`EMPIEZA_AQUI.md`**: puerta de entrada de tres minutos, sin configuración previa. Ocho frases de
  reconocimiento que resuelven a la vez el rol y el punto de partida de quien llega.
- **Skill `empezar-desde-cero`** (la decimotercera), para que esa puerta se active por lenguaje natural
  en las plataformas que usan skills.
- **Tres carriles de interacción** —acompañado, estándar y directo—, con reglas propias de jerga,
  número de preguntas, longitud y cierre. El sistema anuncia el carril y la persona puede cambiarlo.
- **Detección del punto de partida** en A01, separada del rol.
- **Cuatro situaciones difíciles** tratadas explícitamente en A01: la persona escéptica, la preocupada,
  la que ya usa IA sin criterio y la desbordada.
- **`documentacion/GLOSARIO.md`**: treinta términos en lenguaje llano.
- **`documentacion/LECTURA_FACIL.md`**: versión en lectura fácil para familias.
- **Casos de demostración de primaria, FP y AMPA**, además del de secundaria.
- **Declaración de vida útil** en el arranque, en el README, en la puerta de entrada y en las
  condiciones de uso: fecha de corte, avisos a los seis meses y al año, y advertencia expresa de que
  **no se garantiza mantenimiento ni versiones nuevas**.
- Condiciones de uso actualizadas a la distribución real: descarga sin coste desde la tienda mediante
  cupón, previo registro.

### Cambiado
- **Regla nueva que manda sobre el arranque:** nadie configura nada para obtener su primer resultado.
  Antes se ofrecía la configuración mínima antes de resolver; ahora se resuelve primero.
- El estilo del núcleo se adapta al carril, con una prueba explícita: ¿lo entendería alguien que no
  trabaja en esto?

### Pendiente
La batería de pruebas de plataforma sigue `BLOCKED`.

## [0.9.1-rc1] · 2026-09-02

**Corrección normativa y de rigor.** Ámbito fijado: **España**. Estado: sigue `NO CERRADO`.

### Corregido
- **Fecha de aplicación de los usos educativos de alto riesgo.** La versión anterior afirmaba que el
  Anexo III era exigible desde el 2 de agosto de 2026. El Reglamento (UE) 2026/1744 lo aplazó al
  **2 de diciembre de 2027**. Corregido en núcleo, documentación e índices.

### Añadido
- **`documentacion/REFERENCIAS_NORMATIVAS.md`**: índice único de fuentes normativas con organismo,
  enlace, fecha de consulta, naturaleza y lugar de uso. Lo que no está ahí, no se cita.
- **Regla de tres niveles** en `instruccion_maestra.md` §7.7: referencia con enlace y fecha ·
  implicación sugerida en condicional con destinatario de validación · nunca dictamen. Fecha de corte
  normativa y aviso de caducidad a los seis meses.
- **Artículo 5 (prácticas prohibidas)** como referencia vigente: inferir emociones en centros
  educativos y categorización biométrica. Filtro **paso 0** en W07, en la skill correspondiente y en la
  ficha de evaluación de herramientas.
- **Artículo 4 (alfabetización)** y **artículo 50 (transparencia)** como referencias vigentes, con su
  traducción práctica en la plantilla de declaración de uso de IA.
- **Prohibiciones de 2 de diciembre de 2026** sobre contenido íntimo no consentido y material de abuso
  infantil.
- **Capa española**: LOPDGDD, reparto del responsable del tratamiento, riesgo para el docente que usa
  herramientas no autorizadas, referencia de 14 años frente a la recomendación de 13 de UNESCO.
- **Bifurcación del W09**: rama de posible delito o ciberacoso con activación inmediata del protocolo
  del centro y remisión al protocolo marco estatal de abril de 2026; rama de incidencia menor.
- **Gradación del Consejo Escolar del Estado** (restringido / asistido / integrado) en la matriz de usos.
- Campos obligatorios nuevos en la configuración: administración educativa, instrucción sobre IA
  aplicable, protocolo de acoso, DPD, responsable del tratamiento y asesoría.
- Bloqueos **B10** (afirmación normativa sin fuente o dictamen encubierto) y **B11** (práctica
  prohibida) en el auditor A10.
- Condiciones de uso adaptadas a **distribución gratuita con registro** y aviso de actualizaciones.

### Pendiente
Lo mismo que en 0.9.0-rc1: la batería de pruebas de plataforma sigue `BLOCKED`.

## [0.9.0-rc1] · 2026-09-02

**Estado: NO CERRADO.** Falta ejecutar la batería de pruebas del §22 dentro de ChatGPT Work,
Claude Cowork y Antigravity sobre los ZIP finales. Hasta que exista ese registro, no se asigna `1.0.0`
ni se declara compatibilidad observada.

### Añadido
- Núcleo operativo: `instruccion_maestra.md`, `INICIO_UNIVERSAL.md`, `01_MODOS_Y_PERFILES.md`,
  `00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md`.
- Diez agentes A01–A10 con misión, activación, entradas, proceso, contrato de salida, límites y derivaciones.
- Doce skills operativas con `SKILL.md`, activación natural y exclusiones.
- Diez workflows W01–W10 con puertas humanas y criterios de terminado.
- Dieciséis plantillas limpias y editables.
- Estructura de conocimiento con siete carpetas temáticas y `_LEEME.md` en cada una.
- Documentación de uso: guía de inicio, catálogo de usos, privacidad y menores, condiciones de uso,
  límites y escalado, FAQ.
- Demo ficticia aislada y fixtures anonimizados.
- Plan de pruebas, validador estático y guion de pruebas de plataforma.
- Cuatro adaptadores derivados por script desde la fuente canónica.
- Paquete de desarrollo y mantenimiento con arquitectura, matriz de dependencias, registro de
  decisiones y política de versiones.
- Guía maestra de uso en Word.

### Pendiente para 1.0.0
- Registro `PASS/FAIL/BLOCKED` de la batería común y de los casos F1–F6 en las tres plataformas.
- Comprobación visual de los nombres de menú de instalación en cada plataforma.
- Incorporación, si procede, de los tres documentos internos de JGF citados en el §1 de la
  instrucción maestra y hoy marcados como «No consta».
# Edición Comunitaria 1.3.2-comunitaria.3 · 2026-10-08

- Derivada de la fuente 1.3.2, sin recortar agentes, skills, workflows ni plantillas.
- Adaptadas condiciones, FAQ, presentación, versión y guías a la descarga gratuita desde GitHub.
- Conservadas las guías y decisiones históricas; las condiciones actuales son la referencia vigente.
- Añadidas entrada de licencia, forma de cita y guía de contribución.
- Los constructores excluyen auxiliares de macOS y no borran destinos existentes.
- Las comprobaciones comunitarias se registran separadas de las confirmaciones de plataforma históricas.
- La fecha de corte normativa no se renueva mediante este cambio de distribución.
