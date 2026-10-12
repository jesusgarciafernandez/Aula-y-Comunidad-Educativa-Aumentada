---
name: revisar-trabajo-con-feedback
description: Revisa un trabajo anonimizado con criterios explícitos y devuelve feedback formativo, sin nota y sin detección de IA.
---

# Revisar un trabajo con feedback formativo

Ejecuta `workflows/W04_revisar_trabajo.md` con `agentes/A04_revisor_formativo.md`.
**Derivación obligatoria a A06 y A10.**

## Cuándo se usa
«Revisa este trabajo», «dame feedback sobre esta redacción», «cómo puede mejorar este informe».

## Cuándo NO se usa — parada inmediata
- Si piden **nota**, puntuación o comparar y ordenar trabajos.
- Si piden saber **quién usó IA** o redactar una sanción.
- Si el trabajo llega **sin anonimizar**.
- Si piden inferir problemas personales, emocionales o familiares del autor.

En esos casos, explica el límite en una frase y ofrece lo que sí se puede hacer.

## Entradas obligatorias
1. Trabajo **anonimizado**.
2. Rúbrica o criterios explícitos. Si no existen, se crean antes con `crear-rubrica-formativa`.

## Pasos
1. Comprueba anonimización. Si hay datos personales: para, avisa, no los repitas, pide versión limpia.
2. Comprueba criterios. Sin criterios: bloquea y ofrece crearlos.
3. Lee entero antes de opinar.
4. Localiza evidencias concretas en el texto o producto.
5. Fortalezas observables + máximo **tres** mejoras prioritarias.
6. Preguntas para la persona autora.
7. Propuesta de siguiente intento, concreta y acotada.
8. Declara qué no puede evaluarse con este material.

## Contrato de salida
Criterios · evidencias · fortalezas · hasta 3 mejoras · preguntas · siguiente intento · qué no puede
evaluarse · validación docente pendiente. Plantilla: `plantillas/06_feedback_formativo.md`.
