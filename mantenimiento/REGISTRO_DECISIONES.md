# Registro de decisiones

Formato: qué se decidió, por qué, qué se descartó y qué habría que revisar si cambian las condiciones.

---

**D01 · Fuente canónica única con build determinista.**
*Por qué:* cuatro copias manuales divergen en semanas y nadie sabe cuál es la buena.
*Descartado:* mantener cuatro paquetes editables por separado.
*Revisar si:* alguna plataforma exige una estructura incompatible con la derivación automática.

**D02 · El conocimiento del centro no viaja en el paquete.**
*Por qué:* un método que se distribuye no puede llevar dentro documentos de una entidad concreta.
*Descartado:* incluir ejemplos reales anonimizados.
*Revisar si:* nunca. Es un invariante.

**D03 · La demo solo viaja en el paquete genérico.**
*Por qué:* en las plataformas con skills, la demo compite con el conocimiento real y puede mezclarse.
En el genérico es necesaria para tener una primera experiencia sin configurar nada.
*Descartado:* incluirla en los cuatro; excluirla de todos.
*Revisar si:* aparece confusión entre demo y datos reales en las pruebas.

**D04 · Claude Cowork como plugin con `.claude-plugin/plugin.json`.**
*Por qué:* es el formato documentado el 2026-09-02 en `code.claude.com/docs/en/plugins`, con
`skills/`, `agents/` y `commands/` en la **raíz del plugin**, nunca dentro de `.claude-plugin/`.
*Descartado:* configuración suelta en `.claude/`, que no es distribuible.
*Revisar si:* cambia el manifiesto o el mecanismo de instalación.

**D05 · ChatGPT Work como skill, con nota sobre el plugin.**
*Por qué:* la documentación de OpenAI describe la skill (`SKILL.md` + `references/` + `assets/` +
`agents/openai.yaml`) como formato de creación, y el empaquetado como plugin como vía de distribución
más allá de un repositorio. No se ha observado la interfaz de una cuenta Work, así que se entrega el
formato de creación y se documenta la vía de distribución sin certificarla.
*Descartado:* afirmar un procedimiento de instalación no observado.
*Revisar si:* se obtiene acceso a una cuenta Work y se puede comprobar el menú real.

**D06 · Antigravity: `.agents/skills/` + `AGENTS.md`, con agentes y workflows como documentos.**
*Por qué:* la documentación de skills de Antigravity no declara soporte nativo de agentes ni de
workflows como formatos propios. Inventar `.agents/agents/` habría sido declarar compatibilidad no
comprobada.
*Descartado:* crear carpetas de agentes y workflows nativas «por si acaso».
*Revisar si:* Antigravity publica un formato oficial de agentes o workflows.

**D07 · Versión `0.9.0-rc1` y estado `NO CERRADO`.**
*Por qué:* el §19.2 del encargo prohíbe `1.0.0` sin pruebas críticas superadas, y las pruebas de
plataforma están `BLOCKED` por falta de acceso interactivo.
*Descartado:* etiquetar `1.0.0` apoyándose en la validación estática.
*Revisar si:* se completa el registro de pruebas en las tres plataformas.

**D08 · Etiquetas de trazabilidad obligatorias en toda salida.**
*Por qué:* es lo que separa este sistema de un chat. Sin trazabilidad no hay revisión posible.
*Descartado:* usarlas solo en salidas «importantes»; la distinción se degrada sola.

**D09 · Sin conectores, hooks ni ejecución externa.**
*Por qué:* el núcleo funciona con archivos. Cada permiso añadido es superficie de riesgo con menores.
*Revisar si:* aparece una necesidad real que no pueda cubrirse con archivos.

**D10 · Un único centro ficticio para todos los ejemplos.**
*Por qué:* facilita reconocer al instante que un ejemplo es ficticio.
*Descartado:* ejemplos genéricos sin nombre, que se confunden con casos reales.

**D11 · Los tres documentos internos del §1 quedan como «No consta».**
*Por qué:* no están en el workspace conectado. Suponer su contenido habría sido inventar criterios de
JGF.
*Revisar si:* se incorporan al workspace; entonces se reconstruye y se revisa la coherencia.

**D12 · Ámbito: España, declarado.**
*Por qué:* decisión del titular. Un sistema que cita normas concretas solo es útil si sabe en qué
jurisdicción está. La ambigüedad anterior producía referencias europeas sin aterrizaje.
*Consecuencia:* asume la obligación de mantener actualizada la capa española y de declarar una fecha de
corte normativa.

**D13 · El sistema no afirma Derecho: regla de tres niveles.**
*Por qué:* instrucción expresa del titular —«no quiero que haya afirmaciones, siempre sugerencias a
validar, con fuentes oficiales, públicas y contrastadas, en un índice de referencia con enlaces»—.
*Cómo:* referencia con enlace y fecha · implicación sugerida en condicional con destinatario de
validación · nunca dictamen. Implementado en `instruccion_maestra.md` §7.7, A06, A09 y el bloqueo B10.
*Matiz deliberado:* citar literalmente una fuente oficial **no** es una afirmación propia, y degradar
una prohibición a «quizá convendría revisar» sería un fallo de servicio. Por eso la cita se mantiene
firme y lo que desaparece es el dictamen.
*Descartado:* preparar un dossier para revisión jurídica externa; se sustituye por el índice interno.

**D14 · Distribución gratuita con registro.**
*Por qué:* decisión del titular. El registro tiene una finalidad operativa concreta: poder avisar
cuando caduque una referencia normativa.
*Consecuencia:* las condiciones de uso incorporan el apartado 0; y sube la exigencia de autosuficiencia
del sistema, porque no habrá acompañamiento humano en la instalación.

**D15 · Corrección de la fecha del alto riesgo.**
*Por qué:* el Reglamento (UE) 2026/1744 aplazó el Anexo III al 2 de diciembre de 2027 — referencia
RN-05 en `documentacion/REFERENCIAS_NORMATIVAS.md`,
https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=OJ%3AL_202601744, consultado el 2026-09-02. La
versión 0.9.0-rc1 afirmaba agosto de 2026.
*Consecuencia:* comprobación automática en el validador para que no reaparezca.

**D16 · Puerta de entrada antes que configuración.**
*Por qué:* el sistema servía bien a quien ya sabía y perdía a quien no. Con distribución sin coste y sin
acompañamiento humano, quien llega solo abandona en la tercera pregunta.
*Cómo:* `EMPIEZA_AQUI.md` + skill `empezar-desde-cero` + regla en el §2 del núcleo: nadie configura
nada para obtener su primer resultado.
*Descartado:* mejorar la configuración mínima. El problema no era su longitud, era su posición.

**D17 · Tres carriles en lugar de un agente nuevo.**
*Por qué:* la adaptación al nivel es transversal a todo lo que hace el sistema. Un agente aparte habría
que invocarlo, y entonces ya no adapta nada.
*Cómo:* carriles acompañado/estándar/directo en A01 y en el §8 del núcleo.

**D18 · Vida útil declarada.**
*Por qué:* el titular ha indicado que estos sistemas tienen recorrido corto y que puede no haber
mantenimiento a medio plazo. Un sistema que cita normas con fecha y que puede quedar sin actualizar
tiene que decirlo, no ocultarlo.
*Cómo:* fecha de corte visible, avisos a los seis meses y al año, apartado 0 bis en las condiciones y
comprobación en el validador. Se distingue expresamente lo que caduca (el sistema) de lo que no (lo que
la persona produce con él).
*Alternativa descartada:* prometer actualizaciones que quizá no lleguen.

**D19 · Los agentes se transforman al construir, no se renombran en la fuente.**
*Por qué:* el validador de plugins de Claude exige nombres con letras, números y guiones. La fuente
canónica usa `A01_orquestador_educativo.md`, y ese nombre lo citan los workflows, las skills y la
documentación. Renombrar en origen habría obligado a tocar decenas de referencias.
*Cómo:* `tools/build_adapters.py` genera `agents/` con nombres en minúscula y guiones, añade el
frontmatter `name`/`description` a partir de la sección «Misión» de cada agente, y excluye `_LEEME.md`.
*Comprobación:* el validador rechaza cualquier nombre inválido o sin frontmatter, para no reincidir.
*Aprendizaje:* la validación estática propia no sustituye a la del anfitrión. Hasta que alguien no
intenta instalar el paquete de verdad, hay errores que no aparecen. Es exactamente lo que el estado
`NO CERRADO` venía advirtiendo.

**D20 · Cobertura competencial con la regla del 100 %.**
*Por qué:* una prueba real haciendo una programación mostró que el sistema diseñaba buenos proyectos
pero no permitía comprobar lo que un departamento necesita comprobar: que ninguna competencia se queda
sin trabajar y que ninguna ocupa el sitio de otra.
*Cómo:* §6 bis del núcleo, matriz en `.md` y `.xlsx` con sumas automáticas, W11, skill
`programar-por-proyectos` y bloqueo B12.
*Matiz deliberado:* la matriz se lee por filas (competencia, debe sumar 100 %) y por columnas
(proyecto, informativa). Las dos lecturas importan y se explican por separado, porque confundirlas es
el error habitual.

**D21 · La cobertura no es la nota. Frontera explícita.**
*Por qué:* un porcentaje asociado a un proyecto se convierte con demasiada facilidad en una ponderación
de calificación, y eso entraría en contradicción directa con la prohibición de calificar.
*Cómo:* la distinción está escrita en el núcleo, en la matriz, en la programación, en el W11 y en la
skill; el bloqueo B13 la vigila y el validador comprueba que el aviso viaja en las tres piezas.

**D22 · Diversidad por barreras, no por etiquetas.**
*Por qué:* preguntar «qué alumnado especial tengo» exige manejar datos que no deben entrar aquí, señala
a personas y produce diseños peores. Preguntar «qué puede impedir participar en esta tarea» produce
diseños que sirven a más gente y no requiere ningún dato personal.
*Cómo:* tabla de barreras y medidas generales en A08, plantilla 18, y separación explícita entre
medidas generales de diseño y medidas específicas del equipo de orientación.
*Añadido:* la ampliación para quien va sobrado forma parte del bloque. La diversidad también va hacia
arriba y suele olvidarse.

**D23 · Dos sumas, no una. Corrección de la 0.11.0.**
*Por qué:* al leer una programación didáctica real se vio que el modelo anterior era incompleto. Una
programación maneja el **peso de cada competencia en la materia** (todos los pesos suman 100 %) y el
**reparto de cada competencia entre las unidades** (cada una llega a su propio 100 %). La 0.11.0 solo
contemplaba la segunda.
*Aprendizaje:* la funcionalidad se diseñó sobre una intuición razonable y falló al contrastarla con un
documento real. Un ejemplo real vale más que tres iteraciones de diseño.

**D24 · Ponderar la programación sí; calificar personas no.**
*Por qué:* la regla de la 0.11.0 —«el porcentaje no es peso en la nota»— era demasiado amplia. Una
programación **necesita** ponderar criterios y competencias: es una decisión profesional de
planificación, documentada y aprobada por el departamento. Lo que no puede hacerse es aplicar esa
ponderación al trabajo de una persona concreta para producir su nota.
*Cómo:* tabla explícita de cuatro «puedes» y cuatro «no puedes» en §6 bis; B13 reformulado para vigilar
la calificación de personas, no el uso del porcentaje.
*Riesgo asumido:* la frontera es más fina que antes y depende de aplicarla bien. Se compensa con la
prueba negativa N13, que es conductual.

**D25 · Los enunciados del currículo no se inventan.**
*Por qué:* competencias, criterios, saberes y descriptores dependen de la etapa, la materia y la
administración educativa, y el texto normativo tiene sus propias condiciones de reproducción.
*Cómo:* `CATALOGO_CURRICULAR.md` recoge **nomenclatura y códigos**, no enunciados. Cuando no constan,
el sistema trabaja con códigos y registra el hueco.

**D26 · Comprobación de coherencia criterio ↔ competencia.**
*Por qué:* es el fallo más habitual en una programación y el más difícil de ver a ojo: una unidad cita
el criterio `4.1` pero no declara la competencia 4.
*Cómo:* regla en §6 bis, comprobación en el W11 y bloqueo B14. El sistema lo señala; corregirlo es
decisión del docente, porque puede faltar la competencia o sobrar el criterio.

**D27 · Cierre en `1.0.0` con veredicto `VERIFICADO CON LÍMITES`.**
*Por qué:* el titular instaló y comprobó el funcionamiento en las tres plataformas el 2026-09-03, que
era la condición que faltaba desde la primera entrega. Pero su confirmación es **global**, no ítem por
ítem: no existe el registro con prompt exacto y salida observada de las cuarenta pruebas de la batería.
*Descartado:* etiquetar `VERIFICADO` apoyándose en una confirmación global. Habría sido cómodo y falso.
*Descartado también:* seguir en `NO CERRADO`. El uso previsto está cubierto y el sistema instala y
funciona; mantenerlo bloqueado habría sido igual de inexacto en la otra dirección.
*Cómo se cierra el hueco:* `tests/REGISTRO_DE_PRUEBAS.md` §3 explica qué falta y cuánto cuesta, con las
siete pruebas negativas señaladas como prioritarias.

**D28 · La versión deja de repetirse dentro de los documentos.**
*Por qué:* las cabeceras de agentes y workflows llevaban la versión escrita a mano y se quedaron en
`0.9.0-rc1` mientras el sistema avanzaba hasta la `0.12.0`. Un dato duplicado es un dato que envejece.
*Cómo:* la versión vive en `VERSION`, en el README y en el changelog. En ningún sitio más.

**D29 · La capa autonómica es un enrutador de fuentes, no un catálogo de respuestas jurídicas.**
*Por qué:* la misma necesidad familiar o tutorial puede depender de normas, instrucciones y protocolos
distintos, y estos cambian durante la vida del paquete. La revisión detectó sustituciones y modificaciones
posteriores a 2022 en varios territorios.
*Cómo:* RN-36 reúne las puertas oficiales de diecisiete comunidades, Ceuta y Melilla; A20 y W26 obligan
a verificar territorio, etapa, boletín, vigencia, instrucción del curso y protocolo del centro. Toda
consecuencia se rotula «Sugerencia operativa a revisar y contrastar» y A10 la bloquea mediante B19 si se
presenta como certeza.
*Límite aceptado:* el directorio no garantiza exhaustividad ni vigencia futura. Cada centro completa la
ficha 53 y valida con el órgano competente.

**D30 · Secuencia de adopción: Guía Maestra → matriz → demostraciones.**
*Por qué:* la evolución tenía piezas familiares y autonómicas suficientes, pero faltaba un recorrido
único para una persona usuaria y una relación comprobable entre intención, implementación y evidencia.
*Cómo:* `documentacion/GUIA_MAESTRA_DE_USO.md` explica el uso; `documentacion/MATRIZ_TRAZABILIDAD_SISTEMA.md`
conecta 40 filas con componentes y pruebas; `demo/README_DEMOSTRACIONES.md` y tres casos sintéticos
permiten observar el circuito sin datos reales. La guía se materializa también en DOCX y los artefactos
visibles se incluyen en la entrega con SHA-256.
*Límite aceptado:* las demostraciones no sustituyen las pruebas manuales en cada plataforma ni la
revisión del centro, su normativa autonómica, sus protocolos o su DPD.
## EC01 · Edición Comunitaria completa · 2026-10-08

Por encargo de JGF, se prepara una copia comunitaria gratuita del sistema completo para GitHub.
Se conserva la arquitectura y el catálogo operativo. La condición de descarga mediante tienda,
cupón y registro descrita en decisiones históricas no se aplica a esta edición.

Los forks y funciones de GitHub se contemplan sin conceder un derecho general de reventa o
redistribución externa. Se permite el uso profesional y cobrar por servicios con resultados
revisados. Las condiciones completas se mantienen en el archivo canónico existente.

Los originales 1.3.2 permanecen intactos. La versión comunitaria identifica nuevos ZIP y hashes.
Las comprobaciones estáticas no certifican conversaciones ni instalaciones de este nuevo paquete.
La publicación requiere aprobación del titular y validación independiente conforme al flujo JGF.
