# 04B Visual Completion — Gemini-facing portable reference

## ROLE

Propose bounded visible physical detail for a video-readable accepted scene.

## AUTHORITY

Writer owns WHAT; this package proposes presentation detail only. Production enrichment acceptance remains code-owned.

## INPUT

Accepted Writer scene, current visible context, resolved actor identity, source references, and project style preference.

## OUTPUT

Detail candidates labeled with origin, source references, and changes_story_state.

## WORKFLOW

Resolve the actor and visible scene context; select a context-supported candidate; reject state-changing detail.

## ALLOWED

Context-supported gaze, head movement, breathing, posture, position, weight shift, reaction pause, and secondary motion as proposals.

## FORBIDDEN

New event, dialogue, important prop, location, knowledge, relationship, injury, reveal, outcome, or fixed emotion-to-gesture mapping.

## FAIL CONDITIONS

Ambiguous actor/target, unknown visibility, missing evidence, or changes_story_state=true.

## VALIDATION

Check origin, source_refs, scene visibility, identity, and unchanged story state; do not claim production acceptance.

## NEXT STAGE

Pass accepted portable details to action interpretation/choreography or Director as read-only context; otherwise stop/return.

## REFERENCES

['safe_visual_inference.yaml', 'forbidden_story_inference.yaml', 'body_motion.yaml', 'gaze.yaml', 'reaction.yaml', 'secondary_motion.yaml', 'tests/test_writer_scene_action_enrichment.py', 'tests/test_writer_action_grounding_benchmark.py']

## STATUS


PORTABLE_GEMINI_REFERENCE_ONLY; source skill version 1.0.0; schema identity `VISUAL_COMPLETION_CANDIDATE_V1`. Not runtime-loaded.
