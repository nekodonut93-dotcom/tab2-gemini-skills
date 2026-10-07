# 05 Director — Gemini-facing portable stage reference

## ROLE

Select bounded, evidence-backed cinematic HOW for an accepted Writer scene.

## AUTHORITY

DirectorWorkflowService / Director FROZEN_V1; web index is reference-only and current store state is UNKNOWN.

## INPUT

Valid Writer scene, current visible context, model request, and Director INDEX lookup fields.

## OUTPUT

director_plan with selected concept IDs, framing/movement/blocking/pacing, model-adapter status, and source references.

## WORKFLOW

Writer Scene → Scene Feature Assessment → INDEX lookup → target 3-8 relevant records where supported (fewer when fewer apply; exceed eight only with scene-specific evidence) → compose HOW → record adapter and prompt-structure handoff.

## ALLOWED

Recommend subject-bound cinematic execution only; keep knowledge, model adapter, and prompt structure in separate records.

## FORBIDDEN

No Writer fact edits, new events, identity/location/dialogue changes, final prompt compilation, or promotion of UNKNOWN/DRAFT records.

## FAIL CONDITIONS

Invalid Writer scene, unsupported concept, unknown model compatibility, or evidence conflict blocks or leaves the field unresolved.

## VALIDATION

Keep source_reference on selections; enforce max eight selected concepts by default; exceed only with recorded evidence; preserve writer_what_unchanged=true.

## NEXT STAGE

Pass Director HOW and selected verified adapter facts to PROMPT ENGINE; do not load the whole catalog.

## REFERENCES

- references/CORE_CONTRACTS.md
- references/director_contract.md
- references/director_index.md
- references/director_prompt_structure.md

## STATUS


PORTABLE_GEMINI_REFERENCE_ONLY; source skill version 1.0.0; schema identity `DIRECTOR FROZEN_V1`. Not runtime-loaded.
