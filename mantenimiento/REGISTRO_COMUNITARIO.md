# Registro de la Edición Comunitaria

Versión: `1.3.2-comunitaria.3` · Preparación: 2026-10-08.
Fuente: paquete de desarrollo y mantenimiento `1.3.2`, de 2026-09-04.

## Alcance

Se conserva el sistema completo y su arquitectura. No se reescriben los agentes, workflows,
skills ni plantillas operativas. Los cambios se concentran en distribución, condiciones,
documentación de acceso, metadatos de versión y construcción de paquetes.

Las guías históricas permanecen como antecedentes. La guía comunitaria se ha revisado en sus
diez páginas, conservando el diseño original y corrigiendo la distribución y la fecha normativa.
El inventario operativo es de 22 agentes, 32 workflows, 31 skills y 58 plantillas Markdown
numeradas, más la matriz Excel y los archivos de orientación de cada carpeta.

## Comprobaciones

El validador de la fuente ha superado 19 comprobaciones, sin avisos ni fallos.
Se ha corregido el tratamiento de auxiliares AppleDouble, que no son componentes educativos
y no deben incluirse en los ZIP. No se han eliminado de los archivos originales.

Los constructores verifican los cuatro paquetes de usuario desde extracciones limpias y
guardan el resultado, el código de salida y el SHA-256 en `evidencias/` del paquete de mantenimiento.
Si falla un paquete, no se produce la entrega final. Los archivos descargables tienen nuevas
versiones y hashes; las evidencias antiguas se mantienen identificadas como históricas.

Para comparar preservación e integridad, utiliza `tests/verificar_edicion_comunitaria.py`:

```bash
python3 tests/verificar_edicion_comunitaria.py \
  --original RUTA_FUENTE_1_3_2 --repositorio . --paquetes RUTA_ZIPS --evidencia RUTA_INFORME
```

Esta verificación complementa al validador: contrasta hashes del catálogo, estructura de
paquetes, ausencia de auxiliares, sumas internas y enlaces locales del README del repositorio.
No ejecuta conversaciones ni instala el sistema en cuentas de terceros.

## Revisión editorial y publicación

Registro Premium para presentación, condiciones y guía. Aplicado el filtro editorial del
Agente 01: autoría identificada, personas en el centro, supervisión y ausencia de promesas de alcance.

La revisión independiente prevista por el Agente 07 no se ha ejecutado en esta sesión:
no hay un segundo modelo disponible mediante las herramientas de trabajo. No se atribuye
una validación independiente a la revisión realizada por el mismo asistente.

La publicación queda pendiente de esa revisión y de la aprobación del titular, con cuenta y
destino identificados. No se ha creado un remoto ni subido archivos a GitHub.

## Límites de la evidencia

La comprobación estática de referencias normativas es heurística, no una auditoría jurídica de vigencia.
La fecha de corte sigue siendo 2026-09-03. Se contrastó la fuente oficial del Reglamento (UE)
2026/1744 y las condiciones de repositorios públicos de GitHub el 2026-10-08; ello no renueva
ni certifica todas las referencias del sistema.

- [Fuente oficial del Reglamento citado](https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=OJ%3AL_202601744).
- [Condiciones de GitHub sobre contenido público](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#d-user-generated-content).
- [Licencias de repositorios](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).

La fuente de requisitos tutoriales reseñada en la documentación no viaja como documento de
terceros. No se otorgan derechos sobre esa fuente: la atribución y los límites se conservan.
La revisión de los derechos propios de cualquier nueva aportación precede a su publicación.
