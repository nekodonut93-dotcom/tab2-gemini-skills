# Director — portable stage excerpt

**Source package:** `skills/05-director/SKILL.md`  
**Stage owner:** DirectorWorkflowService / Director FROZEN_V1; web index is reference-only and current store state is UNKNOWN.

## Authority

DirectorWorkflowService / Director FROZEN_V1; web index is reference-only and current store state is UNKNOWN.

## Input/output boundary

- Input: Valid Writer scene, current visible context, model request, and Director INDEX lookup fields.
- Output: director_plan with selected concept IDs, framing/movement/blocking/pacing, model-adapter status, and source references.

## Safe advancement

- Validation: Keep source_reference on selections; enforce max eight selected concepts by default; exceed only with recorded evidence; preserve writer_what_unchanged=true.
- Failure: Invalid Writer scene, unsupported concept, unknown model compatibility, or evidence conflict blocks or leaves the field unresolved.
- Next: Pass Director HOW and selected verified adapter facts to PROMPT ENGINE; do not load the whole catalog.

This compact excerpt is for web distribution. The linked production code and
frozen tests remain authoritative.
