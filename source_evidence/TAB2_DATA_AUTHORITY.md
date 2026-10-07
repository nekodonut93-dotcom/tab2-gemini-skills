# Tab 2 data authority map

| Responsibility | Authoritative owner | Downstream may do | Must not do |
|---|---|---|---|
| Persisted source, identity, knowledge, facts, provenance, time visibility | Story Memory | Query scoped visible context; propose reviewable changes | Treat a derived report as persisted canon |
| Derived cross-chapter consistency and repairs | Production Canon / `FullStoryContinuityAnalyzer` | Gate official Writer scene creation; carry source-bound overlay | Rewrite source text or bypass incomplete analysis |
| Story semantics, scene/block identity, exact dialogue, outcomes | Writer / `ScreenplayApplicationService` | Director reads validated immutable handoff | Director or prompt compiler rewrites WHAT |
| Safe adaptation / enrichment | Existing Writer adaptation/enrichment boundary | Add evidence-bound presentation-only blocks when permitted | Create event, prop, dialogue, relationship, outcome or knowledge |
| Official screenplay mutation and validation | `ScreenplayApplicationService` | Persist current version and adaptation evidence | Add a competing screenplay mutation authority |
| Director HOW | `DirectorFacade` and canonical Director workflow | Select structured cinematic realization and provenance | Change Writer facts, output syntax, or current-result authority |
| Skill lifecycle and routing | Canonical Skill services, router, injector | Rank/submit approved compatible recommendations | Commit Director decision, bypass user locks, or emit final prose |
| Final prompt text | `PromptFacade` → `PromptEngine` | Compile typed Writer/Director context through model adapter | Construct a second final prompt in UI/Director/Skill |
| Provider syntax/capability | model profile, template and adapter boundary | Translate semantic intent, report unsupported model surfaces | Put syntax in Writer/Director semantic contracts |
| Language rendering | `PromptLanguageRenderer` under PromptEngine | Translate final prose while protecting source strings | Claim translation success when fallback retained canonical text |
| User copy/display | returned saved `final_prompt` projection | Display/copy the persisted/compiled value | Regenerate on read or build prompt in the UI |
| Job state/idempotency | `JobManager`; production task retry in ProductionOrchestrator | Return/retry attempts under existing keys/state machine | Replace one with another or assume retries are identical |

## Frozen ownership invariants

- Writer owns WHAT; Director owns HOW.
- Story Memory is persisted authority; Production Canon is a derived gate.
- `DirectorHandoffV2` remains the Writer → Director boundary.
- PromptEngine remains the only final compiler.
- Temporal visibility, source identity and alias authority remain deterministic
  code enforcement.
- Skill records may guide, never override, deterministic code authority.

## Duplicated-responsibility register

The following overlap is documented, not refactored in this phase.

| Code locations | Classification | Risk | Recommended owner |
|---|---|---|---|
| `ScreenwriterIntelligence.analyze` during ingest; `FullStoryContinuityAnalyzer`; `reread_for_writer`; chapter scene generation | `DUPLICATED_RESPONSIBILITY` — repeated source analysis at distinct gates, not identical outputs | Parser/evidence drift and confusing repeated work could weaken confidence in which stage owns each finding | Preserve separate stages; Story Memory owns persisted records, Production Canon owns derived gate, Writer scene analysis owns screenplay projection |
| `application/screenwriter_intelligence/scene_analyzer.py::SceneAnalyzer`; `ai_agent_brain/story_director/scene_planner.py::StoryScenePlanner`; `application/story_intelligence/planner.py::StoryIntelligencePlanner.scenes` | `DUPLICATED_RESPONSIBILITY` — scene segmentation/planning surfaces coexist; only `SceneAnalyzer` is in the Professional default path | Future maintenance may mistake a compatibility/unused planner for official scene authority | `SceneAnalyzer` through ScreenplayService for Professional; explicitly mark other paths legacy/optional |
| Deterministic Director heuristics, resolved semantic concept mappings, routed Skill rules, and non-active Director-knowledge revisions can all mention camera movement/motivation | `DUPLICATED_RESPONSIBILITY` — overlapping knowledge, with distinct decision/enforcement roles | Conflicting advice or stale candidate rules | Director workflow is final decision owner; deterministic checks enforce; Skills are advisory; DRAFT package stays inactive |
| `application/skills/seedance_audio_prompt.json` and persisted canonical Seedance Audio Skill record | `DUPLICATED_RESPONSIBILITY` — same knowledge family has file and store representations | Version/provenance divergence; the file alone does not prove active record content | Canonical Skill store/router is runtime owner; JSON remains source/review evidence pending explicit linkage verification |
| `PromptAssembler` blueprint sections and `StructuredModelAdapter` prose clauses | No competing authority; layered formatting surfaces | Template sections may not map one-to-one to model adapter clauses | PromptEngine owns assembly; adapter owns model syntax. Keep the distinction and test templates per model |

“Duplicated” above means overlapping responsibility/catalog content, not proof of
two equally authoritative active producers. No contract or source code was
changed to consolidate them.
