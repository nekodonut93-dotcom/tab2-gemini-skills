# Continuity and Production Canon

Use this reference to understand how deterministic continuity state, source
evidence, and derived Production Canon gates interact.

- Story Memory persists source-backed facts and temporal scope.
- `FullStoryContinuityAnalyzer` creates a derived report and source-bound
  overlay; it does not rewrite source text.
- Required analysis/reread/readiness gates remain executable code.
- Writer story continuity is not Director shot continuity.
- A later-scene fact, scene probe, or Skill statement cannot bypass temporal
  visibility or establish a Canon fact.

## Implementation and tests

- Runtime: `application/screenwriter_intelligence/full_story_continuity.py`,
  `continuity_memory.py`, `screenplay_service.py`
- Functions: `FullStoryContinuityAnalyzer.analyze`,
  `StoryMemoryService.get_scene_context`,
  `ScreenplayApplicationService.create_draft`
- Tests: `tests/test_full_story_continuity_completeness.py`,
  `tests/test_continuity_engine.py`,
  `tests/test_story_memory_temporal_visibility.py`
- Architecture: `architecture/TAB2_DATA_AUTHORITY.md`,
  `architecture/WRITER_STORY_MEMORY_SEMANTIC_INTEGRATION.md`
