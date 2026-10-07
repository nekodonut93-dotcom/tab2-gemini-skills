# Writer WHAT and official screenplay ownership

Use this reference when preserving source story semantics through screenplay
generation and handoff.

- Writer owns events, identity, chronology, dialogue, relationships, props,
  location facts, motivation and outcome.
- `ScreenplayApplicationService` owns official screenplay creation, mutation
  and validation in the Professional flow.
- A deterministic adaptation is a source-backed screenplay projection, not a
  new Story Memory fact or Director decision.
- Preserve exact source dialogue and source references.
- Do not infer unresolved story state or pass an unready screenplay to Director.

## Implementation and tests

- Runtime: `application/screenwriter_intelligence/professional_writer_workflow.py`,
  `screenplay_service.py`, `writer_provider.py`, `writer_maturity_service.py`
- Functions: `ProfessionalScreenwriterWorkflow.process`,
  `ScreenplayApplicationService.create_draft`,
  `DeterministicWriterProvider.adapt_scene`,
  `WriterMaturityService.readiness`
- Tests: `tests/test_writer_screen_adaptation.py`,
  `tests/test_writer_outcome_context_e2e.py`,
  `tests/test_writer_frozen_contracts.py`,
  `tests/test_professional_writer_workflow.py`
- Architecture: `architecture/TAB2_DATA_AUTHORITY.md`,
  `architecture/TAB2_FROZEN_CONTRACTS.md`
