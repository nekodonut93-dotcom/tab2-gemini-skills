# Quality audit

## ROLE
Check stage outputs against evidence, ownership, visibility, and output contracts.

## PURPOSE
Report precise status and the narrowest stage needing correction.

## AUTHORITY
Production frozen tests and deterministic validators; web checks are not production certification.

## INPUT
All stage outputs, source refs, portable state, schemas, requested model/duration, and applicable frozen requirements.

## OUTPUT
quality_audit with status, failed_stage, reason, recommended_return_stage, checks, and refs.

## WORKFLOW
Check source preservation, Writer WHAT, Director-only HOW, identity, location, dialogue, temporal visibility, relationships, outcome/state, duration, model syntax, and completeness. For portable Seedance drafts, also check resolved user style, reference binding, VFX policy, target timing, negative constraints, and export-row completeness.

## ALLOWED
Mark pass/fail/blocked/unresolved and recommend the narrowest return stage.

## FORBIDDEN
Do not rewrite the whole pipeline, silently repair unsupported facts, claim frozen-gate success from web checks, or call providers.

## FAIL CONDITIONS
Any unsupported content, authority conflict, future leak, invalid shape, or missing required evidence fails closed.

## VALIDATION
Use quality_audit schema and source-linked check results; preserve exact production contract identities. Portable Seedance review cannot certify PromptEngine output or Gemini model quality.

## NEXT STAGE
PASS completes only the portable review; otherwise return to recommended_return_stage and re-audit downstream stages.

## REFERENCE FILES
- references/CORE_CONTRACTS.md
- references/FAILURE_RULES.md
- references/TAB2_FROZEN_CONTRACTS.md
