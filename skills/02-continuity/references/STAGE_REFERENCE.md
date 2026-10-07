# Continuity — portable stage excerpt

**Source package:** `skills/02-continuity/SKILL.md`  
**Stage owner:** Production Canon/FullStoryContinuityAnalyzer is a derived gate; Story Memory remains persisted authority.

## Authority

Production Canon/FullStoryContinuityAnalyzer is a derived gate; Story Memory remains persisted authority.

## Input/output boundary

- Input: Current source, filtered Story Memory, chapter/scene scope, and provenance.
- Output: continuity_result with PASS/WARN/BLOCKED/UNRESOLVED, findings, refs, and derived_only=true.

## Safe advancement

- Validation: Require derived_only=true, current chapter, source refs, and a supported status.
- Failure: Blocking findings or unrun required analysis stops Writer; unknown visibility stays unresolved.
- Next: PASS/WARN may proceed under the Writer's actual gate; BLOCKED/UNRESOLVED returns to continuity/source resolution.

This compact excerpt is for web distribution. The linked production code and
frozen tests remain authoritative.
