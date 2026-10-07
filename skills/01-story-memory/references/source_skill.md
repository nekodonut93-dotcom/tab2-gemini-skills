# Story Memory authority and temporal context

Use this reference to explain persisted Story Memory and scoped context to
Writer or reasoning consumers.

- Treat Story Memory records as persisted, project-scoped source authority.
- Preserve character identity and explicit known aliases; never infer a
  transliteration or merge ambiguous people.
- Preserve source references, document/chapter revisions and temporal
  visibility. Future facts are not visible merely because they exist in storage.
- Keep Canon, draft changes, character knowledge and derived reports distinct.
- Use the service/repository query boundary; this document cannot authorize
  reads, writes, alias resolution or promotion to Canon.

## Implementation and tests

- Runtime: `application/screenwriter_intelligence/story_memory.py`,
  `memory_models.py`, `story_memory_repository.py`
- Functions: `StoryMemoryService.ingest_chapter`,
  `build_context_package`, `build_relevant_canon_slice`,
  `build_action_actor_aliases`
- Tests: `tests/test_screenwriter_story_memory.py`,
  `tests/test_story_memory_canonical_character_identity.py`,
  `tests/test_story_memory_temporal_visibility.py`
- Architecture: `architecture/TAB2_DATA_AUTHORITY.md`,
  `architecture/TAB2_FROZEN_CONTRACTS.md`
