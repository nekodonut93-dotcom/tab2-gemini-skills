# Long-novel orchestration — portable stage excerpt

**Source package:** `skills/00-orchestrator/SKILL.md`  
**Stage owner:** The current stage's source authority and its validated result; this orchestrator has no story or creative authority.

## Authority

The current stage's source authority and its validated result; this orchestrator has no story or creative authority.

## Input/output boundary

- Input: Portable project state, current stage, current chapter/scene, previous result, and source refs.
- Output: Stage decision with status, failed_stage, reason, and next_stage or recommended_return_stage.

## Safe advancement

- Validation: Check prior stage status, source refs, visibility markers, output schema, required gate result, and explicit project-profile status. No inference from file order, story genre, or timestamps.
- Failure: Missing or invalid output, blocked continuity/readiness, unknown visibility, incompatible model surface, unresolved identity, or STYLE_UNRESOLVED blocks Gemini portable video-prompt advancement.
- Next: Advance in the declared order; on failure return only to the responsible stage and retain accepted upstream outputs. If Gemini portable project style is unresolved, ask the user and stop before Writer/Director prompt work.

This compact excerpt is for web distribution. The linked production code and
frozen tests remain authoritative.
