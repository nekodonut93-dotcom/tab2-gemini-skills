# Gemini Web safe-stop example

This is a reference example based on the checked-in empty
`dist/common/project-template/PROJECT_STATE.json`. It is not a live Gemini
result or production acceptance test.

## Input state

- `project_id` is `UNRESOLVED`.
- `current_chapter_order` and `current_scene_id` are null.
- `source_document_refs` is empty.
- `visibility_filter_status` is `UNRESOLVED`.
- The current stage is `INGEST`.

## Expected safe behavior

1. Do not invent a story, source reference, chapter, scene, or identity.
2. Do not run Writer, Director, or PromptEngine stages using the empty state.
3. Report the unresolved project/source/scope inputs and keep the result
   non-successful until authoritative source material and scope are supplied.
4. Do not claim production validation: the portable state and Gemini Web
   response cannot invoke the production services.

The stop condition follows the checked-in portable failure rules and state
template. It does not define a new production status transition.
