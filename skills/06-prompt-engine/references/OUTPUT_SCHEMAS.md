# Portable output schemas

JSON Schema files in `schemas/` are web-distribution exchange shapes:

- `story_memory_state.schema.json`
- `continuity_result.schema.json`
- `writer_scene.schema.json`
- `enrichment_result.schema.json`
- `director_plan.schema.json`
- `prompt_package.schema.json`
- `quality_audit.schema.json`
- `project_visual_profile.schema.json`

They intentionally identify themselves as portable and do not replace
production schemas, Writer FROZEN_V1, DIRECTOR FROZEN_V1, or DirectorHandoffV2.
Unknown fields are tolerated unless they violate an explicit forbidden-field
rule. `UNKNOWN` visibility is never equivalent to current visibility.
