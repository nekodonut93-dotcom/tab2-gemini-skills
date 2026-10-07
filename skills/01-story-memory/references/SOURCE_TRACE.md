# Source trace

- Source reference skill: `skills/01-story-memory/SKILL.md`
- Source manifest: `skills/01-story-memory/manifest.yaml`
- Source identity/version: `tab2.story-memory-authority` / `1.0.0`
- Distribution package status: web reference only; no production registration.

## Production implementation

- `application/screenwriter_intelligence/story_memory.py`
- `application/screenwriter_intelligence/memory_models.py`
- `application/screenwriter_intelligence/story_memory_repository.py`

## Source functions

- `StoryMemoryService.ingest_chapter`
- `StoryMemoryService.build_context_package`
- `StoryMemoryService.build_relevant_canon_slice`

## Tests

- `tests/test_screenwriter_story_memory.py`
- `tests/test_story_memory_canonical_character_identity.py`
- `tests/test_story_memory_temporal_visibility.py`

## Architecture and contracts

- `architecture/TAB2_DATA_AUTHORITY.md`
- `architecture/WRITER_STORY_MEMORY_SEMANTIC_INTEGRATION.md`


This source trace is navigational evidence, not a replacement for reading the
implementation, test, or frozen registry.
