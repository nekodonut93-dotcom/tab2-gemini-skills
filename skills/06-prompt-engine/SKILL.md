# 06 Prompt Engine — Gemini-facing portable stage reference

## ROLE

Assemble validated Writer WHAT and Director HOW into a structured prompt package.

## AUTHORITY

Production PromptFacade → PromptEngine is the sole production final-assembly authority.

## INPUT

Writer scene, Director plan, verified model adapter, prompt structure, and language preference.

## OUTPUT

prompt_package with linked inputs, structured sections, final_prompt if supported, validation warnings, and refs.

## WORKFLOW

Validate immutable Writer scene; add Director HOW; check model status and structure; assemble sections; report unsupported fields instead of inventing.

## ALLOWED

Format supplied semantic content and preserve Writer WHAT.

## FORBIDDEN

Do not reason story again, change events/dialogue/location/relationships/outcome, invent details, or dispatch media generation.

## FAIL CONDITIONS

Missing input, unsupported/unverified adapter, incomplete required structure, or Writer WHAT drift blocks output.

## VALIDATION

Check references, writer_what_preserved=true, duration if required by supplied contract, model syntax evidence, and prompt completeness.

## NEXT STAGE

Send package to QUALITY AUDIT; Sora remains UNVERIFIED / INCOMPLETE because no checked-in production template was found.

## REFERENCES

- references/CORE_CONTRACTS.md
- references/model_adapters.md
- references/director_prompt_structure.md
- references/TAB2_MODEL_ADAPTERS.md

## STATUS


PORTABLE_GEMINI_REFERENCE_ONLY; source skill version 1.0.0; schema identity `PromptEngine input/output contracts; see frozen and PromptEngine tests`. Not runtime-loaded.
