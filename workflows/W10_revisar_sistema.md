> Workflow del sistema **Aula y Comunidad Educativa Aumentada**. Subordinado a `instruccion_maestra.md`.

# W10 · Revisar y evolucionar el sistema

**Disparador:** revisión trimestral, cambio en una plataforma, incidente, cambio normativo o petición.

**Entradas mínimas:** versión actual instalada y fecha de la última revisión.

## Fases

1. **Cambios de plataforma** (A09). Revisar la documentación oficial vigente de ChatGPT, Claude y
   Antigravity. Registrar URL y fecha de consulta en el inventario de fuentes.
2. **Cambios de fuentes** (A09). Revisar las fuentes educativas y normativas del inventario. No
   sobrescribir conclusiones históricas: añadir la nueva versión con su fecha.
3. **Incidencias** (A06). Revisar los registros de W09 y las dudas recurrentes.
4. **Patrones de uso**. Qué workflows se usan, cuáles no y por qué.
5. **Propuestas de cambio**. Clasificadas en corrección, mejora compatible o cambio mayor.
6. **Pruebas**. Ejecutar el validador estático y la batería del plan de pruebas.
7. **Versión**. Incrementar según SemVer.
8. **Reconstrucción de paquetes**. Desde la fuente canónica, con el script de build. **Nunca** editando
   un adaptador a mano.
9. **Regresión**. Repetir la batería sobre los ZIP nuevos, desde extracción limpia.
10. **Guía y hashes**. Actualizar la guía Word y recalcular SHA-256 si cambió cualquier archivo.

## Puertas humanas
El titular del sistema aprueba el cambio de versión y la retirada de versiones anteriores.

## Salidas
Nueva versión, changelog actualizado, hashes nuevos, registro de pruebas y notas de migración.

## Criterios de terminado
Los cinco ZIP y la guía comparten versión; los hashes corresponden a los archivos entregados; el
changelog explica qué cambió y por qué.

## Riesgos
Editar un adaptador y olvidar el núcleo; conservar hash antiguo con contenido nuevo; declarar
compatibilidad sin volver a probar.

## Regla dura
No se usa evidencia de la fuente, de un adaptador en construcción ni de una versión anterior para
certificar un ZIP final.
