# Visual completion examples

All examples below are synthetic illustrations, not production acceptance
evidence. Each candidate requires current-scene support and source references
in an actual project.

## GOOD — vehicle arrival

Source: A character stands beside a road; a named vehicle stops in front.
Candidate: `head_turn_toward_explicit_motion`, origin
`SAFE_VISUAL_INFERENCE`, `changes_story_state: false`, anchored to the scene.

## BAD — emotional invention

Candidate: "She cries and decides to leave." This adds an unsupported emotion
and outcome; reject it.

## BLOCKED — unresolved actor

When the source uses an ambiguous pronoun and identity cannot be resolved,
return `UNRESOLVED`; do not assign the motion to a guessed character.
