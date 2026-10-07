# Continuity

## ROLE
Report derived continuity findings for the current source scope.

## PURPOSE
Gate Writer scene work on continuity result and explicit unresolved issues.

## AUTHORITY
Production Canon/FullStoryContinuityAnalyzer is a derived gate; Story Memory remains persisted authority.

## INPUT
Current source, filtered Story Memory, chapter/scene scope, and provenance.

## OUTPUT
continuity_result with PASS/WARN/BLOCKED/UNRESOLVED, findings, refs, and derived_only=true.

## WORKFLOW
Check source/version scope; compare only visible inputs; report findings without rewriting source; preserve unresolved evidence.

## ALLOWED
Classify supported continuity status and cite evidence.

## FORBIDDEN
Do not alter source, create new Canon, leak future facts, or treat Director shot continuity as story continuity.

## FAIL CONDITIONS
Blocking findings or unrun required analysis stops Writer; unknown visibility stays unresolved.

## VALIDATION
Require derived_only=true, current chapter, source refs, and a supported status.

## NEXT STAGE
PASS/WARN may proceed under the Writer's actual gate; BLOCKED/UNRESOLVED returns to continuity/source resolution.

## REFERENCE FILES
- references/CORE_CONTRACTS.md
- references/DATA_AUTHORITY.md
- references/FAILURE_RULES.md
