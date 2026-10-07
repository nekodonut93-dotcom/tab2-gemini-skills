# Source trace

- Source reference skill: `skills/06-prompt-engine/SKILL.md`
- Source manifest: `skills/06-prompt-engine/manifest.yaml`
- Source identity/version: `tab2.prompt-engine-syntax` / `1.0.0`
- Distribution package status: web reference only; no production registration.

## Production implementation

- `ai_agent_brain/prompt_assembly/prompt_engine.py`
- `application/prompt_facade.py`
- `ai_agent_brain/prompt_assembly/model_adapter.py`
- `model_profiles/`
- `prompt_templates/`

## Source functions

- `PromptEngine.assemble`
- `PromptFacade.compile`

## Tests

- `tests/test_prompt_engine.py`
- `tests/test_external_model_final_prompt.py`
- `tests/test_prompt_assembly.py`
- `tests/test_tab2_dynamic_duration_contract.py`

## Architecture and contracts

- `architecture/TAB2_MODEL_ADAPTERS.md`
- `architecture/TAB2_QUOTA_CACHE_RETRY.md`


This source trace is navigational evidence, not a replacement for reading the
implementation, test, or frozen registry.
