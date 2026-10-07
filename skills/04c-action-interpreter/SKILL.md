# 04C Action Interpreter — Gemini-facing portable reference

## ROLE

Normalize source-backed literary action to a conservative semantic class.

## AUTHORITY

Writer action and source remain authoritative; classification is derived portable metadata.

## INPUT

Writer action, source references, current visible scene context, resolved actor.

## OUTPUT

Action class plus evidenced direction/target/contact and unresolved fields.

## WORKFLOW

Classify only the supported specificity; use GENERIC_SINGLE_SLASH only if a single slash is explicit; otherwise leave unresolved.

## ALLOWED

Classes in action_taxonomy.yaml for sword/fight, movement, driving, phone, eating, object, romance, and dialogue.

## FORBIDDEN

Unsupported target, direction, subtype, spin, jump, acrobatics, impact, magic, injury, or result.

## FAIL CONDITIONS

Unresolved actor/action or a classification requiring unsupported specificity.

## VALIDATION

Trace class to source/context; keep ambiguity explicit; do not change Writer WHAT.

## NEXT STAGE

Pass a resolved class to optional choreography; otherwise return UNRESOLVED.

## REFERENCES

['action_taxonomy.yaml', 'examples/README.md', 'tests/test_gemini_seedance_skill_contracts.py']

## STATUS


PORTABLE_GEMINI_REFERENCE_ONLY; source skill version 1.0.0; schema identity `ACTION_INTERPRETATION_V1`. Not runtime-loaded.
