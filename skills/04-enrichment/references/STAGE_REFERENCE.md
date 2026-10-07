# Evidence-bounded enrichment — portable stage excerpt

**Source package:** `skills/04-enrichment/SKILL.md`  
**Stage owner:** Existing Writer enrichment proposal plus deterministic production grounding/acceptance boundary.

## Authority

Existing Writer enrichment proposal plus deterministic production grounding/acceptance boundary.

## Input/output boundary

- Input: Current official Writer scene, bound evidence, visible character identities, source refs, and scope.
- Output: enrichment_result with ACCEPT/NONE/BLOCKED/UNRESOLVED/REJECTED, candidate actions, refs, and story_state_unchanged=true.

## Safe advancement

- Validation: Check enrichment_result schema, refs, unchanged story state, and every candidate against the permanent BASELINE_V1 philosophy.
- Failure: Ambiguous actor, unsupported action/object/location, missing evidence, or state change is rejected or unresolved; do not guess.
- Next: ACCEPT or NONE proceeds to DIRECTOR; BLOCKED/UNRESOLVED returns to the narrow evidence/Writer stage.

This compact excerpt is for web distribution. The linked production code and
frozen tests remain authoritative.
