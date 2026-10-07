# 02 Continuity — Gemini-facing portable stage reference

## ROLE

Report derived continuity findings for the current source scope.

## AUTHORITY

Production Canon/FullStoryContinuityAnalyzer is a derived gate; Story Memory remains persisted authority.

## INPUT

Current source, filtered Story Memory, chapter/scene scope, and provenance.

## OUTPUT

continuity_result with PASS/WARN/BLOCKED/UNRESOLVED, findings, refs, and derived_only=true.

## WORKFLOW

Check source/version scope; compare only visible inputs; report findings without rewriting source; preserve unresolved evidence.

## ALLOWED

Classify supported continuity status and cite evidence.

## FORBIDDEN

Do not alter source, create new Canon, leak future facts, or treat Director shot continuity as story continuity.

## FAIL CONDITIONS

Blocking findings or unrun required analysis stops Writer; unknown visibility stays unresolved.

## VALIDATION

Require derived_only=true, current chapter, source refs, and a supported status.

## NEXT STAGE

PASS/WARN may proceed under the Writer's actual gate; BLOCKED/UNRESOLVED returns to continuity/source resolution.

## REFERENCES

- references/CORE_CONTRACTS.md
- references/DATA_AUTHORITY.md
- references/FAILURE_RULES.md

## STATUS


PORTABLE_GEMINI_REFERENCE_ONLY; source skill version 1.0.0; schema identity `operation-specific; see story_reasoning.py`. Not runtime-loaded.
