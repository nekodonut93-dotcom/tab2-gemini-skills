# Quality audit — portable stage excerpt

**Source package:** `skills/07-quality-audit/SKILL.md`  
**Stage owner:** Production frozen tests and deterministic validators; web checks are not production certification.

## Authority

Production frozen tests and deterministic validators; web checks are not production certification.

## Input/output boundary

- Input: All stage outputs, source refs, portable state, schemas, requested model/duration, and applicable frozen requirements.
- Output: quality_audit with status, failed_stage, reason, recommended_return_stage, checks, and refs.

## Safe advancement

- Validation: Use quality_audit schema and source-linked check results; preserve exact production contract identities. Portable Seedance review cannot certify PromptEngine output or Gemini model quality.
- Failure: Any unsupported content, authority conflict, future leak, invalid shape, or missing required evidence fails closed.
- Next: PASS completes only the portable review; otherwise return to recommended_return_stage and re-audit downstream stages.

This compact excerpt is for web distribution. The linked production code and
frozen tests remain authoritative.
