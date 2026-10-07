# Copyable prompt sheet contract

`sheet_export.schema.json` defines portable JSON rows. CSV columns use this
exact order:

`Prompt ID, Chapter, Scene ID, Shot ID, Duration, Model, Platform, Style, Reference Images, Prompt, Negative Constraints, Status, Revision`

Serialize list-valued cells as JSON strings so commas/newlines inside prompt
text do not create ambiguous columns. XLSX-ready output is the same ordered
structured row data before cell serialization. This skill does not call Google
Sheets or another external spreadsheet API.

Only export one row per prompt/shot. Keep `STYLE_UNRESOLVED`,
`REFERENCE_BINDING_UNVERIFIED`, `BLOCKED`, and `UNRESOLVED` rows non-copyable
as production prompts; their `prompt` value must be empty.
