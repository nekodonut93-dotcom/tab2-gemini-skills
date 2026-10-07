# Director cinematic HOW

Use this reference for source-backed Director ownership and the typed cinematic
planning vocabulary. Director produces structured HOW; it does not own story
WHAT, model-specific prompt syntax, final prompt assembly or renderer dispatch.

- Prefer validated `DirectorHandoffV2` and current Writer screenplay state.
- Treat Skills and knowledge as advisory inputs subject to production approval,
  compatibility, precedence, provenance and currentness checks.
- Do not treat the offline `INDEX.yaml` as a production router.
- Do not promote draft knowledge packages, unverified Skill-store entries or
  model-adapter records.
- Keep unsupported selectors unknown; never infer a model capability from a
  compatibility list.

The index maps source-backed concept families. It does not introduce new
Director semantics or alter `DIRECTOR FROZEN_V1`.

## Implementation and tests

- Runtime: `application/director_reasoning/`,
  `application/director_workflow/`, `application/director_knowledge/`,
  `application/director_intelligence/`,
  `application/skill_intelligence_router/`,
  `application/skill_context_injection/`
- Tests: `tests/test_director_frozen_contracts.py`,
  `tests/test_director_workflow.py`, `tests/test_director_facade.py`
- Architecture: `architecture/TAB2_DIRECTOR_ARCHITECTURE.md`,
  `architecture/TAB2_FROZEN_CONTRACTS.md`

Current persisted Skill-store contents/version/activation were not inspected;
the exact active Skill count is UNKNOWN.
