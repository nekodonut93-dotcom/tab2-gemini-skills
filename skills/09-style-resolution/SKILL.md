# 09 Style Resolution — Gemini-facing portable reference

## ROLE

Resolve explicit user visual preference before portable video-prompt drafting.

## AUTHORITY

User preference only; PROJECT_VISUAL_PROFILE is not Story Memory, Canon, Writer WHAT, Director HOW, or PromptEngine authority.

## INPUT

Project state, existing project profile, and explicit user selections.

## OUTPUT

Resolved PROJECT_VISUAL_PROFILE or STYLE_UNRESOLVED question.

## WORKFLOW

Read profile; if unresolved ask user; persist only explicit choice; default full_chibi_scene to false; validate schema; reuse until user changes it.

## ALLOWED

Offer preset and user-controlled expression, comedy, monologue, chibi inserts, explicit full-scene chibi, VFX, camera and realism settings.

## FORBIDDEN

Infer style from story, genre, costume, language, emotion or model name.

## FAIL CONDITIONS

Missing required choice, invalid profile, or custom values not explicitly supplied.

## VALIDATION

Check profile schema, selected_by=USER, required resolved fields, revision and portable scope.

## NEXT STAGE

Only after resolved, pass profile read-only to the next portable stage; otherwise stop before prompt draft.

## REFERENCES

['style_questionnaire.yaml', 'style_presets.yaml', 'PROJECT_VISUAL_PROFILE.schema.json', 'tests/test_gemini_seedance_skill_contracts.py']

## STATUS


PORTABLE_GEMINI_REFERENCE_ONLY; source skill version 1.0.0; schema identity `PROJECT_VISUAL_PROFILE_V1`. Not runtime-loaded.
