# Source trace

- Source reference skill: `skills/00-orchestrator/SKILL.md`
- Source manifest: `skills/00-orchestrator/manifest.yaml`
- Source identity/version: `tab2.orchestrator-boundaries` / `1.1.0`
- Distribution package status: web reference only; no production registration.

## Production implementation

- `application/professional_canonical_pipeline.py`
- `application/runtime/application_factory.py`
- `application/api/routes.py`
- `ui/application-adapter.js`

## Source functions

- `ProfessionalCanonicalPipelineService.execute`
- `ApplicationFactory.create`

## Tests

- `tests/test_tab2_canonical_pipeline_phase1.py`
- `tests/test_professional_writer_workflow.py`
- `tests/test_tab2_output_projection_phase2.py`

## Architecture and contracts

- `architecture/TAB2_CALL_GRAPH.md`
- `architecture/TAB2_DATA_AUTHORITY.md`
- `architecture/writer_contract_freeze_v1.json`
- `architecture/director_contract_freeze_v1.json`

This source trace is navigational evidence, not a replacement for reading the
implementation, test, or frozen registry.
