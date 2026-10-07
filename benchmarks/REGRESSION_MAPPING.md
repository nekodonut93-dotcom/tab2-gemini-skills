# Portable components to production regression map

| Portable area | Production regression evidence | Scope limit |
|---|---|---|
| Frozen Writer/Director ownership | `tests/test_writer_frozen_contracts.py`; `tests/test_director_frozen_contracts.py` | Tests production contracts, not Gemini adherence |
| Story Memory and visibility | `tests/test_screenwriter_story_memory.py`; `tests/test_story_memory_temporal_visibility.py` | Portable JSON is not the production store |
| Continuity and gates | `tests/test_full_story_continuity_completeness.py`; `tests/test_continuity_engine.py` | No Gemini Web execution evidence |
| Writer/enrichment | `tests/test_writer_scene_action_enrichment.py`; `tests/test_writer_action_grounding_benchmark.py` | Production acceptance only |
| Director | `tests/test_director_workflow.py`; `tests/test_director_quality_facade.py`; `tests/test_director_knowledge_selector.py` | Active production store state may remain unknown |
| PromptEngine/Seedance formatting | `tests/test_prompt_engine.py`; `tests/test_external_model_final_prompt.py`; `tests/test_tab2_dynamic_duration_contract.py` | Formatting is not video-generation API proof |
| Visual/action/choreography/Style portable layers | `tests/test_gemini_seedance_skill_contracts.py` | Portable tests only; no new production authority |
| Language/chibi portable contract | `tests/test_gemini_language_chibi_contracts.py` | Schema/invariant tests only; no production runtime authority |
| Gemini full pipeline | `benchmarks/gemini_seedance_skill_cases_v1.json` | Synthetic/offline fixture; benchmark NOT RUN |
