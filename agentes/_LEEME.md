# Agentes

Veintidós agentes con responsabilidades distintas y contratos de salida verificables. No son personajes:
cada uno hace un trabajo que otro no hace, y cada uno puede bloquear o derivar.

| ID | Agente | Trabajo | Puede bloquear |
|---|---|---|---|
| A01 | Orquestador educativo | Interpreta, enruta y conserva la decisión pendiente | No |
| A02 | Diseñador de experiencias de aprendizaje | Resultados, evidencias y secuencia | No |
| A03 | Adaptador de explicaciones | Etapa, nivel previo, modalidad | No |
| A04 | Revisor formativo de trabajos | Feedback con criterios, sin nota | Sí (si no hay criterios) |
| A05 | Facilitador de alfabetización en IA | Progresión y práctica con evidencia | No |
| A06 | Uso seguro, privacidad y gobernanza | Datos, edad, finalidad, supervisión | Sí |
| A07 | Enlace familias y comunidad | Traducción a lenguaje claro y participación | No |
| A08 | Inclusión y accesibilidad | Alternativas de acceso y expresión | Sí (si el contenido esencial es inaccesible) |
| A09 | Verificador de fuentes | Origen, fecha, ámbito, naturaleza normativa y «No consta» | Sí |
| A10 | Auditor de calidad educativa | Puerta final independiente | Sí |
| A11 | Tutoría de Secundaria | Contextualiza la intervención tutorial y sus entregables | No |
| A12 | Protección y bienestar | Crisis, riesgo, maltrato, familia y derivación segura | Sí |
| A13 | Evaluación y seguimiento | Juntas, datos anonimizados, compromisos y absentismo | Sí |
| A14 | Convivencia y sociograma | Conflictos, mediación, dinámicas y distribución del aula | No |
| A15 | Ciberconvivencia y ciudadanía digital | Evidencias, IA ética, impactos y familias | Sí |
| A16 | Transición, acogida y autocuidado | Tránsito, matrícula sobrevenida, límites y desgaste docente | No |
| A17 | Acompañamiento familiar del aprendizaje | Hábitos, autonomía, motivación y apoyo doméstico | No |
| A18 | Coordinación familia–tutor | Representación, información, entrevistas y acuerdos | Sí |
| A19 | Mediación digital y orientación familiar | Pantallas, IA, decisiones y transiciones | Sí |
| A20 | Contraste normativo autonómico | Boletín, portal, vigencia, protocolo y sugerencia contrastable | Sí |
| A21 | Verificador de contexto en Claude Cowork | Acceso real a carpeta, archivos leídos y permiso de plataforma | Sí |
| A22 | Inicio de curso y comunidad educativa | Coordina apoyos para centro, alumnado, docentes y familias | Sí |

**Regla normativa:** ninguna mención de una norma sin fuente, enlace y fecha; nunca un dictamen.
Ver `instruccion_maestra.md` §7.7 y `documentacion/REFERENCIAS_NORMATIVAS.md`.

**Regla de derivación obligatoria:** cualquier tarea que implique menores, evaluación, normativa o
datos personales pasa por **A06** y por **A10** antes de entregarse.

En los workflows W12–W32 se activan además los agentes tutoriales, familiares y territoriales que correspondan. A12,
A15, A18 y A19 pueden detener el flujo cuando exista riesgo, representación no verificada o una petición que
invada intimidad; A13 detiene el análisis si los datos no están anonimizados o si se intenta calificar personas;
A20 detiene una afirmación autonómica sin fuente oficial y control de vigencia.
