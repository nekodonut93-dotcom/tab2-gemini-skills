# PromptEngine and model-specific prompt syntax

Use this reference for the final-prompt compilation boundary. Director provides
generic semantic HOW; PromptEngine validates semantic context, builds the
prompt blueprint and compiles final text. Prompt rendering is not video
generation or provider dispatch.

- Use the canonical PromptFacade → PromptEngine → PromptAssembler /
  StructuredModelAdapter path.
- Keep profiles (capabilities/options), templates (section layout), and
  adapters (semantic-to-prose formatting) distinct.
- Keep model-specific syntax in model adapter/template data, never Director
  core concepts or Writer contracts.
- Do not infer an adapter from a Skill compatibility list.
- Sora has a profile and adapter registry entry but no checked-in template;
  assembly risk is documented, not fixed by this package.
- The PromptLanguageRenderer cache does not include explicit template,
  adapter, or profile versions in its identity in the audited implementation.
  Treat this as a review gap, not permission to change cache semantics here.

## Implementation and tests

- Runtime: `ai_agent_brain/prompt_assembly/`,
- Profiles/templates: `model_profiles/`, `prompt_templates/`
- Facade: `application/prompt_facade.py`
- Tests: `tests/test_prompt_engine.py`,
  `tests/test_external_model_final_prompt.py`,
  `tests/test_prompt_assembly.py`,
  `tests/test_tab2_dynamic_duration_contract.py`
- Architecture: `architecture/TAB2_MODEL_ADAPTERS.md`,
  `architecture/TAB2_QUOTA_CACHE_RETRY.md`
