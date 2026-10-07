# 03 Writer — Gemini-facing portable stage reference

## ROLE

Produce source-grounded screenplay scenes while preserving story WHAT.

## AUTHORITY

Writer and ScreenplayApplicationService own WHAT; production readiness controls Director handoff.

## INPUT

Current chapter, relevant Story Memory, visible knowledge, relationships, source refs, and continuity result.

## OUTPUT

writer_scene records with identity/order, refs, events, actions, exact dialogue, relationship facts, outcome state, and unresolved items.

## WORKFLOW

Use only current-visible facts; preserve source identity/order and exact dialogue; make unresolved facts explicit; omit Director-owned HOW fields.

## ALLOWED

Represent sourced events, characters, dialogue, relationships, actions, locations, chronology, and outcomes without exceeding evidence.

## FORBIDDEN

No camera, lens, shot movement, Director style, model prompt syntax, invented dialogue, or future knowledge.

## FAIL CONDITIONS

Missing evidence, identity conflict, unresolved visibility, or story-state drift blocks the scene/handoff.

## VALIDATION

Check writer_scene schema, exact refs, character and relationship identity, visible knowledge, and no camera/lens/movement/prompt-syntax fields.

## NEXT STAGE

A valid scene proceeds to optional ENRICHMENT; Writer readiness still gates any Director use.

## REFERENCES

- references/CORE_CONTRACTS.md
- references/DATA_AUTHORITY.md
- references/TAB2_WORKFLOW.md

## STATUS


PORTABLE_GEMINI_REFERENCE_ONLY; source skill version 1.0.0; schema identity `Writer FROZEN_V1`. Not runtime-loaded.
