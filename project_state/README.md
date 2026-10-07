# Portable project state

All templates use `PORTABLE_WEB_STATE_ONLY`. `PROJECT_VISUAL_PROFILE.json` is
a user preference separate from `STORY_MEMORY.json`; the initial style status
is unresolved. `PROJECT_LANGUAGE_PROFILE.json` separately holds user-selected
technical prompt, dialogue, monologue and voice-over language preferences.
Project files are user-managed Gemini working state, not production
persistence or Story Memory.

Collection schemas intentionally remain permissive for record internals
because the production project templates do not define a frozen per-record
DTO for every file. Use the linked production authority and source references;
do not infer missing fields as facts.
