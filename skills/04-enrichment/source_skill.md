# Evidence-bounded enrichment

## ROLE
Offer optional, evidence-grounded visible presentation detail without changing story state.

## PURPOSE
Add a safe visual action only when directly supported; otherwise return NONE.

## AUTHORITY
Existing Writer enrichment proposal plus deterministic production grounding/acceptance boundary.

## INPUT
Current official Writer scene, bound evidence, visible character identities, source refs, and scope.

## OUTPUT
enrichment_result with ACCEPT/NONE/BLOCKED/UNRESOLVED/REJECTED, candidate actions, refs, and story_state_unchanged=true.

## WORKFLOW
Check source evidence and actor resolution; identify optional directly supported visual action; if none is safe return NONE; never force an action.

## ALLOWED
Presentation-only action grounded in current source; reuse only identities, props, and locations already evidenced.

## FORBIDDEN
No emotion-to-fixed-gesture mapping; no new event/prop/location/dialogue/future knowledge/relationship escalation/outcome or state change.

## FAIL CONDITIONS
Ambiguous actor, unsupported action/object/location, missing evidence, or state change is rejected or unresolved; do not guess.

## VALIDATION
Check enrichment_result schema, refs, unchanged story state, and every candidate against the permanent BASELINE_V1 philosophy.

## NEXT STAGE
ACCEPT or NONE proceeds to DIRECTOR; BLOCKED/UNRESOLVED returns to the narrow evidence/Writer stage.

## REFERENCE FILES
- references/CORE_CONTRACTS.md
- references/FAILURE_RULES.md
- references/TAB2_WORKFLOW.md
