# Gemini Web to production regression map

This is a traceability map, not a substitute for running the tests. Paths are
repository-relative. A passing production test demonstrates only its tested
production behavior; it does not prove that Gemini Web reproduces it.

| Pipeline boundary | Production evidence to run | What the evidence covers | Gemini Web limitation |
|---|---|---|---|
| Canonical pipeline / facade handoff | `tests/test_tab2_canonical_pipeline_phase1.py`; `tests/test_professional_writer_workflow.py`; `tests/test_tab2_output_projection_phase2.py` | Canonical pipeline gates, identity propagation, Writer-to-Director handoff, prompt facade/output projection, and failure propagation covered by those tests. | The canonical test uses controlled collaborators in parts; it is not a real Gemini Web end-to-end benchmark. |
| Story Memory identity / temporal visibility | `tests/test_screenwriter_story_memory.py`; `tests/test_story_memory_canonical_character_identity.py`; `tests/test_story_memory_temporal_visibility.py` | Persisted identity, alias resolution, chapter/document scope, future visibility, and revision-related behavior. | Portable records cannot invoke StoryMemoryService or prove persisted currentness. |
| Continuity gate | `tests/test_full_story_continuity_completeness.py`; `tests/test_continuity_engine.py` | Derived continuity analysis and its production gate. | Gemini Web can report a cited finding but cannot certify that the production analyzer ran. |
| Writer readiness / frozen semantics | `tests/test_writer_frozen_contracts.py`; `tests/test_writer_readiness_quality_gate.py`; `tests/test_writer_screen_adaptation.py` | Frozen Writer invariants, readiness blockers, and source-grounded adaptation. | Do not interpret a schema-shaped Writer response as frozen-gate success. |
| Enrichment | `tests/test_writer_scene_action_enrichment.py`; `tests/test_writer_action_grounding_benchmark.py` | Deterministic action grounding and the checked-in `BASELINE_V1` safe/unsafe cases. | The fixture is a production-side regression baseline, not a Gemini accuracy score; historical equivalence is unclaimed. |
| Director authority / selection | `tests/test_director_frozen_contracts.py`; `tests/test_director_workflow.py`; `tests/test_director_knowledge_selector.py`; `tests/test_director_quality_facade.py` | Frozen Director boundaries, workflow, scored selector evidence, and facade quality behavior. | Current persisted Skill-store contents/version/activation are UNKNOWN; Gemini cannot run the deterministic selection/precedence gates. |
| Model capability / prompt assembly | `tests/test_model_capability_alignment.py`; `tests/test_prompt_engine.py`; `tests/test_external_model_final_prompt.py`; `tests/test_prompt_assembly.py`; `tests/test_tab2_dynamic_duration_contract.py` | Evidence-bound model capability and production prompt formatting/assembly contracts. | The selected Gemini Web assistant is distinct from the requested video model; portable text is not PromptEngine output. |
| Job / retry/idempotency and release gate | `tests/test_jobs.py`; `tests/test_tab2_targeted_quota_acceptance.py`; `tests/test_writer_frozen_contracts.py`; `tests/test_director_frozen_contracts.py` | Job semantics, quota acceptance and frozen contract gates. | Web chat retries/resubmission are not equivalent to production retry/idempotency handling. |
| Portable Gemini/Seedance contract add-ons | `tests/test_gemini_seedance_skill_contracts.py`; `tests/fixtures/gemini_seedance_skill_cases_v1.json` | Offline checks for unresolved style/reference stops, state-preserving detail metadata, action ambiguity, adaptive duration templates, prompt/export schemas and critical negative rules. | Synthetic deterministic contract checks only; they do not measure Gemini responses or assert production equivalence. |

## Full-pipeline benchmark status

`tests/test_tab2_canonical_pipeline_phase1.py` is relevant pipeline regression
evidence, not a measured full-pipeline benchmark. `tests/test_end_to_end_pipeline.py`
exercises another end-to-end path and is not treated as canonical Tab 2
Gemini-equivalence evidence. No Gemini Web expected-output corpus, scoring
protocol, acceptance thresholds, or live run is checked in. Those must come
from approved production evidence before a benchmark can be claimed.

The one checked-in frozen enrichment benchmark is
`tests/fixtures/writer_action_grounding_baseline_v1.json`, linked from the
Gemini enrichment package. Its documented historical status must remain
unchanged.
