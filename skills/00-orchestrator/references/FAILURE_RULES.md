# Failure rules

Return a structured `BLOCKED`, `UNRESOLVED`, `REJECTED`, or `NONE` result
instead of fabricating a successful result when:

- source evidence or source references are absent or inconsistent;
- identity/alias resolution is ambiguous;
- a fact's chapter/scene visibility is absent, future, superseded, or unknown;
- continuity has a blocking result or has not run when required;
- a Writer proposal changes story WHAT or exact dialogue;
- enrichment would add an event, prop, location, dialogue, future knowledge,
  relationship escalation, or outcome/state change;
- Director input is not a valid Writer scene or asks Director to decide WHAT;
- a requested model adapter is unavailable/unverified;
- PromptEngine-required structure or output validation fails.

Quality failures do not trigger a silent whole-pipeline rewrite. Report
`status`, `failed_stage`, `reason`, and `recommended_return_stage`. Return to
the narrowest responsible earlier stage; preserve accepted upstream output.
