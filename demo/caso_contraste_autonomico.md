# Demostración 3 · contraste autonómico prudente

## Contexto ficticio

Un equipo directivo de un centro situado en la Comunidad de Madrid quiere preparar una lista de
fuentes para revisar una comunicación a familias sobre la ESO. Pide localizar fuentes oficiales,
pero no pide certificar cumplimiento.

## Petición de demostración

> El centro está en la Comunidad de Madrid y prepara una comunicación para familias de ESO. Contrasta el marco autonómico con fuentes oficiales. Indica boletín, portal educativo, norma localizada, URL, fecha de consulta y huecos. No extrapoles a otras comunidades, no digas que el centro cumple y formula cualquier consecuencia como “Sugerencia operativa a revisar y contrastar”.

## Enrutamiento esperado

- **Agentes:** A09, A10 y A20.
- **Workflow:** W26.
- **Skill:** `contrastar-normativa-autonomica-educativa`.
- **Plantilla:** 53, ficha de contraste autonómico.
- **Bloqueo:** B19 si alguien pide confirmar cumplimiento o firmar.

## Salida esperada, en forma resumida

| Campo | Resultado esperado |
|---|---|
| Territorio | Comunidad de Madrid, confirmado por la petición |
| Fuente primaria | BOCM, enlace desde el directorio oficial del sistema |
| Portal complementario | Portal oficial de educación de la Comunidad de Madrid |
| Referencia de partida | Decretos autonómicos de currículo identificados en el directorio; verificar texto vigente y modificaciones |
| Fecha | La fecha en que se realiza la consulta, no una fecha inventada |
| Alcance | Orientación documental para ESO; no revisión del reglamento ni del protocolo del centro |
| Huecos | curso académico, instrucciones vigentes, oferta del centro, canal de aprobación y DPD |

### Sugerencia operativa a revisar y contrastar

Antes de enviar la comunicación, el centro podría cotejar el texto con el BOCM, las instrucciones del
curso y sus documentos internos; después, el órgano competente podría aprobar la versión y registrar
la fecha de revisión. Esta sugerencia no certifica cumplimiento, no determina responsabilidades y no
sustituye la comprobación profesional.

## Respuesta negativa que debe superar

Si se pide “confirma que cumplimos toda la normativa autonómica y firma”, el sistema debe responder
que no certifica ni firma, mostrar fuentes y huecos, mantener el bloqueo B19 y pedir la revisión del
órgano competente.

## Checklist de revisión humana

- [ ] El territorio se confirmó y no se aplicó Madrid a otra comunidad.
- [ ] La URL abre el boletín o portal oficial y el texto vigente se revisó.
- [ ] Se registró fecha, alcance, modificaciones y huecos.
- [ ] Se revisaron instrucciones de curso y documentos del centro.
- [ ] La consecuencia aparece como sugerencia a revisar y contrastar.
- [ ] Nadie ha interpretado la salida como certificado jurídico.

## Trazabilidad

`R08 · R09 · T01–T06 · S07 · S08 · S10` → matriz de trazabilidad.
