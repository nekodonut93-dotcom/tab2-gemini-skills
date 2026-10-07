# Source trace

- Source reference skill: `skills/04-enrichment/SKILL.md`
- Source manifest: `skills/04-enrichment/manifest.yaml`
- Source identity/version: `tab2.writer-enrichment` / `1.0.0`
- Distribution package status: web reference only; no production registration.

## Production implementation

- `application/screenwriter_intelligence/writer_provider.py`
- `application/screenwriter_intelligence/screenplay_service.py`
- `application/screenwriter_intelligence/story_reasoning.py`
- `application/screenwriter_intelligence/story_memory.py`

## Source functions

- `DeterministicWriterProvider.enrich_official_scene`
- `_visual_enrichment_rejection`
- `StoryMemoryService.build_action_actor_aliases`

## Tests

- `tests/test_writer_scene_action_enrichment.py`
- `tests/test_writer_action_grounding_benchmark.py`

## Architecture and contracts

- `architecture/SCENE_ACTION_ENRICHMENT.md`
- `architecture/TAB2_FROZEN_CONTRACTS.md`
- `architecture/writer_contract_freeze_v1.json`
- `architecture/director_contract_freeze_v1.json`

This source trace is navigational evidence, not a replacement for reading the
implementation, test, or frozen registry.
