# Tab 2 runtime call graph

Các cạnh dưới đây được xác minh qua factory wiring, route/job handler và
service callsites. Tên class/function và source file trong bảng là bằng chứng
runtime; architecture report lịch sử chỉ là supporting evidence.

## Professional Writer → Director prompt

```text
ui/application-adapter.js::createProfessionalWriterJob
→ application/api/routes.py::APIRouter.dispatch
→ application/runtime/application_factory.py::professional_writer_job
→ application/screenwriter_intelligence/professional_writer_workflow.py::process
→ StoryMemoryService / FullStoryContinuityAnalyzer
→ ScreenplayApplicationService::create_draft
→ Critic, lock, readiness, DirectorHandoffV2
```

Sau khi screenplay/readiness tồn tại:

```text
ui/application-adapter.js::generateProfessionalOutput
→ POST /api/writer/screenplays/{screenplay_id}/director-prompt
→ application/api/routes.py
→ application/professional_canonical_pipeline.py::execute
→ DirectorFacade / DirectorWorkflowService
→ ProfessionalCanonicalPipelineService::_prompt_context
→ PromptFacade::compile
→ ai_agent_brain/prompt_assembly/prompt_engine.py::PromptEngine.assemble
→ PromptAssembler + StructuredModelAdapter
→ VideoPromptPackage.final_prompt
→ saved projection / UI copy
```

`PromptEngine.assemble` is per packaged video segment. It validates typed input,
assembles a structured blueprint, compiles prose, and optionally delegates
language rendering. It does not call a video-generation provider.

## Compatibility / quick paths

```text
UI story_analysis (Compatibility)
→ /api/jobs/create
→ JobManager
→ StoryController.execute
→ optional DirectorRuntimeOrchestrator / skill context
→ PromptFacade → PromptEngine
```

`video_prompt_generation` is a separate legacy/quick-video job that calls
`VideoPromptController`, then the existing Director/Prompt facade boundaries.
These routes are not the canonical Professional Writer approval/handoff flow.

## Writer/Story subflow

```text
ProfessionalScreenwriterWorkflow.process
→ StoryMemoryService.ingest_document / ingest_chapter
→ FullStoryContinuityAnalyzer.analyze (official canon gate)
→ StoryReasoningProvider operations as required
→ reread_for_writer
→ ScreenplayApplicationService.create_draft
→ DeterministicWriterProvider.adapt_scene
→ optional DeterministicWriterProvider.enrich_official_scene
→ Writer critic / readiness / DirectorHandoffV2
```

Reasoning operations include `discover_story_issues`,
`reconcile_story_issues`, `resolve_story_issues`,
`critique_production_canon`, `diagnose_probe_failures`, and
`enrich_scene_visuals`. Calls are conditional on stage, findings, and eligibility.
Unavailability does not become a successful no-op for required Canon gates.

## Runtime owner classification

| Stage | Runtime owner | Classification |
|---|---|---|
| Professional screenplay generation and official mutation | `ProfessionalScreenwriterWorkflow` / `ScreenplayApplicationService` | ACTIVE_PRODUCTION |
| Persisted facts, identity and temporal retrieval | `StoryMemoryService` / repository | ACTIVE_PRODUCTION |
| Full-story interpretation/gate | `FullStoryContinuityAnalyzer` | ACTIVE_PRODUCTION, required |
| Enrichment proposals | `StoryReasoningProvider` called by Writer provider | ACTIVE_PRODUCTION, conditional |
| Director proposal/decision | `DirectorFacade` / `DirectorWorkflowService` | ACTIVE_PRODUCTION |
| Semantic provider/model prose | `PromptFacade` / `PromptEngine` | ACTIVE_PRODUCTION |
| compatibility story planner | `StoryController`/legacy planner helpers | compatibility; not Professional authority |
| standalone `PromptFormatter`/`PromptValidator` | direct standalone test path only in final-prompt assembly | ACTIVE_TEST_ONLY relative to canonical compiler |

## Call counts

Quota acceptance checks a five-chapter workflow with **5 discovery**,
**0 reconciliation**, **0 resolution**, **0 Canon critique**, **0 enrichment**,
**0 Director semantic dispatch**, and **0 embedding dispatches** for the
controlled fixture. Language rerender is a separate, user-triggered path.
See quota/cache/retry (production reference: `architecture/TAB2_QUOTA_CACHE_RETRY.md`) and
`tests/test_tab2_targeted_quota_acceptance.py`.
