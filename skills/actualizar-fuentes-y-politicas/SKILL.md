---
name: actualizar-fuentes-y-politicas
description: Revisa y actualiza las fuentes, políticas y formatos de plataforma del sistema, registrando fecha y cambios.
---

# Actualizar fuentes y políticas

Ejecuta `workflows/W10_revisar_sistema.md` con `agentes/A09_verificador_fuentes.md`.

## Cuándo se usa
Revisión trimestral, cambio en una plataforma, cambio normativo, incidente que obliga a revisar, o
cuando alguien pregunta si el sistema sigue vigente.

## Cuándo NO se usa
- Para modificar la configuración de un centro → `configurar-comunidad-educativa`.
- Para cambiar el contenido de una norma → `crear-normas-uso-responsable-ia`.

## Entradas
Versión instalada y fecha de la última revisión.

## Pasos
1. Revisa la documentación oficial vigente de cada plataforma y **registra URL y fecha de consulta**.
2. Revisa las fuentes educativas y normativas del inventario. Para cada comunidad autónoma, Ceuta o
   Melilla usa W26 y comprueba boletín, portal educativo, modificaciones, instrucciones del curso y
   protocolo del centro. Añade la versión nueva con su fecha;
   **no sobrescribas** conclusiones históricas.
3. Revisa incidencias registradas y dudas recurrentes.
4. Clasifica cada cambio: corrección, mejora compatible o cambio mayor.
5. Actualiza `conocimiento/00_INDICE_FUENTES.md` y el changelog.
6. Si hay que reconstruir paquetes, hazlo desde la fuente canónica, nunca editando un adaptador.

## Contrato de salida
Tabla de fuentes revisadas (territorio · título · organismo · URL · fecha de consulta · vigencia · qué
cambió · **Sugerencia operativa a revisar y contrastar**) + propuesta de versión + lista de archivos afectados.

## Regla dura
No se declara compatibilidad con una plataforma sin haberla probado de nuevo sobre el paquete final.
