# Mantenimiento y evolución

Documento para la persona técnica que mantenga el sistema. No requiere haber participado en su
construcción.

## Principio rector

**Una sola fuente canónica.** Todo cambio se hace en `src/aula-comunidad-educativa-aumentada/` y se
propaga a los cuatro paquetes ejecutando el build. **Nunca** se edita un adaptador a mano: si lo haces,
el siguiente build lo sobrescribirá y las variantes divergirán en silencio.

## Ciclo de un cambio

```
1. Editar la fuente canónica
2. python3 tools/build_adapters.py         → regenera dist/ y los cuatro paquetes
3. python3 tests/validador_estructura.py   → sobre cada extracción limpia
4. Ejecutar tests/GUION_PRUEBAS_PLATAFORMA.md
5. Actualizar VERSION y CHANGELOG.md
6. Reconstruir paquetes y recalcular SHA256SUMS.txt
7. Regenerar la guía Word si cambió algo visible para la persona usuaria
8. Reconstruir el paquete de mantenimiento con la evidencia final
```

## Tareas de mantenimiento ordinario

### Actualizar el Índice de Referencia Normativa · **trimestral, no opcional**

`documentacion/REFERENCIAS_NORMATIVAS.md` es la única lista de fuentes normativas que el sistema puede
citar. Cada trimestre: comprobar que los enlaces siguen vivos, actualizar la fecha de consulta, añadir
la versión nueva **sin borrar la anterior**, actualizar la **fecha de corte normativa** de la cabecera y
revisar si alguna fuente ha cambiado de naturaleza (de propuesta a norma, de vigente a derogada).

Si cambia una fecha o una obligación, hay que revisar además: `instruccion_maestra.md` §7.2 y §7.7,
`agentes/A06`, `agentes/A09`, `documentacion/PRIVACIDAD_Y_MENORES.md`, `documentacion/LIMITES_Y_ESCALADO.md`,
`workflows/W07`, `workflows/W09` y las plantillas 07, 09, 12 y 15. El validador comprueba que ninguna
mención normativa se queda sin enlace y sin fecha.

### Actualizar referencias educativas y normativas
Añade la nueva versión de la fuente en `conocimiento/00_INDICE_FUENTES.md` con su fecha de consulta.
**No sobrescribas** conclusiones anteriores: añade una fila nueva y anota qué cambió. Si el cambio
afecta a una regla del núcleo (por ejemplo, a los usos de alto riesgo), edita también
`instruccion_maestra.md` §7 y déjalo reflejado en el changelog.

### Revisar cambios de plataforma
Trimestral, o antes si hay aviso. Consulta la documentación oficial de ChatGPT, Claude y Antigravity,
anota URL y fecha en el inventario de fuentes, y comprueba si cambia el formato de skill, el manifiesto
o la ruta de descubrimiento. Si cambia, ajusta `tools/build_adapters.py`, no los paquetes.

### Añadir o retirar una plantilla
1. Crea o elimina el archivo en `plantillas/`.
2. Actualiza la tabla de `plantillas/_LEEME.md`.
3. Actualiza las referencias en los workflows y skills que la citen (búsqueda por nombre de archivo).
4. Rebuild + validador.

### Modificar un agente, workflow o skill
Edita el archivo en la fuente canónica. Comprueba las referencias cruzadas: cada agente se cita desde
al menos un workflow, y cada skill desde `skills/_LEEME.md`. El validador avisa de referencias rotas.

### Corregir un límite pedagógico o una vulnerabilidad
Tratamiento prioritario. Corrige en `instruccion_maestra.md` §7 y en el agente afectado (normalmente
A04, A06 o A10). Añade una prueba negativa nueva en `tests/PLAN_DE_PRUEBAS.md`. Incrementa `PATCH` si
no cambia el contrato, `MINOR` si añade una capacidad, `MAJOR` si cambia lo que el sistema promete.

### Migrar la configuración de una persona usuaria
La configuración del centro vive en **su** copia, no en el paquete. Al actualizar:
1. La persona guarda su `00_CONFIGURACION_COMUNIDAD_EDUCATIVA.md`, su `conocimiento/` y su `resultados/`.
2. Instala la versión nueva.
3. Copia sus tres elementos de vuelta.
**Nunca** se incorporan datos de una entidad al paquete distribuible.

### Retirar una versión incompatible
Marca la versión en el changelog como retirada, con motivo y fecha. Indica a qué versión migrar y qué
se rompe. No borres los hashes antiguos: sirven para verificar copias en circulación.

## Distinguir tipos de cambio

| Tipo | Qué es | Ejemplo | Versión |
|---|---|---|---|
| Corrección | Arregla algo que estaba mal | Errata en una plantilla | PATCH |
| Mejora compatible | Añade sin romper | Una plantilla nueva | MINOR |
| Cambio mayor | Rompe compatibilidad | Cambia el contrato de salida o la estructura | MAJOR |

## Regla dura de certificación

No se usa evidencia de la fuente canónica, de un adaptador en construcción ni de una versión anterior
para certificar un ZIP final. Y **no se cambia el contenido de un paquete conservando versión y hash
anteriores**: eso invalida toda la cadena de verificación.
