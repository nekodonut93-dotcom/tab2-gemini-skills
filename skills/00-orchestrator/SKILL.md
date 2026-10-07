# 00 Orchestrator — Gemini-facing portable stage reference

## ROLE

Coordinate the existing stages; never do a child stage's work.

## AUTHORITY

The current stage's source authority and its validated result; this orchestrator has no story or creative authority.

## INPUT

Portable project state, current stage, current chapter/scene, previous result, and source refs.

## OUTPUT

Stage decision with status, failed_stage, reason, and next_stage or recommended_return_stage.

## WORKFLOW

INGEST → STORY MEMORY → CONTINUITY → WRITER → ENRICHMENT → DIRECTOR → PROMPT ENGINE → QUALITY AUDIT. Enrichment may return NONE. For Gemini portable video-prompt work, resolve the user's project visual preference before Writer/Director prompt work. Stop at first invalid required stage.

## ALLOWED

Select the next stage, pass only visible/evidenced inputs, check the named output schema, and report a narrow return stage.

## FORBIDDEN

Do not ingest facts, analyze continuity, write scenes, enrich actions, direct shots, compile final prompts, or override stage authority.

## FAIL CONDITIONS

Missing or invalid output, blocked continuity/readiness, unknown visibility, incompatible model surface, unresolved identity, or STYLE_UNRESOLVED blocks Gemini portable video-prompt advancement.

## VALIDATION

Check prior stage status, source refs, visibility markers, output schema, required gate result, and explicit project-profile status. No inference from file order, story genre, or timestamps.

## NEXT STAGE

Advance in the declared order; on failure return only to the responsible stage and retain accepted upstream outputs. If Gemini portable project style is unresolved, ask the user and stop before Writer/Director prompt work.

## REFERENCES

- references/TAB2_WORKFLOW.md
- references/CORE_CONTRACTS.md
- references/OUTPUT_SCHEMAS.md

## STATUS


PORTABLE_GEMINI_REFERENCE_ONLY; source skill version 1.1.0; schema identity `DirectorHandoffV2`. Not runtime-loaded.
