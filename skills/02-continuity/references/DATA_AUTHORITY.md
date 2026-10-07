# Portable data authority

| Data | Authority | Web-package rule |
|---|---|---|
| Source chapters and references | User-provided source and provenance | Preserve exact references; do not silently rewrite |
| Character identity and explicit aliases | Existing Story Memory / Character Bible authority | Never guess identity or transliteration |
| Story facts and character knowledge | Persisted Story Memory, scoped by provenance and time | Filter before use; unknown visibility blocks |
| Production Canon | Derived analyzer report | Gate only; do not turn it into a new source |
| Screenplay scene WHAT | Writer | Director and prompt compilation are read-only |
| Cinematic HOW | Director | Must not add story facts |
| Model syntax and final prompt | Production PromptEngine | Keep adapter and structure concerns separate |
| Files under `dist/common/project-template/` | Portable web-only working state | Mark every document `PORTABLE_WEB_STATE_ONLY` |
| `PROJECT_VISUAL_PROFILE.json` | Explicit user-selected project preference | Keep separate from Story Memory; absent or unresolved profile blocks portable prompt drafting |

Production authorities, validators and persistence are not available merely
because a web model has read this package.
