# Tab 2 model profiles, templates and prompt syntax

## Current formatting path

`PromptEngine` validates semantic context and produces a blueprint;
`PromptAssembler` selects a JSON template; `StructuredModelAdapter` compiles
natural-language clauses. Profiles express model capability/configuration,
while templates control assembly section order. Neither creates a video job.
Tab 2 returns prompt text for user display/copy.

## Evidence-backed model surfaces

| Model | Profile | Prompt template | Adapter registry | Finding |
|---|---|---|---|---|
| Seedance | present | present | present; explicit camera-phrase branch | active formatting path |
| Veo | present | present | present | active formatting path |
| Kling | present | present | present | active formatting path; explicit test |
| Sora | present | **missing** | registry entry exists | assembly failure risk because TemplateManager requires `{model_id}.json`; test coverage not established |
| Runway / Luma / Pika / LTX / MiniMax | various skill/capability references; not uniformly prompt profiles | no checked-in template found by this audit | no established PromptEngine formatter surface beyond the documented registry | do not infer a PromptEngine adapter from a Skill compatibility list |

`model_profiles/seedance.json` audio evidence is guidance-only; it does not
establish native generation API capability. Director knowledge adapter records
for Seedance/Veo/MiniMax were DRAFT/REVIEW_PENDING, not active verified
capability authority in this audit.

## Scope separation

- **Profile:** model capability/option data; no creative authority.
- **Template:** ordering/configuration of `PromptSection`s; not a public Writer
  or Director schema.
- **StructuredModelAdapter:** transforms typed semantic input into prose and
  handles explicitly model-specific formatting.
- **Director:** generic semantic HOW; no API parameter, provider tag, or final
  prompt syntax.
- **Renderer/provider dispatch:** not performed by PromptEngine's model
  formatter.

## Versioning gap

`PromptLanguageRenderer` has `prompt-language-renderer-v1` in its cache
identity. StoryReasoning has explicit prompt/schema identities. The inventory
did not find PromptEngine language-render cache identity including explicit
adapter/template/model-profile versions. Treat this as a cache invalidation
review item, not a behavior change in this phase.

No Sora template, template fallback, or model-adapter behavior was added.
Related regression coverage:
`tests/test_prompt_engine.py`, `tests/test_external_model_final_prompt.py`,
`tests/test_prompt_assembly.py`, `tests/test_tab2_dynamic_duration_contract.py`.
