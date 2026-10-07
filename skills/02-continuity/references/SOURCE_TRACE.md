# Source trace

- Source reference skill: `skills/02-continuity/SKILL.md`
- Source manifest: `skills/02-continuity/manifest.yaml`
- Source identity/version: `tab2.continuity-and-canon` / `1.0.0`
- Distribution package status: web reference only; no production registration.

## Production implementation

- `application/screenwriter_intelligence/full_story_continuity.py`
- `application/screenwriter_intelligence/continuity_memory.py`
- `application/screenwriter_intelligence/screenplay_service.py`

## Source functions

- `FullStoryContinuityAnalyzer.analyze`
- `ScreenplayApplicationService.create_draft`

## Tests

- `tests/test_full_story_continuity_completeness.py`
- `tests/test_continuity_engine.py`
- `tests/test_story_memory_temporal_visibility.py`

## Architecture and contracts

- `architecture/TAB2_DATA_AUTHORITY.md`
- `architecture/TAB2_FROZEN_CONTRACTS.md`


This source trace is navigational evidence, not a replacement for reading the
implementation, test, or frozen registry.
