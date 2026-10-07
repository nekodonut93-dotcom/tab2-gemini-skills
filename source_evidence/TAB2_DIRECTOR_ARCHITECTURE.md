# Tab 2 Director architecture and inventory

## Runtime authority

Professional path: validated `READY_FOR_DIRECTOR` + `DirectorHandoffV2` enters
`DirectorFacade` / `DirectorWorkflowService`. Director produces structured HOW
with identity, provenance, precedence and persisted current-result semantics.
`PromptFacade`/PromptEngine compiles; Director does not own final prompt syntax.

No runtime-active Director-owned LLM prompt template/system instruction was
found in inspected Director production scopes. The product flow that does use
Director reasoning in the quick/compatibility path expresses it through Python
heuristics, semantic concept mappings and typed requests/results. This is
different from Tab 2 Professional's orchestration and must remain labeled as a
separate call path.

## Verified Director concept families

The typed cinematic planner exposes or validates:

- scene geography, continuity memory and multi-shot consistency;
- blocking, choreography, subject references/routes and screen direction;
- shot purpose, coverage, shot size, shot sequence and splitting;
- camera angle, movement, motivation/timing, lens and focus intent;
- composition/framing;
- environment motion and performance realization;
- lighting and visual style/look;
- semantic pacing/rhythm, complexity and quality diagnostics;
- narrative presentation and audio decisions.

The compatibility Director heuristic separately emits a fixed three-shot
heuristic structure with generic framing, angle, lens language, movement,
subject relation and start/end framing. It is a production-active compatibility
surface, not the canonical Professional Director result authority.

## Catalog status

- Active default decisions are structured and rule/heuristic driven.
- Semantic concept mappings are applied when canonical concepts resolve.
- Skills are advisory and active conditionally through approval/compatibility
  checks.
- `NarrativePresentationSkill` and `SeedanceAudioSkill` are typed recommendation
  providers; the latter is model-gated.
- The phase 20.4.1 knowledge package contains eight approved knowledge items
  but the package itself is DRAFT/not activated and the default factory does not
  supply a knowledge package. Draft master-brain/experience records are
  similarly not proven active.
- The current persisted Skill-store contents/version/activation were not read;
  source audit cannot claim the current exact active Skill count.

## DIRECTING_KNOWLEDGE versus PROMPT_SYNTAX

| Type | Examples grounded in current code | Owner |
|---|---|---|
| `DIRECTING_KNOWLEDGE` | camera movement motivation, shot grammar, pacing, blocking, screen direction, lighting motivation, narrative presentation recommendations | Director reasoning/planner and approved Skill/knowledge records |
| `PROMPT_SYNTAX` | natural-language camera clauses, prompt section structure, model-specific section ordering/phrasing | PromptEngine adapter/templates |
| `DETERMINISTIC_CODE` | evidence/subject checks, precedence, lock, currentness, provider compatibility and schema validation | Director/workflow/contract code |

Do not move model literal strings into core Director concepts. Do not turn code
invariants into SKILL.md-only advice.

## Similar concepts and responsibility overlaps

- Camera-movement motivation recurs in the Director heuristic, semantic
  concept mappings, Skill recommendations and DRAFT knowledge revisions:
  semantic duplicate candidate; final authority remains Director workflow.
- Several approved/current Skill or sample references may express shot/camera
  grammar; exact active store state is unknown.
- Model-specific knowledge catalogs under
  `application/director_knowledge/model_adapters/` were found in DRAFT or
  REVIEW_PENDING state; do not promote them.
- Existing code model covers typed concepts, but historical docs call out
  optional detail gaps (blocking/angle/performance axes); this packaging phase
  does not expand them.

## Selective loading

The proposed `INDEX.yaml` separates categories and points to source-backed
records. It is a package navigation mechanism only; production router and
runtime do not read it. Current active algorithm, approved Skill data and
frozen ownership remain in their existing sources.

Sources: `application/director_reasoning/`, `application/director_workflow/`,
`application/director_knowledge/`, `application/director_intelligence/`,
`application/skill_intelligence_router/`, `application/skill_context_injection/`,
and the Director contract/frozen tests. Detailed item mapping:
inventory (production reference: `architecture/audits/TAB2_PROMPT_SKILL_INVENTORY.md`).
