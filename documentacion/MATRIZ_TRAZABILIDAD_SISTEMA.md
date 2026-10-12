# Matriz de trazabilidad del sistema

## Aula y Comunidad Educativa Aumentada · versión 1.3.2-comunitaria.3

**Fecha de corte:** 2026-09-04 · **Estado:** propuesta para revisión y contraste humano.  
Esta matriz conecta intención, componente y evidencia. No acredita cumplimiento normativo ni
sustituye las decisiones del centro.

### Cómo leerla

- `R` = capacidad transversal; `F` = familia/tutoría; `T` = territorial y fuentes; `S` = salvaguarda.
- Una referencia `Axx`, `Wxx` o plantilla apunta al archivo homónimo de `agentes/`, `workflows/` o `plantillas/`.
- `Demo` identifica un caso reproducible en `demo/`.
- `Prueba` remite a la prueba común, funcional o negativa del plan de pruebas.
- `Pendiente` significa que una persona debe aportar, revisar o aprobar algo; no es un fallo del sistema.

| ID | Requisito o capacidad | Fuente/justificación | Agente(s) | Workflow / skill | Plantilla o salida | Demo | Prueba / evidencia |
|---|---|---|---|---|---|---|---|
| R01 | Arranque portable y declaración de capacidad real | Objetivo del sistema y límites | A01 | W01 / `empezar-desde-cero` | `EMPIEZA_AQUI.md` | `caso_demo_actividad.md` | C1, C10, C13 |
| R17 | Distinguir plugin, contexto disponible y archivos leídos | Límite de acceso de plataformas | A01, A21 | W27 / `verificar-contexto-claude-cowork` | `INTEGRACION_CLAUDE_COWORK.md` | — | F21, N21 |
| R02 | Diseñar actividad con evidencia y alternativa sin IA | Diseño educativo | A02 | W02 / `disenar-actividad` | 02, 03 | `caso_demo_actividad.md` | C6, F1 |
| R03 | Adaptar explicación a etapa y acceso | Inclusión y comprensión | A03, A08 | W03 / `adaptar-explicacion` | 04, 18 | — | F2, F14 |
| R04 | Feedback formativo sin nota ni ranking | Supervisión docente | A04, A10 | W04 / `revisar-feedback` | 05, 06 | — | C8, F3, N1 |
| R05 | Alfabetización crítica, ética y práctica en IA | Uso educativo responsable | A05 | W05 / `alfabetizacion-ia` | 14 | — | F4, C15 |
| R06 | Normas de uso del centro y participación | Gobernanza humana | A06, A10 | W06 / `crear-normas-ia` | 09, 10 | — | F5, N4 |
| R07 | Evaluar una herramienta antes de adoptarla | Privacidad, proporcionalidad y pedagogía | A06, A10 | W07 / `evaluar-herramienta` | 12 | — | N9 |
| R08 | Trazar fuentes, fecha, alcance y huecos | Verificación de fuentes | A09 | W10 / `actualizar-fuentes` | 08, 16 | `caso_contraste_autonomico.md` | C2, C12, C16 |
| R09 | Minimizar datos y proteger menores | RGPD/LOPDGDD y gobernanza | A06, A10 | W09/W07 / `privacidad-menores` | 07, 15 | Todos | C7, N5, N15 |
| R10 | Inclusión, accesibilidad y DUA | Atención a la diversidad | A08 | W12 / `atender-diversidad` | 18, 22 | — | F14, N3 |
| R11 | Bienestar, protección y derivación humana | Protección y convivencia | A12 | W13 / `activar-proteccion` | 24, 25, 52 | `caso_tutoria_familia.md` | N3, N10, N18 |
| R12 | Seguimiento y revisión de decisiones | Mejora continua | A13 | W14 / `preparar-seguimiento` | 30, 32 | — | C16 |
| R13 | Absentismo y coordinación responsable | Acción tutorial | A13 | W15 / `gestionar-absentismo` | 33–35 | — | — |
| R14 | Convivencia y sociograma con datos agregados | Clima y participación | A14 | W16/W17 / `convivencia` | 36, 37 | — | N3, N5 |
| R15 | Ciberconvivencia y ciudadanía digital | Prevención y alfabetización | A15 | W18 / `ciberconvivencia` | 38, 39 | — | N10 |
| R16 | Acogida, transición y autocuidado | Continuidad educativa | A16 | W19 / `transicion-acogida` | 40–42 | — | F16 |
| R18 | Coordinar el inicio de curso por hitos | Continuidad y organización educativa | A22 | W28 / `inicio-curso-comunidad-educativa` | 54 | `caso_inicio_curso.md` | F22 |
| R19 | Preparar el primer día con el alumnado | Acogida, pertenencia y acceso | A22, A11, A08 | W29 | 55 | `caso_inicio_curso.md` | F23 |
| F01 | Incorporar a familias con rol, canales y límites | Participación y representación | A17, A18 | W20 / `incorporar-familias` | 43, 44 | `caso_familia_autonomia.md` | F11, N15, N16 |
| F02 | Preparar entrevista familia–tutor | Acción tutorial colaborativa | A18 | W21 / `entrevista-familia-tutor` | 45–47 | `caso_tutoria_familia.md` | F12 |
| F03 | Acompañar el aprendizaje en casa sin hacer la tarea | Corresponsabilidad educativa | A17 | W22 / `acompanamiento-hogar` | 47, 48 | `caso_tutoria_familia.md` | F13, N6 |
| F04 | Participación familiar inclusiva y multicanal | Accesibilidad y retorno | A07, A08 | W23 / `participacion-familiar` | 49 | — | F14 |
| F05 | Mediación parental de pantallas e IA | Ciudadanía digital familiar | A19, A15 | W24 / `mediacion-parental` | 50 | `caso_familia_autonomia.md` | F15 |
| F06 | Orientación y decisiones compartidas | Voz del alumno y opciones verificadas | A19, A16 | W25 / `orientacion-transicion` | 51, 52 | `caso_familia_autonomia.md` | F16, N17 |
| F07 | Preparar la primera reunión docente con una familia | Acción tutorial de comienzo de curso | A22, A18, A17 | W30 | 56 | `caso_inicio_curso.md` | F24 |
| F08 | Preparar la reunión general del instituto con las familias | Información común y participación accesible | A22, A07, A08, A18 | W31 | 57 | `caso_inicio_curso.md` | F25 |
| F09 | Apoyar a las familias durante el inicio de curso | Autonomía, canales y ayuda inicial | A22, A17, A19, A07 | W32 | 58 | `caso_inicio_curso.md` | F26 |
| T01 | Contrastar la comunidad autónoma aplicable | Variación territorial | A20, A09 | W26 / `contrastar-normativa-autonomica-educativa` | 53 | `caso_familia_autonomia.md` | F17 |
| T02 | Usar boletín y portal educativo oficiales | Jerarquía de fuentes | A09, A20 | W10/W26 | `REFERENCIAS_NORMATIVAS.md` | `caso_contraste_autonomico.md` | C12 |
| T03 | No extrapolar una norma o protocolo | Incertidumbre territorial | A20 | W26 | `53_ficha_contraste_autonomico.md` | `caso_contraste_autonomico.md` | N19 |
| T04 | Rotular la consecuencia como sugerencia revisable | Responsabilidad institucional | A10, A20 | W26 / bloqueo B19 | Guía + ficha 53 | Todos los territoriales | N20 |
| T05 | Cubrir 17 CCAA, Ceuta y Melilla | Alcance declarado | A20 | W26 | `FUENTES_AUTONOMICAS...md` | — | `c_autonomias` |
| T06 | Distinguir fuente, fecha, vigencia y protocolo de centro | Control de actualización | A09, A10 | W10/W26 | 08, 53 | Todos los territoriales | C11, C16 |
| S01 | Verificar representación humana antes de conceder acceso | Protección de terceros | A18, A06 | W20/W21 | 43, 45 | `caso_familia_autonomia.md` | N15, N16 |
| S02 | Incorporar voz del alumno según edad y madurez | Interés superior y participación | A18, A12 | W20–W25 | 44, 51, 52 | `caso_tutoria_familia.md` | F12, F16, N17 |
| S03 | Bloquear avisos automáticos en protección | Evitar perjuicio | A12, A10 | W13 | 24, 25, 52 | `caso_tutoria_familia.md` | N18 |
| S04 | No introducir datos de terceros o de menores | Minimización | A06 | W07/W20/W21 | 07, 15, 43 | Todos | C7, N5, N15 |
| S05 | No realizar acciones externas | Control humano | A10 | Todos | `CONDICIONES_DE_USO.md` | — | C5, N4 |
| S06 | No calificar ni inferir autoría de IA | Frontera pedagógica | A04, A10 | W04/W14 | 05, 06 | — | C8, N1, N2, N13 |
| S07 | Declarar `No consta` en vez de completar por similitud | Honestidad y trazabilidad | A01, A09 | W01/W10/W26 | 08, 53 | `caso_contraste_autonomico.md` | C3, C4, N14, N19 |
| S08 | Declarar fecha de corte y vida útil | Control temporal | A09, A10 | W10 | `REFERENCIAS_NORMATIVAS.md` | — | C11, C16 |
| S09 | Ofrecer alternativa accesible y no digital | Inclusión | A08, A19 | W23/W24 | 49, 50 | — | F14, F15 |
| S10 | Registrar versión, ruta y revisión humana | Auditoría de calidad | A10 | W01–W32 | 16, 53, 54–58 | Todos | validador estático |
| S11 | No presentar skills visibles como archivos leídos | Honestidad y privacidad de plataforma | A21, A06, A10 | W27 | `INTEGRACION_CLAUDE_COWORK.md` | — | F21, N21 |

## Cobertura y pendientes

- **Capacidades registradas:** 19 transversales + 9 familiares + 6 territoriales + 11 salvaguardas = **45 filas**.
- **Carril familiar:** A17–A19, W20–W25 y plantillas 43–52 están vinculados a capacidades y pruebas.
- **Carril autonómico:** A20, W26, skill de contraste, ficha 53 y directorio oficial están vinculados.
- **Integración Cowork:** A21, W27 y `verificar-contexto-claude-cowork` comprueban el permiso de carpeta y
  separan el método del contexto documental.
- **Inicio de curso:** A22, la skill específica, W28–W32 y las plantillas 54–58 separan los cinco hitos
  y exigen adaptación, comprensión, accesibilidad, ajuste y aprobación humana.
- **Pendientes explícitos:** datos del centro, protocolo vigente, canal institucional, representación,
  órgano aprobador, DPD, calendario y resultados de pruebas manuales en cada plataforma.
- **Criterio de cierre:** una fila solo puede marcarse como validada cuando existe salida observada,
  fuente o fixture identificable, responsable humano y registro de fecha. La matriz no certifica por sí sola.
