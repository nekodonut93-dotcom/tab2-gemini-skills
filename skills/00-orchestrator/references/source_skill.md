# Tab 2 orchestration boundaries

Use this reference when tracing a Professional Writer request from chapter
submission through Director prompt output. Keep the Writer request, later
Director-prompt request, and compatibility/quick routes distinct.

## Required boundaries

- Story Memory persists evidence; Production Canon is a derived gate.
- Writer produces WHAT and must pass readiness before Director.
- `DirectorHandoffV2` is the validated Writer/Director boundary.
- Director selects HOW; Skills only recommend.
- PromptFacade → PromptEngine is the sole final-prompt path.
- Renderer executes downstream artifacts; it does not author story semantics.
- `PROJECT_VISUAL_PROFILE` is a user preference kept outside Story Memory.
- In the portable Gemini workflow, resolve project visual style before starting
  Writer/Director video-prompt work. If absent, ask the user and stop with
  `STYLE_UNRESOLVED`; do not infer style from the novel.
- Visual completion, action interpretation and choreography are optional
  portable proposals between accepted Writer WHAT and Director HOW. They do
  not mutate the screenplay or extend production acceptance behavior.
- Seedance/Dola add-ons produce user-reviewable portable drafts only; do not
  claim PromptEngine compilation or invent Dola UI syntax.

Do not call providers or claim readiness based on this document. Follow the
runtime gates and tests linked below. This reference skill is model-neutral.

## Implementation and tests

- Runtime: `application/professional_canonical_pipeline.py`,
  `application/runtime/application_factory.py`,
  `application/api/routes.py`, `ui/application-adapter.js`
- Functions: `ProfessionalCanonicalPipelineService.execute`,
  `ApplicationFactory.create`, route dispatch and
  `generateProfessionalOutput`
- Tests: `tests/test_tab2_canonical_pipeline_phase1.py`,
  `tests/test_professional_writer_workflow.py`,
  `tests/test_tab2_output_projection_phase2.py`
- Architecture: `architecture/TAB2_CALL_GRAPH.md`,
  `architecture/TAB2_DATA_AUTHORITY.md`
