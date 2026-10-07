# Source trace

- Source reference skill: `skills/05-director/SKILL.md`
- Source manifest: `skills/05-director/manifest.yaml`
- Source identity/version: `tab2.director-cinematic-how` / `1.0.0`
- Distribution package status: web reference only; no production registration.

## Production implementation

- `application/director_facade.py`
- `application/director_reasoning/`
- `application/director_workflow/`
- `application/director_knowledge/`
- `application/director_intelligence/`
- `application/skill_intelligence_router/`
- `application/skill_context_injection/`

## Source functions

- `DirectorFacade`
- `DirectorWorkflowService`

## Tests

- `tests/test_director_frozen_contracts.py`
- `tests/test_director_workflow.py`
- `tests/test_director_quality_facade.py`

## Architecture and contracts

- `architecture/TAB2_DIRECTOR_ARCHITECTURE.md`
- `architecture/TAB2_FROZEN_CONTRACTS.md`
- `architecture/writer_contract_freeze_v1.json`
- `architecture/director_contract_freeze_v1.json`

This source trace is navigational evidence, not a replacement for reading the
implementation, test, or frozen registry.
