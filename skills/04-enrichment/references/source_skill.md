# Evidence-bounded Writer enrichment

Use this reference only for the optional visual-enrichment stage after official
Canon completion and Writer reread.

- The reasoning provider proposes; deterministic gates and the existing
  ScreenplayService decide whether a derived action is applied.
- Enrichment may clarify visible expression, not invent plot, dialogue,
  relationship escalation, props, location, outcome or future knowledge.
- Keep exact evidence/source refs, scene reality layer and scene character
  authority. Unresolved actors fail closed.
- Do not bypass alias source authority, provider/schema validation or current
  screenplay persistence. Prompt prose is not the validation boundary.

## Production identity

Story reasoning uses `story-reasoning-v1:scene-visual-v1` and
`scene-visual-schema-v2`; provider, context, model, prompt and schema identity
participate in the existing cache path. Keep those existing identities stable
unless a separately reviewed migration requires otherwise.

## Implementation and tests

- Runtime: `application/screenwriter_intelligence/writer_provider.py`,
  `screenplay_service.py`, `story_reasoning.py`, `story_memory.py`
- Functions: `DeterministicWriterProvider.enrich_official_scene`,
  `_visual_enrichment_rejection`, `StoryMemoryService.build_action_actor_aliases`
- Tests: `tests/test_writer_scene_action_enrichment.py`,
  `tests/test_writer_action_grounding_benchmark.py`
- Fixture: `tests/fixtures/writer_action_grounding_baseline_v1.json`
- Architecture: `architecture/SCENE_ACTION_ENRICHMENT.md`,
  `architecture/TAB2_FROZEN_CONTRACTS.md`
