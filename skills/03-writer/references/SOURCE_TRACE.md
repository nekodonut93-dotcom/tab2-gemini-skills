# Source trace

- Source reference skill: `skills/03-writer/SKILL.md`
- Source manifest: `skills/03-writer/manifest.yaml`
- Source identity/version: `tab2.writer-what` / `1.0.0`
- Distribution package status: web reference only; no production registration.

## Production implementation

- `application/screenwriter_intelligence/professional_writer_workflow.py`
- `application/screenwriter_intelligence/screenplay_service.py`
- `application/screenwriter_intelligence/writer_provider.py`
- `application/screenwriter_intelligence/writer_maturity_service.py`

## Source functions

- `ProfessionalScreenwriterWorkflow.process`
- `ScreenplayApplicationService.create_draft`
- `DeterministicWriterProvider.adapt_scene`

## Tests

- `tests/test_writer_screen_adaptation.py`
- `tests/test_writer_outcome_context_e2e.py`
- `tests/test_writer_frozen_contracts.py`
- `tests/test_professional_writer_workflow.py`

## Architecture and contracts

- `architecture/TAB2_DATA_AUTHORITY.md`
- `architecture/TAB2_FROZEN_CONTRACTS.md`
- `architecture/writer_contract_freeze_v1.json`
- `architecture/director_contract_freeze_v1.json`

This source trace is navigational evidence, not a replacement for reading the
implementation, test, or frozen registry.
