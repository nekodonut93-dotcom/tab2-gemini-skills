# 01 Story Memory — Gemini-facing portable stage reference

## ROLE

Present only persisted, source-backed facts and identity with their visibility boundaries.

## AUTHORITY

Production StoryMemoryService/Character Bible remain authoritative; portable state is not production memory.

## INPUT

Current chapter/scene, source refs, character IDs, and Story Memory records with visibility and provenance.

## OUTPUT

story_memory_state with filtered visible_facts, visible_knowledge, characters, relationships, source_refs, and filter status.

## WORKFLOW

Validate record identity and source refs; apply current chapter/scene and known-by-character visibility; exclude future/superseded records; mark unknowns unresolved.

## ALLOWED

Filter and report explicitly visible records; preserve evidenced aliases and identity refs.

## FORBIDDEN

Do not invent facts/aliases, merge characters, promote a derived report to Canon, or infer character knowledge.

## FAIL CONDITIONS

Missing, ambiguous, future, superseded, or unknown visibility is BLOCKED/UNRESOLVED and must not be passed downstream.

## VALIDATION

Require source_refs and explicit visibility for each fact/knowledge record; one canonical identity only where existing authority resolves it.

## NEXT STAGE

Pass filtered context to CONTINUITY; do not pass raw future records.

## REFERENCES

- references/CORE_CONTRACTS.md
- references/DATA_AUTHORITY.md
- references/TAB2_WORKFLOW.md

## STATUS


PORTABLE_GEMINI_REFERENCE_ONLY; source skill version 1.0.0; schema identity `Story Memory semantic v1`. Not runtime-loaded.
