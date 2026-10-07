from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import re
from pathlib import Path, PurePosixPath


REPOSITORY = Path(__file__).resolve().parent
PRODUCTION = REPOSITORY.parent
VERSION = "1.1.0"
BUILD_DATE = "2026-10-07"
PORTABLE = "PORTABLE_GEMINI_REFERENCE_ONLY"

FROZEN_FILES = (
    "architecture/writer_contract_freeze_v1.json",
    "architecture/director_contract_freeze_v1.json",
)
ARCHITECTURE_EXPORTS = (
    "architecture/TAB2_CALL_GRAPH.md",
    "architecture/TAB2_DATA_AUTHORITY.md",
    "architecture/TAB2_FROZEN_CONTRACTS.md",
    "architecture/TAB2_DIRECTOR_ARCHITECTURE.md",
    "architecture/TAB2_MODEL_ADAPTERS.md",
    "architecture/TAB2_PROMPT_SKILL_ARCHITECTURE.md",
    "architecture/SCENE_ACTION_ENRICHMENT.md",
    "architecture/GEMINI_MODEL_ROUTING_AND_LIVE_ACCEPTANCE.md",
    "architecture/GEMINI_STABLE_LIVE_ACCEPTANCE.md",
    "architecture/GEMINI_LIVE_STORY_REPAIR_ACCEPTANCE.md",
    "architecture/TAB2_OUTPUT_SHEETS_SCENE_COPY_PHASE2.md",
)
SKILL_EXPORTS = (
    ("00-orchestrator", "00-long-novel-orchestrator", "skills/00-orchestrator/manifest.yaml"),
    ("01-story-memory", "01-story-memory", "skills/01-story-memory/manifest.yaml"),
    ("02-continuity", "02-continuity", "skills/02-continuity/manifest.yaml"),
    ("03-writer", "03-writer", "skills/03-writer/manifest.yaml"),
    ("04-enrichment", "04-enrichment", "skills/04-enrichment/manifest.yaml"),
    ("04b-visual-completion", "04b-visual-completion", "skills/04b-visual-completion/manifest.yaml"),
    ("04c-action-interpreter", "04c-action-interpreter", "skills/04c-action-interpreter/manifest.yaml"),
    ("04d-action-choreography", "04d-action-choreography", "skills/04d-action-choreography/manifest.yaml"),
    ("04e-chibi-performance", "04e-chibi-performance", "skills/04e-chibi-performance/manifest.yaml"),
    ("05-director", "05-director", "skills/05-director/manifest.yaml"),
    ("06-prompt-engine", "06-prompt-engine", "skills/06-prompt-engine/manifest.yaml"),
    ("07-quality-audit", "07-quality-audit", "skills/07-quality-audit/manifest.yaml"),
    ("08-seedance", "08-seedance", "skills/08-seedance/manifest.yaml"),
    ("09-style-resolution", "09-style-resolution", "skills/09-style-resolution/manifest.yaml"),
)

CAPABILITIES = [
    {
        "id": "production-authority-and-workflow",
        "status": "VERIFIED",
        "what_is_evidenced": "Canonical call graph, source authorities, frozen ownership, and production facade flow are documented and tested.",
        "production_sources": ["architecture/TAB2_CALL_GRAPH.md", "architecture/TAB2_DATA_AUTHORITY.md", "architecture/TAB2_FROZEN_CONTRACTS.md"],
        "source_skill": "skills/00-orchestrator/manifest.yaml",
        "tests": ["tests/test_tab2_canonical_pipeline_phase1.py", "tests/test_professional_writer_workflow.py", "tests/test_writer_frozen_contracts.py", "tests/test_director_frozen_contracts.py"],
        "known_gaps": ["Gemini Web cannot execute production deterministic validators; portable compliance is not production certification."],
    },
    {
        "id": "story-memory-identity-provenance-temporal-visibility",
        "status": "VERIFIED",
        "what_is_evidenced": "Production StoryMemoryService owns persisted identity/provenance and chapter-scoped visibility; future and superseded knowledge is filtered by production behavior.",
        "production_sources": ["application/screenwriter_intelligence/story_memory.py", "application/screenwriter_intelligence/memory_models.py", "architecture/TAB2_DATA_AUTHORITY.md"],
        "source_skill": "skills/01-story-memory/manifest.yaml",
        "tests": ["tests/test_screenwriter_story_memory.py", "tests/test_story_memory_canonical_character_identity.py", "tests/test_story_memory_temporal_visibility.py"],
        "known_gaps": ["Gemini's portable state is not persisted Story Memory and cannot certify database currentness."],
    },
    {
        "id": "production-continuity-canon-gate",
        "status": "VERIFIED",
        "what_is_evidenced": "FullStoryContinuityAnalyzer produces the derived continuity/Canon gate; Story Memory remains persisted authority.",
        "production_sources": ["application/screenwriter_intelligence/full_story_continuity.py", "architecture/TAB2_DATA_AUTHORITY.md"],
        "source_skill": "skills/02-continuity/manifest.yaml",
        "tests": ["tests/test_full_story_continuity_completeness.py", "tests/test_continuity_engine.py", "tests/test_story_memory_temporal_visibility.py"],
        "known_gaps": ["Gemini Web execution of the production analyzer is not established."],
    },
    {
        "id": "writer-what-readiness-and-handoff",
        "status": "VERIFIED",
        "what_is_evidenced": "Writer owns story WHAT and official screenplay mutation/readiness before DirectorHandoffV2; frozen Writer contracts are tested.",
        "production_sources": ["application/screenwriter_intelligence/professional_writer_workflow.py", "application/screenwriter_intelligence/screenplay_service.py", "architecture/TAB2_FROZEN_CONTRACTS.md"],
        "source_skill": "skills/03-writer/manifest.yaml",
        "tests": ["tests/test_writer_screen_adaptation.py", "tests/test_writer_outcome_context_e2e.py", "tests/test_writer_frozen_contracts.py", "tests/test_professional_writer_workflow.py"],
        "known_gaps": ["Gemini Web output is not official screenplay state and cannot claim frozen readiness."],
    },
    {
        "id": "writer-enrichment-deterministic-grounding",
        "status": "VERIFIED",
        "what_is_evidenced": "Production enrichment is conditional; deterministic grounding and acceptance/rejection are covered by tests and BASELINE_V1.",
        "production_sources": ["application/screenwriter_intelligence/writer_provider.py", "application/screenwriter_intelligence/screenplay_service.py", "architecture/SCENE_ACTION_ENRICHMENT.md"],
        "source_skill": "skills/04-enrichment/manifest.yaml",
        "tests": ["tests/test_writer_scene_action_enrichment.py", "tests/test_writer_action_grounding_benchmark.py"],
        "known_gaps": ["Portable micro-motion candidates do not imply production acceptance beyond existing test evidence; historical benchmark equivalence is unclaimed."],
    },
    {
        "id": "visual-completion",
        "status": "PARTIAL",
        "what_is_evidenced": "Production has evidence-bounded scene visual enrichment; the separate broad gaze/body/secondary-motion candidate catalog is a portable proposal layer.",
        "production_sources": ["architecture/SCENE_ACTION_ENRICHMENT.md", "application/screenwriter_intelligence/writer_provider.py"],
        "source_skill": "skills/04b-visual-completion/manifest.yaml",
        "tests": ["tests/test_writer_scene_action_enrichment.py", "tests/test_writer_action_grounding_benchmark.py"],
        "known_gaps": ["No production acceptance matrix was found for every new portable visual-completion candidate."],
    },
    {
        "id": "action-interpreter",
        "status": "NOT_IMPLEMENTED",
        "what_is_evidenced": "The action taxonomy/interpreter is a new portable classification reference, not an identified production service.",
        "production_sources": ["architecture/SCENE_ACTION_ENRICHMENT.md"],
        "source_skill": "skills/04c-action-interpreter/manifest.yaml",
        "tests": ["tests/test_gemini_seedance_skill_contracts.py"],
        "known_gaps": ["No production action-classification API, semantic contract, or acceptance suite is claimed."],
    },
    {
        "id": "action-choreography",
        "status": "NOT_IMPLEMENTED",
        "what_is_evidenced": "Production Director contains structured HOW planning; the separate portable six-phase choreography guide is not a production contract.",
        "production_sources": ["architecture/TAB2_DIRECTOR_ARCHITECTURE.md", "architecture/TAB2_FROZEN_CONTRACTS.md"],
        "source_skill": "skills/04d-action-choreography/manifest.yaml",
        "tests": ["tests/test_gemini_seedance_skill_contracts.py"],
        "known_gaps": ["No production phase-by-phase action choreography executor or contract is claimed."],
    },
    {
        "id": "director-how-and-advisory-skills",
        "status": "PARTIAL",
        "what_is_evidenced": "DirectorFacade/DirectorWorkflowService own structured HOW and are frozen/tested; exported Director INDEX defines bounded retrieval, source-supported selection, status and conflicts_with fields; Skill advice remains approval/compatibility gated.",
        "production_sources": ["application/director_facade.py", "application/director_workflow/", "architecture/TAB2_DIRECTOR_ARCHITECTURE.md"],
        "source_skill": "skills/05-director/manifest.yaml",
        "tests": ["tests/test_director_frozen_contracts.py", "tests/test_director_workflow.py", "tests/test_director_quality_facade.py", "tests/test_director_knowledge_selector.py"],
        "known_gaps": ["Current persisted Director Skill-store contents/version/activation remain UNKNOWN; portable index is not production router.", "A scored production Skill ranking/order algorithm is not evidenced; no score or tie-break behavior is invented."],
    },
    {
        "id": "promptengine-seedance-formatting",
        "status": "VERIFIED",
        "what_is_evidenced": "Seedance profile/template/adapter are checked in and PromptEngine is the production final compiler.",
        "production_sources": ["ai_agent_brain/prompt_assembly/prompt_engine.py", "application/prompt_facade.py", "model_profiles/seedance.json", "prompt_templates/seedance.json", "architecture/TAB2_MODEL_ADAPTERS.md"],
        "source_skill": "skills/06-prompt-engine/manifest.yaml",
        "tests": ["tests/test_prompt_engine.py", "tests/test_prompt_assembly.py", "tests/test_external_model_final_prompt.py", "tests/test_tab2_dynamic_duration_contract.py"],
        "known_gaps": ["No Seedance generation API capability is established by formatting assets; PromptLanguageRenderer cache version coverage is a documented review gap."],
    },
    {
        "id": "quality-audit-and-frozen-regression",
        "status": "VERIFIED",
        "what_is_evidenced": "Frozen contracts, stage regression and enrichment baseline are mapped to executable production tests.",
        "production_sources": ["architecture/writer_contract_freeze_v1.json", "architecture/director_contract_freeze_v1.json", "architecture/TAB2_FROZEN_CONTRACTS.md"],
        "source_skill": "skills/07-quality-audit/manifest.yaml",
        "tests": ["tests/test_writer_frozen_contracts.py", "tests/test_director_frozen_contracts.py", "tests/test_writer_action_grounding_benchmark.py", "tests/test_tab2_canonical_pipeline_phase1.py"],
        "known_gaps": ["No Gemini Web full-pipeline benchmark or quality threshold is present."],
    },
    {
        "id": "style-resolution-user-intake",
        "status": "NOT_IMPLEMENTED",
        "what_is_evidenced": "PROJECT_VISUAL_PROFILE and style questionnaire are portable additions; no production-owned style-intake service is claimed.",
        "production_sources": ["architecture/TAB2_PROMPT_SKILL_ARCHITECTURE.md"],
        "source_skill": "skills/09-style-resolution/manifest.yaml",
        "tests": ["tests/test_gemini_seedance_skill_contracts.py"],
        "known_gaps": ["No production persistence or runtime gate for PROJECT_VISUAL_PROFILE."],
    },
    {
        "id": "dola-ui-reference-binding",
        "status": "UNKNOWN",
        "what_is_evidenced": "No checked-in evidence verifies Dola UI tag syntax or reference-binding semantics.",
        "production_sources": ["architecture/TAB2_MODEL_ADAPTERS.md"],
        "source_skill": "skills/08-seedance/manifest.yaml",
        "tests": ["tests/test_gemini_seedance_skill_contracts.py"],
        "known_gaps": ["Do not emit @ImageN/@VideoN tags unless confirmed by current UI/user; otherwise REFERENCE_BINDING_UNVERIFIED."],
    },
    {
        "id": "gemini-web-full-pipeline-equivalence",
        "status": "NOT_IMPLEMENTED",
        "what_is_evidenced": "Repository has offline production regressions and historical Gemini API reports; no Gemini Web Tab 2 full-pipeline benchmark is checked in.",
        "production_sources": ["architecture/GEMINI_STABLE_LIVE_ACCEPTANCE.md", "architecture/GEMINI_LIVE_STORY_REPAIR_ACCEPTANCE.md"],
        "source_skill": "skills/07-quality-audit/manifest.yaml",
        "tests": ["tests/test_gemini_seedance_skill_contracts.py", "tests/test_tab2_canonical_pipeline_phase1.py"],
        "known_gaps": ["Synthetic portable tests do not establish Gemini model quality or web UI behavior."],
    },
    {
        "id": "prompt-language-rendering",
        "status": "VERIFIED",
        "what_is_evidenced": "PromptLanguageRenderer normalizes English/Vietnamese/Chinese and renders technical prompt text when configured; tests exercise language normalization and engine behavior.",
        "production_sources": ["ai_agent_brain/prompt_assembly/language_renderer.py", "ai_agent_brain/prompt_assembly/prompt_engine.py"],
        "source_skill": "skills/language-policy/manifest.yaml",
        "tests": ["tests/test_prompt_engine.py"],
        "known_gaps": ["Production prompt_language is a prompt-rendering setting, not a project-wide source/spoken-language profile."],
    },
    {
        "id": "source-text-language-independence",
        "status": "PARTIAL",
        "what_is_evidenced": "Writer owns exact source dialogue; PromptLanguageRenderer can protect source text supplied by PromptEngine callers, including typed narrative-expression source text.",
        "production_sources": ["skills/03-writer/SKILL.md", "ai_agent_brain/prompt_assembly/prompt_engine.py", "ai_agent_brain/prompt_assembly/language_renderer.py"],
        "source_skill": "skills/language-policy/manifest.yaml",
        "tests": ["tests/test_writer_frozen_contracts.py", "tests/test_prompt_engine.py"],
        "known_gaps": ["No frozen production PROJECT_LANGUAGE_PROFILE or end-to-end assurance that every spoken/voice-over field is separated from technical prompt rendering."],
    },
    {
        "id": "portable-project-language-profile-and-typed-speech",
        "status": "MISSING",
        "what_is_evidenced": "New portable package defines independent user-selected source, prompt, dialogue, internal-monologue, voice-over and on-screen-text languages.",
        "production_sources": ["ai_agent_brain/prompt_assembly/language_renderer.py", "ai_agent_brain/prompt_assembly/prompt_engine.py"],
        "source_skill": "skills/language-policy/manifest.yaml",
        "tests": ["tests/test_gemini_language_chibi_contracts.py"],
        "known_gaps": ["This profile and typed export policy are Gemini-facing additions, not production runtime behavior."],
    },
    {
        "id": "profile-gated-basic-chibi-insert",
        "status": "PARTIAL",
        "what_is_evidenced": "Existing portable style profile and Seedance examples permit brief nonverbal chibi reactions and forbid invented lines/confessions.",
        "production_sources": ["skills/09-style-resolution/PROJECT_VISUAL_PROFILE.schema.json", "skills/08-seedance/vfx/comedic.yaml", "skills/08-seedance/examples/good/comedy_reaction.yaml"],
        "source_skill": "skills/09-style-resolution/manifest.yaml",
        "tests": ["tests/test_gemini_seedance_skill_contracts.py"],
        "known_gaps": ["Existing reference did not define typed inner-monologue routing, symbolic action namespace, or a full real-vs-non-diegetic state contract."],
    },
    {
        "id": "chibi-inner-monologue-symbolic-performance",
        "status": "MISSING",
        "what_is_evidenced": "New portable reference distinguishes source monologue, nonverbal response and non-diegetic chibi action; it does not claim production behavior.",
        "production_sources": ["skills/03-writer/SKILL.md", "skills/08-seedance/vfx/comedic.yaml", "skills/08-seedance/examples/good/chinese_3d_chibi.yaml"],
        "source_skill": "skills/04e-chibi-performance/manifest.yaml",
        "tests": ["tests/test_gemini_language_chibi_contracts.py"],
        "known_gaps": ["No production chibi performance service or frozen contract is evidenced."],
    },
    {
        "id": "dola-reference-tags",
        "status": "UNKNOWN",
        "what_is_evidenced": "The existing package explicitly records Dola tag syntax as unknown and fails closed.",
        "production_sources": ["skills/08-seedance/platforms/dola.yaml"],
        "source_skill": "skills/08-seedance/manifest.yaml",
        "tests": ["tests/test_gemini_language_chibi_contracts.py"],
        "known_gaps": ["Current Dola UI syntax requires direct current UI confirmation; no @ImageN/@VideoN syntax is assumed."],
    },
]

SKILL_SECTIONS = {
    "04b-visual-completion": {
        "ROLE": "Propose bounded visible physical detail for a video-readable accepted scene.",
        "AUTHORITY": "Writer owns WHAT; this package proposes presentation detail only. Production enrichment acceptance remains code-owned.",
        "INPUT": "Accepted Writer scene, current visible context, resolved actor identity, source references, and project style preference.",
        "OUTPUT": "Detail candidates labeled with origin, source references, and changes_story_state.",
        "WORKFLOW": "Resolve the actor and visible scene context; select a context-supported candidate; reject state-changing detail.",
        "ALLOWED": "Context-supported gaze, head movement, breathing, posture, position, weight shift, reaction pause, and secondary motion as proposals.",
        "FORBIDDEN": "New event, dialogue, important prop, location, knowledge, relationship, injury, reveal, outcome, or fixed emotion-to-gesture mapping.",
        "FAIL CONDITIONS": "Ambiguous actor/target, unknown visibility, missing evidence, or changes_story_state=true.",
        "VALIDATION": "Check origin, source_refs, scene visibility, identity, and unchanged story state; do not claim production acceptance.",
        "NEXT STAGE": "Pass accepted portable details to action interpretation/choreography or Director as read-only context; otherwise stop/return.",
        "REFERENCES": ["safe_visual_inference.yaml", "forbidden_story_inference.yaml", "body_motion.yaml", "gaze.yaml", "reaction.yaml", "secondary_motion.yaml", "tests/test_writer_scene_action_enrichment.py", "tests/test_writer_action_grounding_benchmark.py"],
    },
    "04c-action-interpreter": {
        "ROLE": "Normalize source-backed literary action to a conservative semantic class.",
        "AUTHORITY": "Writer action and source remain authoritative; classification is derived portable metadata.",
        "INPUT": "Writer action, source references, current visible scene context, resolved actor.",
        "OUTPUT": "Action class plus evidenced direction/target/contact and unresolved fields.",
        "WORKFLOW": "Classify only the supported specificity; use GENERIC_SINGLE_SLASH only if a single slash is explicit; otherwise leave unresolved.",
        "ALLOWED": "Classes in action_taxonomy.yaml for sword/fight, movement, driving, phone, eating, object, romance, and dialogue.",
        "FORBIDDEN": "Unsupported target, direction, subtype, spin, jump, acrobatics, impact, magic, injury, or result.",
        "FAIL CONDITIONS": "Unresolved actor/action or a classification requiring unsupported specificity.",
        "VALIDATION": "Trace class to source/context; keep ambiguity explicit; do not change Writer WHAT.",
        "NEXT STAGE": "Pass a resolved class to optional choreography; otherwise return UNRESOLVED.",
        "REFERENCES": ["action_taxonomy.yaml", "examples/README.md", "tests/test_gemini_seedance_skill_contracts.py"],
    },
    "04d-action-choreography": {
        "ROLE": "Propose optional physical phases for an already classified action.",
        "AUTHORITY": "Writer owns WHAT; choreography is not a production screenplay mutation or Director decision.",
        "INPUT": "Resolved action class, Writer action, current visible context, project style profile.",
        "OUTPUT": "Optional pre_action/anticipation/primary_action/follow_through/reaction/settle phases.",
        "WORKFLOW": "Choose only context-supported phases; use fewer for simple actions; preserve source action and end state.",
        "ALLOWED": "Readable physical realization consistent with action class and selected visual style.",
        "FORBIDDEN": "New contact/result, acrobatics, injury, event, emotion/relationship change, or story-state change.",
        "FAIL CONDITIONS": "Actor/action/target unresolved or any phase would add unsupported state.",
        "VALIDATION": "Check phase support, source refs, unchanged WHAT and no invented outcome.",
        "NEXT STAGE": "Pass bounded proposal to Director/Seedance draft, never to production screenplay state.",
        "REFERENCES": ["choreography_phases.yaml", "examples/README.md", "tests/test_gemini_seedance_skill_contracts.py"],
    },
    "04e-chibi-performance": {
        "ROLE": "Route source-established inner monologue and reactions through optional, brief chibi performance without changing story reality.",
        "AUTHORITY": "Portable presentation only. Writer owns exact source text and WHAT; Director owns production HOW; PromptFacade/PromptEngine remains production final-prompt authority.",
        "INPUT": "Accepted Writer scene with typed source expressions/actions, resolved PROJECT_VISUAL_PROFILE, resolved PROJECT_LANGUAGE_PROFILE, current scene timeline, and identity/source references.",
        "OUTPUT": "A contextual chibi mode or no chibi; every symbolic action is separately named, NON_DIEGETIC, and has story_state_effect NONE.",
        "WORKFLOW": "Separate source spoken dialogue, internal monologue, narrator voice-over, nonverbal reaction, and on-screen text; preserve source strings; check language and visual profiles; select among contextual candidates; ensure timing and immediate return to the main scene.",
        "ALLOWED": "CHIBI_SPOKEN_MONOLOGUE, CHIBI_NONVERBAL_REACTION, CHIBI_SYMBOLIC_PANTOMIME, or CHIBI_EMOTION_BURST only when the resolved visual profile permits it; otherwise use source-faithful ordinary performance.",
        "FORBIDDEN": "Invent dialogue/thought, translate source speech, treat symbolic action as real action, create a real target/injury/event, force every monologue into chibi, map one emotion to one fixed gesture, or transform the whole scene unless full_chibi_scene is explicitly true.",
        "FAIL CONDITIONS": "Missing source text for spoken/thought content, unresolved profiles, unsupported real-world punch/kick/crying, any diegetic state change, or no reliable return-to-scene continuity.",
        "VALIDATION": "Check exact source strings and type labels; chibi_insertions enabled; full-scene flag; representation_scope=NON_DIEGETIC; story_state_effect=NONE; no real-world event; and explicit return to main scene.",
        "NEXT STAGE": "Pass separate REAL_ACTION and CHIBI_SYMBOLIC_ACTION records to Seedance draft; do not merge their namespaces or mutate Writer/Story Memory.",
        "REFERENCES": ["grammars/", "inner_monologue/", "constraints/", "examples/", "../../language/LANGUAGE_POLICY.md", "../../seedance/schemas/seedance_scene_package.schema.json"],
    },
    "08-seedance": {
        "ROLE": "Prepare a portable user-reviewable Seedance prompt draft and sheet row.",
        "AUTHORITY": "PromptFacade → PromptEngine remains sole production final-prompt authority; Dola UI syntax is unknown absent confirmation.",
        "INPUT": "Accepted Writer scene, Director HOW, resolved user profile, references confirmed by UI, and duration 5/10/15 seconds.",
        "OUTPUT": "Portable prompt_draft and copyable export row or explicit blocked/unresolved status.",
        "WORKFLOW": "Require resolved visual and language profiles; keep technical prompt language separate from typed source speech languages; preserve source strings; bind references without invented tags; preserve WHAT; apply optional visual/choreography proposals; use adaptive duration target; draft ordered sections; validate.",
        "ALLOWED": "Format visible scene, Director HOW, selected style/languages, typed source expressions, confirmed references, and style-permitted presentation/VFX as a portable draft.",
        "FORBIDDEN": "Claim production PromptEngine compilation, dispatch generation, invent platform tags, translate or invent source speech, merge chibi symbolic actions with real actions, or alter story semantics.",
        "FAIL CONDITIONS": "STYLE_UNRESOLVED, LANGUAGE_UNRESOLVED, REFERENCE_BINDING_UNVERIFIED, blocked Writer/readiness, missing evidence, or state change.",
        "VALIDATION": "Validate portable schemas, independent prompt/spoken languages, exact source strings, typed sections, profile, tag status, target timeline, negative rules, VFX/chibi policy, and export row.",
        "NEXT STAGE": "Quality audit and user review; production prompt compilation remains the separate canonical path.",
        "REFERENCES": ["../../seedance/PROMPT_CONTRACT.yaml", "../../seedance/platforms/dola.yaml", "../../seedance/schemas/seedance_scene_package.schema.json", "../../seedance/sheet_export/sheet_export.schema.json", "tests/test_prompt_engine.py", "tests/test_gemini_seedance_skill_contracts.py"],
    },
    "09-style-resolution": {
        "ROLE": "Resolve explicit user visual preference before portable video-prompt drafting.",
        "AUTHORITY": "User preference only; PROJECT_VISUAL_PROFILE is not Story Memory, Canon, Writer WHAT, Director HOW, or PromptEngine authority.",
        "INPUT": "Project state, existing project profile, and explicit user selections.",
        "OUTPUT": "Resolved PROJECT_VISUAL_PROFILE or STYLE_UNRESOLVED question.",
        "WORKFLOW": "Read profile; if unresolved ask user; persist only explicit choice; default full_chibi_scene to false; validate schema; reuse until user changes it.",
        "ALLOWED": "Offer preset and user-controlled expression, comedy, monologue, chibi inserts, explicit full-scene chibi, VFX, camera and realism settings.",
        "FORBIDDEN": "Infer style from story, genre, costume, language, emotion or model name.",
        "FAIL CONDITIONS": "Missing required choice, invalid profile, or custom values not explicitly supplied.",
        "VALIDATION": "Check profile schema, selected_by=USER, required resolved fields, revision and portable scope.",
        "NEXT STAGE": "Only after resolved, pass profile read-only to the next portable stage; otherwise stop before prompt draft.",
        "REFERENCES": ["style_questionnaire.yaml", "style_presets.yaml", "PROJECT_VISUAL_PROFILE.schema.json", "tests/test_gemini_seedance_skill_contracts.py"],
    },
}


def _relative(path: Path) -> str:
    return path.relative_to(REPOSITORY).as_posix()


class ExportBuilder:
    def __init__(self) -> None:
        self.provenance: dict[str, dict] = {}
        self.previous_manifest_path = REPOSITORY / "SOURCE_MANIFEST.json"
        self.previous_manifest = None
        if self.previous_manifest_path.exists():
            self.previous_manifest = json.loads(self.previous_manifest_path.read_text(encoding="utf-8"))
        self.baseline_path = REPOSITORY / "validation" / "frozen_contract_baseline.json"
        self.baseline = None
        if self.baseline_path.exists():
            self.baseline = json.loads(self.baseline_path.read_text(encoding="utf-8"))

    def _record(
        self,
        relative: str,
        *,
        sources: list[str],
        skill_version: str | None = None,
        schema_version: str = "not_applicable",
        status: str = PORTABLE,
        gaps: list[str] | None = None,
    ) -> None:
        self.provenance[relative] = {
            "source_production_files": sources,
            "source_skill_version": skill_version,
            "schema_version": schema_version,
            "distribution_version": VERSION,
            "status": status,
            "known_gaps": gaps or [],
        }

    def write(
        self,
        relative: str,
        content: str | bytes,
        *,
        sources: list[str],
        skill_version: str | None = None,
        schema_version: str = "not_applicable",
        status: str = PORTABLE,
        gaps: list[str] | None = None,
    ) -> None:
        target = REPOSITORY / PurePosixPath(relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, str):
            data = (content.rstrip() + "\n").encode("utf-8")
        else:
            data = content
        target.write_bytes(data)
        self._record(
            relative,
            sources=sources,
            skill_version=skill_version,
            schema_version=schema_version,
            status=status,
            gaps=gaps,
        )

    def copy_file(
        self,
        source_relative: str,
        target_relative: str,
        *,
        skill_version: str | None = None,
        schema_version: str = "not_applicable",
        status: str = PORTABLE,
        gaps: list[str] | None = None,
    ) -> None:
        source = PRODUCTION / PurePosixPath(source_relative)
        if not source.is_file():
            raise FileNotFoundError(f"Required production evidence missing: {source_relative}")
        self.write(
            target_relative,
            source.read_bytes(),
            sources=[source_relative],
            skill_version=skill_version,
            schema_version=schema_version,
            status=status,
            gaps=gaps,
        )

    def copy_tree(
        self,
        source_relative: str,
        target_relative: str,
        *,
        skill_version: str,
        skip_names: set[str] | None = None,
    ) -> None:
        source = PRODUCTION / PurePosixPath(source_relative)
        skip_names = skip_names or set()
        for path in sorted(source.rglob("*")):
            if not path.is_file() or path.name in skip_names:
                continue
            if path.suffix in {".pyc", ".pyo"} or "__pycache__" in path.parts:
                continue
            rel = path.relative_to(source).as_posix()
            target = f"{target_relative}/{rel}"
            self.write(
                target,
                path.read_bytes(),
                sources=[path.relative_to(PRODUCTION).as_posix()],
                skill_version=skill_version,
                schema_version=self._schema_identity(path),
                gaps=[],
            )

    @staticmethod
    def _schema_identity(path: Path) -> str:
        if path.suffix != ".json":
            return "not_applicable"
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return "not_applicable"
        return data.get("$id") or data.get("title") or "portable-schema-unversioned"

    def _remove_prior_generated_files(self) -> None:
        if not self.previous_manifest:
            return
        previous = self.previous_manifest.get("files", {})
        for relative in previous:
            path = REPOSITORY / PurePosixPath(relative)
            if path.is_file() and path.resolve() != Path(__file__).resolve():
                path.unlink()
        for directory in sorted(
            (path for path in REPOSITORY.rglob("*") if path.is_dir()),
            key=lambda path: len(path.parts),
            reverse=True,
        ):
            try:
                directory.rmdir()
            except OSError:
                pass

    def build(self) -> None:
        self._remove_prior_generated_files()
        self.provenance = {}
        current_hashes = self._frozen_hashes()
        if self.baseline and self.baseline.get("files") != current_hashes:
            raise SystemExit("Frozen contract registries differ from recorded repository build baseline.")
        self._write_core()
        self._write_project_state()
        self._write_skills()
        self._write_language()
        self._write_seedance()
        self._write_source_evidence()
        self._write_validation_metadata(current_hashes)
        self._write_readme()
        self._write_builder_copy()
        self._write_manifest()
        self.validate()

    def _frozen_hashes(self) -> dict[str, str]:
        result = {}
        for relative in FROZEN_FILES:
            path = PRODUCTION / PurePosixPath(relative)
            if not path.is_file():
                raise FileNotFoundError(f"Frozen registry missing: {relative}")
            result[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        return result

    def _write_core(self) -> None:
        docs = {
            "00_CORE/CORE_CONTRACTS.md": """# Gemini Tab 2 portable core contracts

**Status:** reference-only; not loaded into production.

The production repository is the source of truth. This independent package
exports evidence and portable instructions but does not become runtime
authority. Frozen Writer/Director contracts, Story Memory, Production Canon,
DirectorHandoffV2, PromptFacade/PromptEngine, and deterministic validators
remain production-owned.

Preserve this authority order exactly:

`SOURCE > STORY MEMORY > PRODUCTION CANON > WRITER WHAT > VISUAL COMPLETION > ACTION INTERPRETER > ACTION CHOREOGRAPHY > DIRECTOR HOW > SEEDANCE ADAPTER > PROMPT ENGINE > QUALITY AUDIT`

The intervening visual/action layers are portable proposals, not production
authorities. Writer WHAT is immutable downstream. Gemini may prepare a
user-reviewed prompt draft but must never claim it is the production
PromptEngine final prompt.

Sources: `source_evidence/architecture/TAB2_FROZEN_CONTRACTS.md`,
`source_evidence/architecture/TAB2_DATA_AUTHORITY.md`.
""",
            "00_CORE/DATA_AUTHORITY.md": """# Data authority

| Data | Authority | Gemini package boundary |
|---|---|---|
| Novel/source text and provenance | Source document | Cite and preserve exact evidence |
| Persisted identity, facts, knowledge and temporal visibility | StoryMemoryService / repository | Portable copy is not persisted Story Memory |
| Cross-chapter continuity/Production Canon | FullStoryContinuityAnalyzer derived gate | Do not promote its report to persisted source |
| Story events, identity, exact dialogue, relationship and outcome | Writer / ScreenplayApplicationService | Downstream is read-only |
| Visual-completion/action/choreography proposal | Portable reference layers only | Cannot change story state or imply production acceptance |
| Cinematic HOW | DirectorFacade / canonical Director workflow | Cannot mutate Writer WHAT |
| Final prompt text | PromptFacade → PromptEngine | Seedance portable `prompt_draft` is not a final production prompt |
| Visual style | Explicit project user preference | `PROJECT_VISUAL_PROFILE` is not Story Memory |
| Technical and spoken language preferences | Explicit project language preference | `PROJECT_LANGUAGE_PROFILE` is portable and distinct from Story Memory |
| Dola tag behavior | Current Dola UI only when confirmed | Unknown means REFERENCE_BINDING_UNVERIFIED |

Production reference: `source_evidence/architecture/TAB2_DATA_AUTHORITY.md`.
""",
            "00_CORE/WORKFLOW.md": """# Gemini Tab 2 portable workflow

`INGEST → STORY MEMORY → CONTINUITY → WRITER → ENRICHMENT → VISUAL COMPLETION → ACTION INTERPRETER → ACTION CHOREOGRAPHY → DIRECTOR → SEEDANCE DRAFT → PROMPT ENGINE AUTHORITY CHECK → QUALITY AUDIT`

Before Gemini video-prompt work, check `PROJECT_VISUAL_PROFILE` and
`PROJECT_LANGUAGE_PROFILE`. If absent or unresolved, return the corresponding
unresolved status, ask the user, and stop prompt drafting. Technical prompt
language is independent from dialogue, internal-monologue, voice-over and
on-screen-text language. The portable chibi reference may add a short symbolic
insert only when the profile allows it.
The optional portable layers do not change the production canonical flow:
they add reference guidance after accepted Writer WHAT and before Director
HOW. Production enrichment remains governed by its existing production gate.

Advance only with required evidence and a valid stage output. BLOCKED or
UNRESOLVED is not success. The PromptEngine authority check means either use
the production facade in production or clearly label a Gemini result as a
portable draft; Gemini Web alone cannot claim that production validation ran.

Production call graph: `source_evidence/architecture/TAB2_CALL_GRAPH.md`.
See `workflow/STAGE_TRANSITIONS.json` for explicit portable stage gates and
narrow return destinations. This expanded portable sequence must not be
represented as a changed production runtime call graph.
""",
            "00_CORE/CREATIVE_BOUNDARY.md": """# Creative boundary

**PRESERVE STORY TRUTH STRICTLY. REALIZE MISSING VISUAL DETAILS FLEXIBLY.
INVENT NO NEW NARRATIVE STATE.**

## Hard lock

Story facts; canonical identity; relationships; character knowledge and
future visibility; important location and props; source dialogue; events;
outcome and state.

## Soft / creative presentation

Gaze, breathing, posture, supported body movement, blocking, reaction,
secondary motion, framing, camera, pacing, timeline, optional choreography,
and style-compliant VFX.

Every added detail must identify its origin (`SOURCE_EXPLICIT`,
`SAFE_VISUAL_INFERENCE`, or `DIRECTOR_CREATIVE_CHOICE`), source references
where applicable, and `changes_story_state: false`. A state-changing or
unsupported detail is rejected. Do not use fixed emotion-to-gesture rules.

See `skills/04b-visual-completion/` and `skills/08-seedance/`.
""",
            "00_CORE/FAILURE_RULES.md": """# Fail-closed outcomes

- Missing/ambiguous identity, source, visibility or actor: `UNRESOLVED`.
- Unknown or future visibility: do not use; stop downstream advancement.
- Continuity or Writer readiness blocker: preserve status and return to the
  responsible production boundary; do not manufacture a ready result.
- Missing user-selected visual style: `STYLE_UNRESOLVED`, ask and stop.
- Unknown Dola image/video tag syntax: `REFERENCE_BINDING_UNVERIFIED`; emit
  no invented tag or prompt row suitable for copying.
- Unresolved `PROJECT_LANGUAGE_PROFILE`: stop before language-sensitive draft.
- Translation or mutation of source dialogue/internal monologue: reject.
- Chibi disabled, diegetic symbolic action, or missing scene return: block.
- Unsupported action subtype: retain ambiguity or `UNRESOLVED`.
- Story-state-changing visual detail, VFX, or choreography: reject.
- A blocked/unresolved sheet row has an empty prompt.

These portable outcomes do not replace executable production gates.
""",
            "00_CORE/GEMINI_OPERATING_RULES.md": """# Gemini Pro operating rules

1. Treat this repository as a read-only reference package; production code,
   frozen contracts and persisted authorities remain the source of truth.
2. Resolve user-selected project style before prompt drafting. Never infer it.
3. Preserve story truth, identity, relationships, knowledge, dialogue and
   outcome. Do not guess missing evidence.
4. Keep source facts, visual proposals, Director HOW, model formatting and
   platform UI syntax in separate fields.
5. Ask the user when this package explicitly requires a preference; do not
   silently choose a preset.
6. Keep technical prompt language separate from each typed speech language;
   preserve source speech/monologue verbatim and do not invent words.
7. Treat chibi as an optional non-diegetic insert with no story-state effect;
   return to the same main-scene continuity.
8. Use only current UI-confirmed Dola tags. Unknown syntax blocks binding.
9. Do not present a portable draft or checklist result as production
   PromptEngine, readiness, or Gemini quality certification.
10. Cite source references and report known gaps instead of inventing
   production behavior.

No live provider calls or external APIs are part of this repository builder.
""",
        }
        for target, content in docs.items():
            self.write(
                target,
                content,
                sources=[
                    "architecture/TAB2_FROZEN_CONTRACTS.md",
                    "architecture/TAB2_DATA_AUTHORITY.md",
                    "architecture/TAB2_CALL_GRAPH.md",
                ],
                schema_version="GEMINI_CORE_REFERENCE_V1",
            )
        transitions = {
            "workflow_id": "GEMINI_TAB2_PORTABLE_REFERENCE_V1",
            "runtime_authority": False,
            "stages": [
                ["INGEST", "source text and project id", "source refs and initial state", "unreadable source or missing id", "INGEST"],
                ["STORY_MEMORY", "source refs and visible chapter boundary", "identity/facts/knowledge with provenance and visibility", "ambiguous identity or unsupported extraction", "INGEST"],
                ["CONTINUITY", "Story Memory and current chapter", "derived continuity/readiness result", "future visibility or unresolved contradiction", "STORY_MEMORY"],
                ["WRITER", "source, visible Story Memory, continuity gate", "WHAT scene and readiness/handoff status", "missing evidence or blocked readiness", "STORY_MEMORY or CONTINUITY"],
                ["ENRICHMENT", "accepted Writer scene", "conditionally accepted grounded enrichment or NONE", "unsupported addition", "WRITER"],
                ["VISUAL_COMPLETION", "accepted scene and visible context", "bounded non-state-changing visual proposal", "identity/context unresolved or state change", "WRITER"],
                ["ACTION_INTERPRETER", "source-backed action and resolved actor", "supported action class or UNRESOLVED", "unsupported target/subtype/outcome", "WRITER"],
                ["ACTION_CHOREOGRAPHY", "resolved action class and current visible context", "optional supported physical phases", "any unsupported story/physical outcome", "ACTION_INTERPRETER"],
                ["DIRECTOR", "accepted Writer WHAT and bounded read-only context", "HOW plan under production Director authority", "missing handoff or authority conflict", "WRITER"],
                ["SEEDANCE_DRAFT", "accepted scene, HOW, resolved user style and confirmed references", "portable prompt_draft and sheet row", "STYLE_UNRESOLVED or REFERENCE_BINDING_UNVERIFIED", "STYLE_INTAKE or DIRECTOR"],
                ["PROMPT_ENGINE_AUTHORITY_CHECK", "portable draft or production facade result", "labelled portable draft OR production final prompt", "Gemini claims production compile without facade", "DIRECTOR"],
                ["QUALITY_AUDIT", "all required stage statuses and output", "PASS or BLOCKED/UNRESOLVED with trace refs", "any failed gate or missing provenance", "responsible failed stage"],
            ],
            "return_rules": [
                {"condition": "source/provenance missing", "return_to": "INGEST", "retain": "no downstream claims"},
                {"condition": "identity, knowledge or temporal visibility unresolved", "return_to": "STORY_MEMORY", "retain": "accepted source and upstream state only"},
                {"condition": "continuity/readiness blocker", "return_to": "CONTINUITY", "retain": "Story Memory as authority"},
                {"condition": "Writer WHAT/readiness unsupported", "return_to": "WRITER", "retain": "accepted source and visible memory"},
                {"condition": "visual/action proposal adds state", "return_to": "WRITER", "retain": "accepted upstream outputs; discard proposal"},
                {"condition": "style unresolved", "return_to": "STYLE_INTAKE", "retain": "all prior accepted content"},
                {"condition": "reference binding unverified", "return_to": "REFERENCE_CONFIRMATION", "retain": "reference files and roles, no tags"},
                {"condition": "portable prompt structure invalid", "return_to": "SEEDANCE_DRAFT", "retain": "Writer WHAT and Director HOW"},
            ],
            "visibility": {
                "as_of": "explicit current chapter/scene boundary",
                "future_facts": "BLOCKED",
                "unknown_or_missing_visibility": "UNRESOLVED",
                "do_not_advance_on_blocked_or_unresolved": True,
            },
            "note": "Portable guidance only. Production gates and return semantics are enforced by production code and frozen contracts.",
        }
        self.write(
            "workflow/STAGE_TRANSITIONS.json",
            json.dumps(transitions, ensure_ascii=False, indent=2, sort_keys=True),
            sources=["architecture/TAB2_CALL_GRAPH.md", "architecture/TAB2_FROZEN_CONTRACTS.md", "architecture/TAB2_DATA_AUTHORITY.md"],
            schema_version="GEMINI_TAB2_PORTABLE_REFERENCE_V1",
            gaps=["Portable stage list extends labels for reference-only visual/action layers; it is not a changed production runtime pipeline."],
        )

    def _write_project_state(self) -> None:
        template_source = "dist/common/project-template"
        schema_source = "dist/common/schemas"
        for name in (
            "PROJECT_STATE.json",
            "PROJECT_VISUAL_PROFILE.json",
            "STORY_MEMORY.json",
            "CHARACTERS.json",
            "RELATIONSHIPS.json",
            "KNOWLEDGE.json",
            "EVENTS.json",
            "OPEN_THREADS.json",
            "CHAPTER_STATUS.json",
        ):
            self.copy_file(
                f"{template_source}/{name}",
                f"project_state/templates/{name}",
                schema_version="PORTABLE_WEB_STATE_ONLY",
                gaps=["Template is not a production DTO or persistence authority."],
            )
            if name == "PROJECT_STATE.json":
                target = REPOSITORY / "project_state/templates/PROJECT_STATE.json"
                instance = json.loads(target.read_text(encoding="utf-8"))
                instance["project_language_profile_ref"] = "PROJECT_LANGUAGE_PROFILE.json"
                self.write(
                    "project_state/templates/PROJECT_STATE.json",
                    json.dumps(instance, ensure_ascii=False, indent=2, sort_keys=True),
                    sources=[f"{template_source}/PROJECT_STATE.json", "skills/language-policy/PROJECT_LANGUAGE_PROFILE.template.json"],
                    schema_version="PORTABLE_WEB_STATE_ONLY",
                    gaps=["Portable template and profile reference; not production persistence."],
                )
            elif name == "PROJECT_VISUAL_PROFILE.json":
                target = REPOSITORY / "project_state/templates/PROJECT_VISUAL_PROFILE.json"
                instance = json.loads(target.read_text(encoding="utf-8"))
                instance["full_chibi_scene"] = False
                self.write(
                    "project_state/templates/PROJECT_VISUAL_PROFILE.json",
                    json.dumps(instance, ensure_ascii=False, indent=2, sort_keys=True),
                    sources=[f"{template_source}/PROJECT_VISUAL_PROFILE.json", "skills/04e-chibi-performance/manifest.yaml"],
                    schema_version="PORTABLE_WEB_STATE_ONLY",
                    gaps=["full_chibi_scene defaults to false; an enabled full-scene mode requires explicit user selection."],
                )
        for name in (
            "story_memory_state.schema.json",
            "project_visual_profile.schema.json",
        ):
            self.copy_file(
                f"{schema_source}/{name}",
                f"project_state/schemas/{name}",
                schema_version=name,
                gaps=["Portable interchange schema; production validators remain authoritative."],
            )
            if name == "project_visual_profile.schema.json":
                self._augment_full_chibi_profile_schema(
                    "project_state/schemas/project_visual_profile.schema.json",
                    [
                        f"{schema_source}/project_visual_profile.schema.json",
                        "skills/04e-chibi-performance/manifest.yaml",
                    ],
                )
        collection_schemas = {
            "project_state.schema.json": ("project_state", "project_id", "source_document_refs"),
            "characters.schema.json": ("characters", "characters", "rule"),
            "relationships.schema.json": ("relationships", "relationships", "rule"),
            "knowledge.schema.json": ("knowledge", "knowledge", "rule"),
            "events.schema.json": ("events", "events", "rule"),
            "open_threads.schema.json": ("open_threads", "open_threads", "rule"),
            "chapter_status.schema.json": ("chapter_status", "chapters", "rule"),
        }
        for filename, (title, collection_key, auxiliary_key) in collection_schemas.items():
            if filename == "project_state.schema.json":
                schema = {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "$id": "PORTABLE_PROJECT_STATE_V1",
                    "type": "object",
                    "additionalProperties": True,
                    "properties": {
                        "state_scope": {"const": "PORTABLE_WEB_STATE_ONLY"},
                        "project_id": {"type": "string"},
                        "current_chapter_order": {"type": ["integer", "null"], "minimum": 1},
                        "current_scene_id": {"type": ["string", "null"]},
                        "stage": {"type": "string"},
                        "visibility_filter_status": {"enum": ["PASS", "BLOCKED", "UNRESOLVED"]},
                        "source_document_refs": {"type": "array", "items": {"type": "string"}},
                        "project_visual_profile_ref": {"type": "string"},
                        "project_language_profile_ref": {"type": "string"},
                    },
                    "required": ["state_scope", "project_id", "current_chapter_order", "current_scene_id", "stage", "visibility_filter_status", "source_document_refs", "project_language_profile_ref"],
                }
            else:
                schema = {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "$id": f"PORTABLE_{title.upper()}_COLLECTION_V1",
                    "title": f"Portable {title} collection",
                    "type": "object",
                    "additionalProperties": True,
                    "properties": {
                        "state_scope": {"const": "PORTABLE_WEB_STATE_ONLY"},
                        collection_key: {"type": "array", "items": {"type": "object"}},
                        auxiliary_key: {"type": "string"},
                    },
                    "required": ["state_scope", collection_key],
                }
            self.write(
                f"project_state/schemas/{filename}",
                json.dumps(schema, ensure_ascii=False, indent=2, sort_keys=True),
                sources=[
                    f"{template_source}/{self._template_for_schema(title)}",
                    "dist/build_distribution.py",
                ],
                schema_version=schema["$id"],
                gaps=["Portable permissive collection schema; does not claim equivalence to a production DTO."],
            )
        self.write(
            "project_state/README.md",
            """# Portable project state

All templates use `PORTABLE_WEB_STATE_ONLY`. `PROJECT_VISUAL_PROFILE.json` is
a user preference separate from `STORY_MEMORY.json`; the initial style status
is unresolved. `PROJECT_LANGUAGE_PROFILE.json` separately holds user-selected
technical prompt, dialogue, monologue and voice-over language preferences.
Project files are user-managed Gemini working state, not production
persistence or Story Memory.

Collection schemas intentionally remain permissive for record internals
because the production project templates do not define a frozen per-record
DTO for every file. Use the linked production authority and source references;
do not infer missing fields as facts.
""",
            sources=["dist/common/project-template/README.md", "dist/build_distribution.py"],
            schema_version="PORTABLE_PROJECT_STATE_V1",
        )

    @staticmethod
    def _template_for_schema(title: str) -> str:
        return {
            "project_state": "PROJECT_STATE.json",
            "characters": "CHARACTERS.json",
            "relationships": "RELATIONSHIPS.json",
            "knowledge": "KNOWLEDGE.json",
            "events": "EVENTS.json",
            "open_threads": "OPEN_THREADS.json",
            "chapter_status": "CHAPTER_STATUS.json",
        }[title]

    def _write_skills(self) -> None:
        source_dirs = {name: source for name, source, _ in SKILL_EXPORTS}
        for target_name, source_name, source_manifest_path in SKILL_EXPORTS:
            source_manifest = PRODUCTION / source_manifest_path
            manifest = self._read_skill_manifest(source_manifest)
            version = manifest.get("version", "UNKNOWN")
            target_dir = f"skills/{target_name}"
            if target_name == "08-seedance":
                skill_text = self._skill_wrapper(target_name, manifest)
                self.write(
                    f"{target_dir}/SKILL.md",
                    skill_text,
                    sources=[source_manifest_path, "skills/08-seedance/SKILL.md", "architecture/TAB2_MODEL_ADAPTERS.md"],
                    skill_version=version,
                    schema_version="SEEDANCE_PROMPT_CONTRACT_V1",
                    gaps=CAPABILITIES[10]["known_gaps"],
                )
                self.write(
                    f"{target_dir}/manifest.json",
                    self._portable_skill_manifest(target_name, manifest, source_manifest_path),
                    sources=[source_manifest_path],
                    skill_version=version,
                    schema_version="PORTABLE_SKILL_MANIFEST_V1",
                )
                continue
            if target_name in {"04b-visual-completion", "04c-action-interpreter", "04d-action-choreography"}:
                self.copy_tree(
                    f"skills/{source_name}",
                    target_dir,
                    skill_version=version,
                    skip_names={"portable_validator.py"},
                )
                self.write(
                    f"{target_dir}/SKILL.md",
                    self._skill_wrapper(target_name, manifest),
                    sources=[source_manifest_path, f"skills/{source_name}/SKILL.md"],
                    skill_version=version,
                    schema_version=manifest.get("schema_version", "not_applicable"),
                    gaps=self._capability(target_name)["known_gaps"],
                )
                continue
            if target_name == "04e-chibi-performance":
                self.copy_tree(
                    f"skills/{source_name}",
                    target_dir,
                    skill_version=version,
                )
                self.write(
                    f"{target_dir}/manifest.json",
                    self._portable_skill_manifest(target_name, manifest, source_manifest_path),
                    sources=[source_manifest_path],
                    skill_version=version,
                    schema_version="CHIBI_PERFORMANCE_REFERENCE_V1",
                    gaps=self._capability(target_name)["known_gaps"],
                )
                continue
            if target_name == "09-style-resolution":
                self.copy_tree(
                    "skills/09-style-resolution",
                    target_dir,
                    skill_version=version,
                )
                self.write(
                    f"{target_dir}/SKILL.md",
                    self._skill_wrapper(target_name, manifest),
                    sources=[source_manifest_path, "skills/09-style-resolution/SKILL.md"],
                    skill_version=version,
                    schema_version="PROJECT_VISUAL_PROFILE_V1",
                    gaps=self._capability(target_name)["known_gaps"],
                )
                self._augment_full_chibi_profile_schema(
                    f"{target_dir}/PROJECT_VISUAL_PROFILE.schema.json",
                    [
                        "skills/09-style-resolution/PROJECT_VISUAL_PROFILE.schema.json",
                        "skills/04e-chibi-performance/manifest.yaml",
                    ],
                    skill_version=version,
                )
                questionnaire_path = REPOSITORY / target_dir / "style_questionnaire.yaml"
                questionnaire = questionnaire_path.read_text(encoding="utf-8")
                if "id: full_chibi_scene" not in questionnaire:
                    marker = '  - id: chibi_insertions\n    required: true\n    prompt: "Should brief nonverbal chibi reaction inserts be allowed?"\n    options: [true, false]\n'
                    added = marker + '  - id: full_chibi_scene\n    required: false\n    prompt: "Should the entire scene be chibi rather than using only brief inserts?"\n    options: [true, false]\n    default: false\n'
                    if marker not in questionnaire:
                        raise ValueError("Could not add explicit full_chibi_scene choice to style questionnaire.")
                    questionnaire = questionnaire.replace(marker, added, 1)
                    self.write(
                        f"{target_dir}/style_questionnaire.yaml",
                        questionnaire,
                        sources=["skills/09-style-resolution/style_questionnaire.yaml", "skills/04e-chibi-performance/manifest.yaml"],
                        skill_version=version,
                        schema_version="STYLE_RESOLUTION_QUESTIONNAIRE_V1",
                    )
                continue
            # Core stage exports use the already-generated Gemini package, which
            # contains portable examples, stage schemas, source traces and maps.
            dist_id = source_dirs[target_name]
            self.copy_tree(
                f"dist/gemini/{dist_id}",
                target_dir,
                skill_version=version,
                skip_names={"portable_validator.py"},
            )
            original_skill = PRODUCTION / "dist" / "gemini" / dist_id / "SKILL.md"
            if not original_skill.is_file():
                raise FileNotFoundError(f"Gemini skill package missing: {dist_id}/SKILL.md")
            core_skill = self._standard_core_skill(target_name, manifest, original_skill)
            if target_name == "07-quality-audit":
                core_skill += (
                    "\n\n## LANGUAGE AND CHIBI PORTABLE CHECKS\n\n"
                    "Apply the reference checks in `LANGUAGE_CHIBI_RULES.yaml` "
                    "to portable drafts. These checks do not replace production "
                    "validators or certify Gemini output."
                )
            self.write(
                f"{target_dir}/source_skill.md",
                original_skill.read_bytes(),
                sources=[f"dist/gemini/{dist_id}/SKILL.md"],
                skill_version=version,
            )
            self.write(
                f"{target_dir}/SKILL.md",
                core_skill,
                sources=[
                    source_manifest_path,
                    f"dist/gemini/{dist_id}/SKILL.md",
                ] + (["skills/04e-chibi-performance/constraints/quality_audit.yaml"] if target_name == "07-quality-audit" else []),
                skill_version=version,
                schema_version=manifest.get("schema_version", "not_applicable"),
                gaps=self._capability(target_name)["known_gaps"],
            )
            self.write(
                f"{target_dir}/manifest.json",
                self._portable_skill_manifest(target_name, manifest, source_manifest_path),
                sources=[source_manifest_path, f"dist/gemini/{dist_id}/manifest.yaml"],
                skill_version=version,
                schema_version=manifest.get("schema_version", "not_applicable"),
                gaps=self._capability(target_name)["known_gaps"],
            )
            if target_name == "07-quality-audit":
                self.copy_file(
                    "skills/04e-chibi-performance/constraints/quality_audit.yaml",
                    f"{target_dir}/LANGUAGE_CHIBI_RULES.yaml",
                    skill_version="1.0.0",
                    schema_version="LANGUAGE_CHIBI_PORTABLE_AUDIT_V1",
                    gaps=["Portable reference checks only; not production validators."],
                )

    def _standard_core_skill(self, skill_name: str, manifest: dict, path: Path) -> str:
        text = path.read_text(encoding="utf-8")
        sections: dict[str, str] = {}
        current = None
        for line in text.splitlines():
            heading = re.match(r"^##\s+(.+?)\s*$", line)
            if heading:
                current = heading.group(1).strip().upper()
                sections[current] = ""
            elif current:
                sections[current] += line + "\n"
        aliases = {
            "ROLE": ("ROLE",),
            "AUTHORITY": ("AUTHORITY",),
            "INPUT": ("INPUT",),
            "OUTPUT": ("OUTPUT",),
            "WORKFLOW": ("WORKFLOW",),
            "ALLOWED": ("ALLOWED",),
            "FORBIDDEN": ("FORBIDDEN",),
            "FAIL CONDITIONS": ("FAIL CONDITIONS",),
            "VALIDATION": ("VALIDATION",),
            "NEXT STAGE": ("NEXT STAGE",),
            "REFERENCES": ("REFERENCES", "REFERENCE FILES"),
        }
        title = skill_name.replace("-", " ").title()
        lines = [f"# {title} — Gemini-facing portable stage reference"]
        for required, candidates in aliases.items():
            content = next((sections[key].strip() for key in candidates if sections.get(key, "").strip()), "")
            if not content and required == "ROLE":
                content = sections.get("PURPOSE", "").strip()
            if not content and required == "REFERENCES":
                content = "See the source skill and `manifest.json` for traceable sources and tests."
            if not content:
                content = "No additional behavior is claimed beyond the cited production contract, source skill, and tests."
            lines.extend([f"\n## {required}\n\n{content}"])
        lines.extend([
            "\n## STATUS",
            f"\n\n{PORTABLE}; source skill version {manifest['version']}; "
            f"schema identity `{manifest['schema_version']}`. Not runtime-loaded.",
        ])
        return "\n".join(lines)

    @staticmethod
    def _read_skill_manifest(path: Path) -> dict:
        text = path.read_text(encoding="utf-8")
        def scalar(name: str) -> str:
            found = re.search(rf"^{re.escape(name)}:\s*(.*?)\s*$", text, re.M)
            if not found:
                return "UNKNOWN"
            return found.group(1).strip().strip('"')
        return {
            "skill_id": scalar("skill_id"),
            "version": scalar("version"),
            "owner": scalar("owner"),
            "authority": scalar("authority"),
            "schema_version": scalar("schema_version"),
            "prompt_version": scalar("prompt_version"),
        }

    def _portable_skill_manifest(self, package: str, source_manifest: dict, source_path: str) -> str:
        capability = self._capability(package)
        data = {
            "id": package,
            "source_skill_id": source_manifest["skill_id"],
            "source_skill_version": source_manifest["version"],
            "distribution_version": VERSION,
            "schema_version": source_manifest["schema_version"],
            "status": PORTABLE,
            "source_skill_manifest": source_path,
            "production_sources": capability["production_sources"],
            "related_tests": capability["tests"],
            "known_gaps": capability["known_gaps"],
            "runtime_loaded": False,
        }
        return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)

    def _augment_full_chibi_profile_schema(
        self,
        target_relative: str,
        sources: list[str],
        *,
        skill_version: str | None = None,
    ) -> None:
        path = REPOSITORY / PurePosixPath(target_relative)
        schema = json.loads(path.read_text(encoding="utf-8"))
        schema.setdefault("properties", {})["full_chibi_scene"] = {
            "type": ["boolean", "null"],
            "default": False,
        }
        for rule in schema.get("allOf", []):
            if rule.get("if", {}).get("properties", {}).get("profile_status", {}).get("const") == "RESOLVED":
                rule.setdefault("then", {}).setdefault("properties", {})["full_chibi_scene"] = {
                    "type": "boolean",
                }
                break
        self.write(
            target_relative,
            json.dumps(schema, ensure_ascii=False, indent=2, sort_keys=True),
            sources=sources,
            skill_version=skill_version,
            schema_version="PROJECT_VISUAL_PROFILE_V1",
            gaps=["The optional full-scene chibi flag is a portable preference and defaults false; it is not a production contract."],
        )

    @staticmethod
    def _capability(skill_name: str) -> dict:
        map_ids = {
            "00-orchestrator": "production-authority-and-workflow",
            "01-story-memory": "story-memory-identity-provenance-temporal-visibility",
            "02-continuity": "production-continuity-canon-gate",
            "03-writer": "writer-what-readiness-and-handoff",
            "04-enrichment": "writer-enrichment-deterministic-grounding",
            "04b-visual-completion": "visual-completion",
            "04c-action-interpreter": "action-interpreter",
            "04d-action-choreography": "action-choreography",
            "04e-chibi-performance": "chibi-inner-monologue-symbolic-performance",
            "05-director": "director-how-and-advisory-skills",
            "06-prompt-engine": "promptengine-seedance-formatting",
            "07-quality-audit": "quality-audit-and-frozen-regression",
            "08-seedance": "promptengine-seedance-formatting",
            "09-style-resolution": "style-resolution-user-intake",
            "language-policy": "portable-project-language-profile-and-typed-speech",
        }
        return next(row for row in CAPABILITIES if row["id"] == map_ids[skill_name])

    def _write_language(self) -> None:
        source_root = "skills/language-policy"
        manifest = self._read_skill_manifest(PRODUCTION / source_root / "manifest.yaml")
        self.copy_tree(
            source_root,
            "language",
            skill_version=manifest["version"],
        )
        self.copy_file(
            f"{source_root}/PROJECT_LANGUAGE_PROFILE.schema.json",
            "language/PROJECT_LANGUAGE_PROFILE.schema.json",
            skill_version=manifest["version"],
            schema_version="PROJECT_LANGUAGE_PROFILE_V1",
            gaps=self._capability("language-policy")["known_gaps"],
        )
        self.copy_file(
            f"{source_root}/PROJECT_LANGUAGE_PROFILE.template.json",
            "project_state/templates/PROJECT_LANGUAGE_PROFILE.json",
            skill_version=manifest["version"],
            schema_version="PROJECT_LANGUAGE_PROFILE_V1",
            gaps=["Portable project preference only; not production persistence."],
        )
        self.write(
            "language/manifest.json",
            json.dumps(
                {
                    "id": "language-policy",
                    "source_skill_id": manifest["skill_id"],
                    "source_skill_version": manifest["version"],
                    "distribution_version": VERSION,
                    "schema_version": "PROJECT_LANGUAGE_PROFILE_V1",
                    "status": PORTABLE,
                    "source_skill_manifest": f"{source_root}/manifest.yaml",
                    "production_sources": self._capability("language-policy")["production_sources"],
                    "related_tests": self._capability("language-policy")["tests"],
                    "known_gaps": self._capability("language-policy")["known_gaps"],
                    "runtime_loaded": False,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            sources=[f"{source_root}/manifest.yaml"],
            skill_version=manifest["version"],
            schema_version="PORTABLE_LANGUAGE_MANIFEST_V1",
            gaps=self._capability("language-policy")["known_gaps"],
        )

    def _skill_wrapper(self, skill_name: str, manifest: dict) -> str:
        sections = SKILL_SECTIONS[skill_name]
        title = skill_name.replace("-", " ").title()
        output = [f"# {title} — Gemini-facing portable reference"]
        for heading in (
            "ROLE", "AUTHORITY", "INPUT", "OUTPUT", "WORKFLOW", "ALLOWED",
            "FORBIDDEN", "FAIL CONDITIONS", "VALIDATION", "NEXT STAGE", "REFERENCES",
        ):
            output.append(f"\n## {heading}\n\n{sections[heading]}")
        output.extend([
            "\n## STATUS",
            f"\n\n{PORTABLE}; source skill version {manifest['version']}; "
            f"schema identity `{manifest['schema_version']}`. Not runtime-loaded.",
        ])
        return "\n".join(output)

    def _write_seedance(self) -> None:
        base_source = "skills/08-seedance"
        manifest = self._read_skill_manifest(PRODUCTION / base_source / "manifest.yaml")
        self.copy_tree(
            base_source,
            "seedance",
            skill_version=manifest["version"],
            skip_names={"SKILL.md", "manifest.yaml", "portable_validator.py"},
        )
        self._augment_seedance_language_chibi_schema(manifest)
        self.copy_file(
            "model_profiles/seedance.json",
            "seedance/evidence/seedance_profile_summary_source.json",
            skill_version=manifest["version"],
            schema_version="production-model-profile-evidence",
            gaps=["Copied source profile is reference evidence only; it does not prove provider capability."],
        )
        self.copy_file(
            "prompt_templates/seedance.json",
            "seedance/evidence/seedance_template_evidence.json",
            skill_version=manifest["version"],
            schema_version="production-prompt-template-evidence",
            gaps=["Template evidence is not a Gemini-generated prompt or generation API guarantee."],
        )
        self.copy_file(
            "skills/08-seedance/SKILL.md",
            "seedance/README.md",
            skill_version=manifest["version"],
            schema_version="SEEDANCE_PROMPT_CONTRACT_V1",
        )
        self.copy_file(
            "skills/04e-chibi-performance/examples/good/vi_chibi_inner_monologue.yaml",
            "seedance/examples/good/vi_chibi_inner_monologue.yaml",
            skill_version=manifest["version"],
            schema_version="PORTABLE_SYNTHETIC_EXAMPLE_V1",
            gaps=["Synthetic portable example; not production or observed Gemini output."],
        )
        self.write(
            "seedance/PROMPT_CONTRACT.yaml",
            """contract_id: SEEDANCE_PROMPT_CONTRACT_V1
version: 1.0.0
status: PORTABLE_PROMPT_DRAFT_ONLY
production_authority: PromptFacade_then_PromptEngine
required_sections:
  - REFERENCE
  - WHO
  - STYLE
  - WHERE
  - CAMERA
  - WHEN
  - WHAT
  - HOW
  - TECHNICAL_INSTRUCTIONS
  - SPOKEN_DIALOGUE
  - INTERNAL_MONOLOGUE
  - NARRATOR_VOICE_OVER
  - ON_SCREEN_TEXT
  - VFX
  - END_STATE
language_policy:
  technical_instructions_language: PROJECT_LANGUAGE_PROFILE.prompt_language
  spoken_language: independent_from_prompt_language
  source_dialogue: preserve_verbatim_and_never_translate
  source_internal_monologue: preserve_verbatim_and_never_translate
rules:
  - "No internal reasoning in prompt_draft."
  - "Never mutate Writer WHAT."
  - "Never invent dialogue or internal monologue."
  - "No draft while PROJECT_VISUAL_PROFILE is unresolved."
  - "No draft while PROJECT_LANGUAGE_PROFILE is unresolved."
  - "Unknown Dola binding syntax means REFERENCE_BINDING_UNVERIFIED."
  - "A portable prompt_draft is not production PromptEngine output."
chibi_insert:
  symbolic_namespace: CHIBI_SYMBOLIC_ACTION
  representation_scope: NON_DIEGETIC
  story_state_effect: NONE
  returns_to_main_scene: required
""",
            sources=["skills/08-seedance/prompt_structure/seedance_prompt_v1.yaml", "skills/language-policy/LANGUAGE_POLICY.md", "skills/04e-chibi-performance/SKILL.md", "architecture/TAB2_MODEL_ADAPTERS.md"],
            skill_version=manifest["version"],
            schema_version="SEEDANCE_PROMPT_CONTRACT_V1",
            gaps=["Additional rendered sections are portable guidance; production formatter owns its compiled section behavior."],
        )

    def _augment_seedance_language_chibi_schema(self, manifest: dict) -> None:
        skill_version = manifest["version"]
        relative = "seedance/schemas/seedance_scene_package.schema.json"
        path = REPOSITORY / relative
        schema = json.loads(path.read_text(encoding="utf-8"))
        properties = schema.setdefault("properties", {})
        properties.update({
            "language_profile_ref": {"type": ["string", "null"]},
            "spoken_dialogue": {"type": "array", "items": {"$ref": "#/$defs/spokenDialogue"}},
            "internal_monologue": {"type": "array", "items": {"$ref": "#/$defs/internalMonologue"}},
            "voice_over": {"type": "array", "items": {"$ref": "#/$defs/narratorVoiceOver"}},
            "on_screen_text": {"type": "array", "items": {"$ref": "#/$defs/onScreenText"}},
            "nonverbal_reaction": {"type": "array", "items": {"$ref": "#/$defs/nonverbalReaction"}},
            "chibi_insert": {"$ref": "#/$defs/chibiInsert"},
        })
        definitions = schema.setdefault("$defs", {})
        definitions["typedExpression"] = {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "type": {"enum": ["SPOKEN_DIALOGUE", "INTERNAL_MONOLOGUE", "NARRATOR_VOICE_OVER", "NONVERBAL_REACTION", "ON_SCREEN_TEXT"]},
                "source_text": {"type": ["string", "null"]},
                "language": {"type": ["string", "null"]},
                "source_refs": {"type": "array", "items": {"type": "string"}},
                "preserve_verbatim": {"type": "boolean"},
            },
            "required": ["type", "source_text", "language", "source_refs", "preserve_verbatim"],
        }
        for name, category in (
            ("spokenDialogue", "SPOKEN_DIALOGUE"),
            ("internalMonologue", "INTERNAL_MONOLOGUE"),
            ("narratorVoiceOver", "NARRATOR_VOICE_OVER"),
            ("onScreenText", "ON_SCREEN_TEXT"),
        ):
            definitions[name] = {
                "allOf": [
                    {"$ref": "#/$defs/typedExpression"},
                    {"properties": {
                        "type": {"const": category},
                        "source_text": {"type": "string"},
                        "language": {"type": "string"},
                        "preserve_verbatim": {"const": True},
                    }},
                ]
            }
        definitions["nonverbalReaction"] = {
            "allOf": [
                {"$ref": "#/$defs/typedExpression"},
                {"properties": {
                    "type": {"const": "NONVERBAL_REACTION"},
                    "source_text": {"type": "null"},
                    "language": {"type": "null"},
                    "preserve_verbatim": {"const": False},
                }},
            ]
        }
        definitions["chibiInsert"] = {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "enabled": {"type": "boolean"},
                "mode": {"enum": ["CHIBI_SPOKEN_MONOLOGUE", "CHIBI_NONVERBAL_REACTION", "CHIBI_SYMBOLIC_PANTOMIME", "CHIBI_EMOTION_BURST"]},
                "representation_scope": {"const": "NON_DIEGETIC"},
                "start_time": {"type": "number", "minimum": 0},
                "end_time": {"type": "number", "exclusiveMinimum": 0},
                "performance": {"type": ["string", "array"]},
                "spoken_text": {"type": ["string", "null"]},
                "spoken_language": {"type": ["string", "null"]},
                "story_state_effect": {"const": "NONE"},
                "returns_to_main_scene": {"const": True},
            },
            "required": ["enabled"],
            "allOf": [
                {
                    "if": {"properties": {"enabled": {"const": True}}},
                    "then": {
                        "required": ["mode", "representation_scope", "start_time", "end_time", "performance", "spoken_text", "spoken_language", "story_state_effect", "returns_to_main_scene"],
                        "properties": {"returns_to_main_scene": {"const": True}},
                    },
                },
                {
                    "if": {"properties": {"mode": {"const": "CHIBI_SPOKEN_MONOLOGUE"}}},
                    "then": {"properties": {"spoken_text": {"type": "string", "minLength": 1}, "spoken_language": {"type": "string", "minLength": 2}}},
                },
                {
                    "if": {"properties": {"mode": {"const": "CHIBI_NONVERBAL_REACTION"}}},
                    "then": {"properties": {"spoken_text": {"const": None}}},
                },
            ],
        }
        root_rule = {
            "if": {
                "required": ["chibi_insert"],
                "properties": {
                    "chibi_insert": {
                        "type": "object",
                        "properties": {"enabled": {"const": True}},
                        "required": ["enabled"],
                    }
                },
            },
            "then": {
                "properties": {
                    "style_profile": {
                        "type": "object",
                        "properties": {"chibi_insertions": {"const": True}},
                        "required": ["chibi_insertions"],
                    }
                }
            },
        }
        rules = schema.setdefault("allOf", [])
        rules[:] = [rule for rule in rules if rule.get("if", {}).get("required") != ["chibi_insert"]]
        rules.insert(0, root_rule)
        self.write(
            relative,
            json.dumps(schema, ensure_ascii=False, indent=2, sort_keys=True),
            sources=[
                "skills/08-seedance/schemas/seedance_scene_package.schema.json",
                "skills/language-policy/PROJECT_LANGUAGE_PROFILE.schema.json",
                "skills/04e-chibi-performance/manifest.yaml",
            ],
            skill_version=skill_version,
            schema_version="PORTABLE_SEEDANCE_SCENE_PACKAGE_V1",
            gaps=["Additive portable fields only; no production or frozen contract is changed."],
        )
        self.write(
            "seedance/body_mechanics/README.md",
            """# Body mechanics references

Use only after source action and actor are resolved. Portable candidate families
are in `../action_grammar/README.md` and
`../examples/` with body-motion candidate categories in
`../.. /skills/04b-visual-completion/`. No body mechanic may imply new target,
contact, injury, relationship, or outcome.
""".replace("../.. /", "../../"),
            sources=["skills/04b-visual-completion/body_motion.yaml", "skills/04d-action-choreography/choreography_phases.yaml"],
            skill_version=manifest["version"],
            schema_version="GEMINI_CREATIVE_BOUNDARY_CONTRACT_V1",
            gaps=["No production body-mechanics action executor is claimed."],
        )
        self.write(
            "seedance/README_STRUCTURE.md",
            """# Seedance package map

- `PROMPT_CONTRACT.yaml`: section order and authority.
- `reference_binding/`: image and multi-reference roles.
- `timing/`: adaptive 5/10/15-second targets.
- `camera/`: framing, movement and continuity guidance.
- `action_grammar/`: conservative source-action usage.
- `body_mechanics/`: optional movement reference.
- `vfx/`: profile/policy-specific restrictions.
- `negatives/`: identity, continuity and extra-character rules.
- `platforms/dola.yaml`: Dola UI syntax status and fail-closed behavior.
- `schemas/`: portable scene-package contract.
- `sheet_export/`: copyable structured row contract.
- `evidence/`: copied production profile/template evidence; not runtime code.
""",
            sources=["skills/08-seedance/manifest.yaml", "architecture/TAB2_MODEL_ADAPTERS.md"],
            skill_version=manifest["version"],
            schema_version="SEEDANCE_PROMPT_CONTRACT_V1",
        )
        self.write(
            "seedance/timing/README.md",
            """# Adaptive target durations: 5, 10 and 15 seconds

The three source timing references are independent targets, not a forced
equal-split timeline. Allocate beats from the action and scene rhythm; only
the primary sourced action is required in the listed template. Do not add
filler or a new state to fill a target duration.

Detailed portable references: `5s.yaml`, `10s.yaml`, and `15s.yaml`.
""",
            sources=["skills/08-seedance/timing/5s.yaml", "skills/08-seedance/timing/10s.yaml", "skills/08-seedance/timing/15s.yaml"],
            skill_version=manifest["version"],
            schema_version="SEEDANCE_ADAPTIVE_TIMING_V1",
        )

    def _write_source_evidence(self) -> None:
        for relative in ARCHITECTURE_EXPORTS:
            target = "source_evidence/" + relative.removeprefix("architecture/")
            source_text = (PRODUCTION / PurePosixPath(relative)).read_text(encoding="utf-8")
            source_text = self._rewrite_production_links(source_text)
            self.write(
                target,
                source_text,
                sources=[relative],
                schema_version="architecture-reference",
                gaps=["Architecture document is evidence-linked guidance; production code/tests remain executable authority."],
            )
        for relative in FROZEN_FILES:
            self.copy_file(
                relative,
                "source_evidence/frozen_contracts/" + Path(relative).name,
                schema_version="frozen-contract-registry",
                status="FROZEN_PRODUCTION_CONTRACT_REFERENCE_ONLY",
            )
        self.write(
            "source_evidence/README.md",
            """# Source evidence

This folder contains selected production architecture/contract reference
documents and frozen registry snapshots. It does not contain production
application source code. Listed source/test paths in manifests are trace
references, not vendored code.
""",
            sources=list(ARCHITECTURE_EXPORTS) + list(FROZEN_FILES),
            schema_version="SOURCE_EVIDENCE_INDEX_V1",
        )
        fixture = "tests/fixtures/gemini_seedance_skill_cases_v1.json"
        self.copy_file(
            fixture,
            "benchmarks/gemini_seedance_skill_cases_v1.json",
            schema_version="GEMINI_SEEDANCE_SKILL_CASES_V1",
            gaps=["Offline portable contract cases only; not a Gemini Web or Gemini Pro quality benchmark."],
        )
        self.copy_file(
            "skills/04e-chibi-performance/examples/good/vi_chibi_inner_monologue.yaml",
            "benchmarks/END_TO_END_PORTABLE_EXAMPLE.yaml",
            schema_version="PORTABLE_EXAMPLE_NOT_PIPELINE_ACCEPTANCE",
            gaps=["Portable style example only; not an observed Gemini full-pipeline output."],
        )
        self.copy_file(
            "tests/fixtures/gemini_language_chibi_cases_v1.json",
            "benchmarks/gemini_language_chibi_cases_v1.json",
            schema_version="GEMINI_LANGUAGE_CHIBI_CASES_V1",
            gaps=["Offline deterministic package contract cases; no live Gemini execution."],
        )
        self.copy_file(
            "skills/04e-chibi-performance/examples/good/vi_chibi_inner_monologue.yaml",
            "benchmarks/vi_chibi_inner_monologue_example.yaml",
            schema_version="PORTABLE_SYNTHETIC_EXAMPLE_V1",
            gaps=["Synthetic authored example for package behavior; not production or Gemini output."],
        )
        self.write(
            "benchmarks/README.md",
            """# Gemini full-pipeline benchmark status

## Evidence available

`gemini_seedance_skill_cases_v1.json` is a synthetic offline contract fixture.
`gemini_language_chibi_cases_v1.json` is an offline deterministic contract
fixture for independent language profiles and symbolic chibi safety.
Production regressions are mapped in `../validation/production_test_map.json`.
Neither is a full-pipeline Gemini Web benchmark.

## Full-pipeline benchmark: NOT RUN

No live Gemini/OpenAI calls are made by this repository. A future user-run
benchmark must evaluate source → portable state/visibility → continuity →
Writer WHAT → conditional enrichment → optional visual/action references →
Director HOW → Seedance prompt draft → quality audit. Record the model and
version, prompt and repository versions, input fixture ids, expected hard
invariants, output artifacts, repeatability, failures, and reviewer decision.
Do not convert the absence of a live run into a passing score.

Cases already present in the source fixture cover profile gating, Dola
reference uncertainty, action specificity, style examples and sheet output.
They do not measure the model's behavior.
""",
            sources=[fixture, "architecture/GEMINI_MODEL_ROUTING_AND_LIVE_ACCEPTANCE.md"],
            schema_version="GEMINI_FULL_PIPELINE_BENCHMARK_STATUS_V1",
            gaps=["Full-pipeline Gemini Web benchmark is NOT IMPLEMENTED."],
        )
        self.write(
            "audit/USER_GAP_CHECKLIST.md",
            """# User checklist: evidence or capability to add

- [ ] Gemini Pro/Web full-pipeline runs with pinned model/UI versions and review labels.
- [ ] Production acceptance contract for each portable visual-completion candidate.
- [ ] Production action-interpreter and phase-by-phase choreography evidence, if those are to be claimed as production capabilities.
- [ ] Current Director Skill-store version, approval state and active retrieval/ranking behavior.
- [ ] Current Dola UI evidence for single-image and multi-reference binding syntax.
- [ ] Decide whether style profiles should ever become production-persisted state; this package does not imply that they should.
- [ ] Full-pipeline benchmark thresholds and repeatability requirements from an owner.

Do not close a box from portable examples alone.
""",
            sources=["architecture/TAB2_DIRECTOR_ARCHITECTURE.md", "architecture/TAB2_MODEL_ADAPTERS.md", "architecture/GEMINI_MODEL_ROUTING_AND_LIVE_ACCEPTANCE.md"],
            schema_version="USER_GAP_CHECKLIST_V1",
        )
        self.write(
            "benchmarks/REGRESSION_MAPPING.md",
            """# Portable components to production regression map

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
""",
            sources=["tests/test_writer_frozen_contracts.py", "tests/test_director_frozen_contracts.py", "tests/test_gemini_seedance_skill_contracts.py"],
            schema_version="PRODUCTION_REGRESSION_MAP_V1",
            gaps=["Production regression tests are not Gemini quality benchmarks."],
        )

    @staticmethod
    def _rewrite_production_links(text: str) -> str:
        def replace(match: re.Match[str]) -> str:
            label, target = match.group(1), match.group(2).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                return match.group(0)
            source_path = PurePosixPath("architecture", target.split("#", 1)[0])
            normalized = posixpath.normpath(str(source_path))
            anchor = ("#" + target.split("#", 1)[1]) if "#" in target else ""
            return f"{label} (production reference: `{normalized}{anchor}`)"
        return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace, text)

    def _write_validation_metadata(self, current_hashes: dict[str, str]) -> None:
        frozen_baseline = self.baseline or {
            "format": "TAB2_FROZEN_CONTRACT_HASH_BASELINE_V1",
            "created_from_production_snapshot": BUILD_DATE,
            "files": current_hashes,
            "note": "First generated independent-package baseline; not a substitute for frozen test gates or version-control history.",
        }
        self.write(
            "validation/frozen_contract_baseline.json",
            json.dumps(frozen_baseline, ensure_ascii=False, indent=2, sort_keys=True),
            sources=list(FROZEN_FILES),
            schema_version="TAB2_FROZEN_CONTRACT_HASH_BASELINE_V1",
            status="FROZEN_PRODUCTION_CONTRACT_REFERENCE_ONLY",
            gaps=["Baseline is initialized from the production snapshot at first package build; repository has no git metadata."],
        )
        self.write(
            "audit/production_capability_audit.json",
            json.dumps(
                {
                    "audit_date": BUILD_DATE,
                    "production_is_source_of_truth": True,
                    "gemini_repository_runtime_authority": False,
                    "classification_values": ["VERIFIED", "PARTIAL", "MISSING", "UNKNOWN", "NOT_IMPLEMENTED"],
                    "capabilities": CAPABILITIES,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            sources=[
                "architecture/audits/tab2_prompt_skill_inventory.json",
                "architecture/TAB2_CALL_GRAPH.md",
                "architecture/TAB2_DATA_AUTHORITY.md",
                "architecture/TAB2_FROZEN_CONTRACTS.md",
                "architecture/TAB2_MODEL_ADAPTERS.md",
            ],
            schema_version="PRODUCTION_CAPABILITY_AUDIT_V1",
            gaps=["Capability statuses describe checked-in production evidence, not live Gemini Web behavior."],
        )
        self.write(
            "audit/language_chibi_prebuild_audit.json",
            json.dumps(
                {
                    "audit_date": BUILD_DATE,
                    "classification_values": ["VERIFIED", "PARTIAL", "MISSING", "UNKNOWN"],
                    "scope": [
                        "style resolution",
                        "inner_monologue",
                        "chibi_insertions",
                        "comedic VFX",
                        "dialogue",
                        "dialogue performance",
                        "action interpreter",
                        "action choreography",
                        "visual completion",
                        "Seedance prompt structure",
                        "PromptLanguageRenderer",
                        "prompt language",
                        "Chinese 3D chibi example",
                        "comedy reaction example",
                    ],
                    "findings": [
                        {"capability": "User-resolved visual style, inner_monologue and chibi_insertions flags", "status": "VERIFIED", "evidence": ["skills/09-style-resolution/PROJECT_VISUAL_PROFILE.schema.json", "skills/09-style-resolution/style_questionnaire.yaml", "skills/09-style-resolution/style_presets.yaml"], "gap": "Existing profile had no explicit full_chibi_scene scope before this package update."},
                        {"capability": "Brief nonverbal chibi insert and comedy restrictions", "status": "PARTIAL", "evidence": ["skills/08-seedance/vfx/comedic.yaml", "skills/08-seedance/examples/good/comedy_reaction.yaml"], "gap": "Did not type monologue modes or enforce a diegetic/state boundary for every symbolic action."},
                        {"capability": "Chinese 3D chibi example", "status": "PARTIAL", "evidence": ["skills/08-seedance/examples/good/chinese_3d_chibi.yaml"], "gap": "Style example contains no concrete typed language, source monologue, safe symbolic-action, or return-to-main-world example."},
                        {"capability": "Writer exact source dialogue", "status": "VERIFIED", "evidence": ["skills/03-writer/SKILL.md", "tests/test_writer_frozen_contracts.py"], "gap": "Portable Seedance did not have language-typed fields for each speech category."},
                        {"capability": "PromptLanguageRenderer target prompt language", "status": "VERIFIED", "evidence": ["ai_agent_brain/prompt_assembly/language_renderer.py", "ai_agent_brain/prompt_assembly/prompt_engine.py", "tests/test_prompt_engine.py"], "gap": "Renderer target language does not itself establish a separate project source/spoken-language profile."},
                        {"capability": "Protected source speech through every rendering path", "status": "PARTIAL", "evidence": ["ai_agent_brain/prompt_assembly/prompt_engine.py", "ai_agent_brain/prompt_assembly/language_renderer.py"], "gap": "Renderer protects caller-supplied exact text; no evidence that a separate project profile guarantees every speech/VO path end-to-end."},
                        {"capability": "Independent PROJECT_LANGUAGE_PROFILE and typed speech categories", "status": "MISSING", "evidence": ["tests/test_prompt_engine.py"], "gap": "No frozen production project language profile or typed portable speech policy existed."},
                        {"capability": "Chibi spoken monologue, symbolic pantomime and real-vs-symbolic action boundary", "status": "MISSING", "evidence": ["skills/08-seedance/vfx/comedic.yaml", "skills/04d-action-choreography/manifest.yaml"], "gap": "No production chibi performance authority or complete portable contract existed."},
                        {"capability": "PromptLanguageRenderer spoken-language schema", "status": "UNKNOWN", "evidence": ["ai_agent_brain/prompt_assembly/language_renderer.py"], "gap": "Production rendering only accepts a prompt target language; no separate spoken language routing interface is evidenced."},
                    ],
                    "production_changed": False,
                    "contracts_changed": False,
                    "runtime_authority_added": False,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            sources=[
                "skills/09-style-resolution/PROJECT_VISUAL_PROFILE.schema.json",
                "skills/08-seedance/vfx/comedic.yaml",
                "skills/03-writer/SKILL.md",
                "ai_agent_brain/prompt_assembly/language_renderer.py",
                "ai_agent_brain/prompt_assembly/prompt_engine.py",
                "tests/test_prompt_engine.py",
            ],
            schema_version="LANGUAGE_CHIBI_PREBUILD_AUDIT_V1",
            gaps=["Statuses describe reviewed evidence before the targeted portable package addition; they do not assert provider behavior."],
        )
        tests = sorted({test for capability in CAPABILITIES for test in capability["tests"]})
        tests.append("tests/test_gemini_language_chibi_contracts.py")
        tests = sorted(set(tests))
        self.write(
            "validation/production_test_map.json",
            json.dumps(
                {
                    "status": "TRACEABILITY_ONLY_NOT_EXECUTION",
                    "tests": tests,
                    "portable_contract_tests": [
                        "tests/test_gemini_seedance_skill_contracts.py",
                        "tests/test_gemini_language_chibi_contracts.py",
                    ],
                    "no_provider_calls": True,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            sources=["architecture/audits/tab2_prompt_skill_inventory.json"],
            schema_version="PRODUCTION_TEST_MAP_V1",
        )

    def _write_readme(self) -> None:
        self.write(
            "README.md",
            """# Tab 2 Gemini Skills

An independent, portable Gemini-facing reference repository built from
verified production architecture, frozen registries, existing Gemini
distribution files, source skills, schemas, fixtures and test mappings.

**Production remains the source of truth. This repository is not runtime
authority.** It contains no production application Python implementation.
The only Python script is the deterministic exporter/validator.

## Build from the production workspace

From the parent production workspace:

```powershell
py -3.13 tab2-gemini-skills\\build_from_production.py --build
```

The build reads the parent workspace, copies only reference material, runs
offline package validation, writes a provenance index, and verifies source
contract hashes against the recorded baseline. The first build creates the
frozen-hash baseline from the observed production snapshot; subsequent builds
fail if either frozen registry differs. Run the production frozen tests
separately before distributing.

Generate the Vietnamese Word guide only after a successful build:

```powershell
py -3.13 tab2-gemini-skills\\generate_word_guide.py
```

The Word generator reads only files inside this repository. Neither command
makes a live Gemini/OpenAI call or invokes production API routes.

## Top-level layout

- `00_CORE/`: authority, workflow, creative boundary and failure rules.
- `project_state/`: portable project templates and schemas.
- `skills/`: 14 Gemini-facing stage/reference packages.
- `language/`: portable profile and typed-source-text rules.
- `seedance/`: consolidated Seedance, timing, reference and Dola guidance.
- `source_evidence/`: selected architecture docs and frozen registry snapshots.
- `audit/`: evidence-based capability classifications.
- `benchmarks/`: offline synthetic contract cases and mapped production tests.
- `validation/`: hash baseline, test map and build checks.
- `docs/generated/`: generated Vietnamese architecture guide after validation.

`SOURCE_MANIFEST.json` maps every packaged file to source production paths,
skill/schema version, distribution version, reference-only status and known
gaps.
""",
            sources=["architecture/TAB2_PROMPT_SKILL_ARCHITECTURE.md", "dist/README.md"],
            schema_version="GEMINI_REPOSITORY_README_V1",
        )
        self.write(
            "RELEASE_METADATA.json",
            json.dumps(
                {
                    "repository": "tab2-gemini-skills",
                    "distribution_version": VERSION,
                    "release_date": BUILD_DATE,
                    "release_status": "PARTIAL_READINESS_REFERENCE_PACKAGE",
                    "source_of_truth": "parent production repository",
                    "runtime_authority": False,
                    "builder": "build_from_production.py",
                    "rebuild_command": "py -3.13 tab2-gemini-skills\\build_from_production.py --build",
                    "word_document_generator": "generate_word_guide.py",
                    "live_provider_calls": False,
                    "known_release_gaps": [
                        "Gemini Web full-pipeline benchmark not run",
                        "Dola UI reference tag syntax unknown",
                        "Current production Director Skill-store state unknown",
                    ],
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            ),
            sources=["dist/build_distribution.py", "architecture/GEMINI_MODEL_ROUTING_AND_LIVE_ACCEPTANCE.md"],
            schema_version="GEMINI_SKILLS_RELEASE_METADATA_V1",
            gaps=["Partial readiness; see audit/production_capability_audit.json."],
        )
        self.write(
            "CHANGELOG.md",
            """# Changelog

## 1.1.0 — 2026-10-07

- Initial independent Gemini-facing reference distribution generated from the
  production workspace and existing Gemini skill assets.
- Added per-file source provenance, portable state templates/schemas,
  authority/workflow boundaries, Seedance/Dola guidance, and capability audit.
- Added deterministic build, frozen-registry hash check, relative-reference
  check, schema check, and secret-pattern scan.
- Added offline synthetic benchmark fixture and production regression map.
- Gemini Web full-pipeline benchmark remains NOT RUN; no live provider calls.
- Dola UI tag syntax and current Director Skill-store status remain unknown.
- Added user-selected independent source/prompt/speech language profile,
  typed speech policy, and offline Vietnamese-source/English-prompt cases.
- Added optional non-diegetic chibi inner-monologue performance reference,
  real-vs-symbolic action boundaries, Seedance schema fields, and regressions.
""",
            sources=["dist/build_distribution.py", "architecture/TAB2_PROMPT_SKILL_ARCHITECTURE.md"],
            schema_version="GEMINI_SKILLS_CHANGELOG_V1",
            gaps=["Release notes describe this independent package, not production runtime changes."],
        )

    def _write_builder_copy(self) -> None:
        self.write(
            "build_from_production.py",
            Path(__file__).read_bytes(),
            sources=["dist/build_distribution.py", "architecture/TAB2_PROMPT_SKILL_ARCHITECTURE.md"],
            schema_version="DETERMINISTIC_EXPORT_BUILDER_V1",
            gaps=["Requires the production workspace as its parent directory."],
        )
        self.write(
            "generate_word_guide.py",
            self._word_builder_source(),
            sources=["tab2-gemini-skills/00_CORE/", "tab2-gemini-skills/skills/", "tab2-gemini-skills/seedance/", "tab2-gemini-skills/audit/"],
            schema_version="VIETNAMESE_WORD_GUIDE_GENERATOR_V1",
            gaps=["Requires python-docx; output is descriptive of this repository, not production runtime."],
        )

    @staticmethod
    def _word_builder_source() -> str:
        return WORD_BUILDER_SOURCE

    def _write_manifest(self) -> None:
        manifest = {
            "repository": "tab2-gemini-skills",
            "distribution_version": VERSION,
            "generated_at": BUILD_DATE,
            "source_of_truth": "parent production repository",
            "runtime_authority": False,
            "file_provenance": "files map to source_production_files, source_skill_version, schema_version, distribution_version, status, known_gaps",
            "manifest_provenance": {
                "source_production_files": ["dist/build_distribution.py", "architecture/TAB2_PROMPT_SKILL_ARCHITECTURE.md"],
                "source_skill_version": None,
                "schema_version": "SOURCE_MANIFEST_V1",
                "distribution_version": VERSION,
                "status": PORTABLE,
                "known_gaps": ["The manifest indexes all package files except itself to avoid recursive self-hashing."],
            },
            "files": self.provenance,
        }
        path = REPOSITORY / "SOURCE_MANIFEST.json"
        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    def validate(self, include_document: bool = False) -> None:
        errors: list[str] = []
        expected_order = [
            "SOURCE", "STORY MEMORY", "PRODUCTION CANON", "WRITER WHAT",
            "VISUAL COMPLETION", "ACTION INTERPRETER", "ACTION CHOREOGRAPHY",
            "DIRECTOR HOW", "SEEDANCE ADAPTER", "PROMPT ENGINE", "QUALITY AUDIT",
        ]
        core = (REPOSITORY / "00_CORE/CORE_CONTRACTS.md").read_text(encoding="utf-8")
        order_positions = [core.index(item) for item in expected_order]
        if order_positions != sorted(order_positions):
            errors.append("authority order changed")
        manifest = json.loads((REPOSITORY / "SOURCE_MANIFEST.json").read_text(encoding="utf-8")) if (REPOSITORY / "SOURCE_MANIFEST.json").exists() else None
        if manifest:
            expected_skills = {item[0] for item in SKILL_EXPORTS}
            for skill in expected_skills:
                path = REPOSITORY / "skills" / skill / "SKILL.md"
                if not path.is_file():
                    errors.append(f"missing skill {skill}")
                    continue
                text = path.read_text(encoding="utf-8")
                for heading in ("ROLE", "AUTHORITY", "INPUT", "OUTPUT", "WORKFLOW", "ALLOWED", "FORBIDDEN", "FAIL CONDITIONS", "VALIDATION", "NEXT STAGE", "REFERENCES"):
                    if f"## {heading}" not in text:
                        errors.append(f"{skill}: missing {heading}")
            for relative, data in manifest["files"].items():
                path = REPOSITORY / PurePosixPath(relative)
                if not path.is_file():
                    errors.append(f"manifest file missing: {relative}")
                    continue
                for key in ("source_production_files", "source_skill_version", "schema_version", "distribution_version", "status", "known_gaps"):
                    if key not in data:
                        errors.append(f"{relative}: provenance missing {key}")
                if data.get("distribution_version") != VERSION:
                    errors.append(f"{relative}: distribution version mismatch")
                for source in data.get("source_production_files", []):
                    if not (PRODUCTION / PurePosixPath(source)).exists():
                        errors.append(f"{relative}: source trace missing in production workspace: {source}")
            actual_files = {
                _relative(path)
                for path in REPOSITORY.rglob("*")
                if path.is_file() and path.name != "SOURCE_MANIFEST.json"
            }
            if actual_files != set(manifest["files"]):
                errors.append("source manifest file set mismatch")
        schemas = list((REPOSITORY / "project_state/schemas").glob("*.json"))
        schemas += list((REPOSITORY / "seedance/schemas").glob("*.json"))
        schemas += list((REPOSITORY / "seedance/sheet_export").glob("*.json"))
        schemas += list((REPOSITORY / "skills/09-style-resolution").glob("*.schema.json"))
        schemas += list((REPOSITORY / "language").glob("*.schema.json"))
        for schema_path in schemas:
            try:
                import jsonschema
                schema = json.loads(schema_path.read_text(encoding="utf-8"))
                jsonschema.Draft202012Validator.check_schema(schema)
            except ImportError:
                errors.append("python package jsonschema missing; schema validation not run")
                break
            except Exception as exc:
                errors.append(f"invalid schema {schema_path.relative_to(REPOSITORY)}: {exc}")
        if schemas:
            import jsonschema
            template_pairs = (
                ("project_state/templates/PROJECT_STATE.json", "project_state/schemas/project_state.schema.json"),
                ("project_state/templates/PROJECT_VISUAL_PROFILE.json", "project_state/schemas/project_visual_profile.schema.json"),
                ("project_state/templates/PROJECT_LANGUAGE_PROFILE.json", "language/PROJECT_LANGUAGE_PROFILE.schema.json"),
                ("project_state/templates/STORY_MEMORY.json", "project_state/schemas/story_memory_state.schema.json"),
                ("project_state/templates/CHARACTERS.json", "project_state/schemas/characters.schema.json"),
                ("project_state/templates/RELATIONSHIPS.json", "project_state/schemas/relationships.schema.json"),
                ("project_state/templates/KNOWLEDGE.json", "project_state/schemas/knowledge.schema.json"),
                ("project_state/templates/EVENTS.json", "project_state/schemas/events.schema.json"),
                ("project_state/templates/OPEN_THREADS.json", "project_state/schemas/open_threads.schema.json"),
                ("project_state/templates/CHAPTER_STATUS.json", "project_state/schemas/chapter_status.schema.json"),
            )
            for template_relative, schema_relative in template_pairs:
                try:
                    instance = json.loads((REPOSITORY / template_relative).read_text(encoding="utf-8"))
                    schema = json.loads((REPOSITORY / schema_relative).read_text(encoding="utf-8"))
                    jsonschema.Draft202012Validator(schema).validate(instance)
                except Exception as exc:
                    errors.append(f"template/schema mismatch {template_relative}: {exc}")
        transitions_path = REPOSITORY / "workflow/STAGE_TRANSITIONS.json"
        if transitions_path.is_file():
            transitions = json.loads(transitions_path.read_text(encoding="utf-8"))
            if transitions["visibility"].get("future_facts") != "BLOCKED" or transitions["visibility"].get("unknown_or_missing_visibility") != "UNRESOLVED":
                errors.append("future/unknown temporal visibility is not fail-closed")
        seedance_schema_path = REPOSITORY / "seedance/schemas/seedance_scene_package.schema.json"
        if seedance_schema_path.is_file():
            seedance_schema = json.loads(seedance_schema_path.read_text(encoding="utf-8"))
            expected_sections = ("WHO", "WHERE", "WHAT", "HOW", "WHEN", "CAMERA", "REFERENCE", "STYLE", "END_STATE")
            prompt_contract = (REPOSITORY / "seedance/PROMPT_CONTRACT.yaml").read_text(encoding="utf-8")
            if any(section not in prompt_contract for section in expected_sections):
                errors.append("Seedance prompt contract is missing a required section")
            if "writer_what_unchanged" not in seedance_schema.get("properties", {}):
                errors.append("Seedance schema does not lock Writer WHAT")
        sheet_schema_path = REPOSITORY / "seedance/sheet_export/sheet_export.schema.json"
        if sheet_schema_path.is_file():
            sheet_schema = json.loads(sheet_schema_path.read_text(encoding="utf-8"))
            expected_fields = {"prompt_id", "chapter", "scene_id", "shot_id", "duration_seconds", "model", "platform", "style", "reference_images", "prompt", "negative_constraints", "status", "revision"}
            if not expected_fields.issubset(set(sheet_schema.get("required", []))):
                errors.append("sheet schema is missing a required export field")
            if sheet_schema.get("$id") != "PORTABLE_VIDEO_PROMPT_SHEET_ROW_V1":
                errors.append("unexpected sheet schema identity")
        language_schema_path = REPOSITORY / "language/PROJECT_LANGUAGE_PROFILE.schema.json"
        if language_schema_path.is_file():
            language_schema = json.loads(language_schema_path.read_text(encoding="utf-8"))
            language_properties = language_schema.get("properties", {})
            for required in ("prompt_language", "spoken_dialogue_language", "inner_monologue_language", "voice_over_language"):
                if required not in language_properties:
                    errors.append(f"language profile missing {required}")
            if language_schema.get("$id") != "PROJECT_LANGUAGE_PROFILE_V1":
                errors.append("unexpected language profile schema identity")
        if seedance_schema_path.is_file():
            language_chibi_fields = {
                "language_profile_ref", "spoken_dialogue", "internal_monologue",
                "voice_over", "chibi_insert",
            }
            missing_fields = language_chibi_fields - set(seedance_schema.get("properties", {}))
            if missing_fields:
                errors.append("Seedance portable schema missing additive fields: " + ", ".join(sorted(missing_fields)))
            chibi_schema = seedance_schema.get("$defs", {}).get("chibiInsert", {})
            if chibi_schema.get("properties", {}).get("representation_scope", {}).get("const") != "NON_DIEGETIC":
                errors.append("chibi schema does not enforce NON_DIEGETIC")
            if chibi_schema.get("properties", {}).get("story_state_effect", {}).get("const") != "NONE":
                errors.append("chibi schema does not enforce story_state_effect NONE")
            chibi_profile_condition = any(
                condition.get("if", {}).get("required") == ["chibi_insert"]
                for condition in seedance_schema.get("allOf", [])
            )
            if not chibi_profile_condition:
                errors.append("Seedance schema does not gate chibi inserts on the selected visual profile")
        chibi_skill = REPOSITORY / "skills/04e-chibi-performance/SKILL.md"
        if chibi_skill.is_file():
            chibi_text = chibi_skill.read_text(encoding="utf-8")
            for required in ("CHIBI_SPOKEN_MONOLOGUE", "CHIBI_NONVERBAL_REACTION", "CHIBI_SYMBOLIC_PANTOMIME", "CHIBI_EMOTION_BURST", "REAL_ACTION", "CHIBI_SYMBOLIC_ACTION", "story_state_effect: NONE", "return"):
                if required.casefold() not in chibi_text.casefold():
                    errors.append(f"chibi skill missing invariant {required}")
        if (REPOSITORY / "language/examples/vi_source_en_prompt_vi_speech.json").is_file():
            language_example = json.loads((REPOSITORY / "language/examples/vi_source_en_prompt_vi_speech.json").read_text(encoding="utf-8"))
            speech = language_example["content"][0]
            if language_example["profile"]["prompt_language"] == speech["language"]:
                errors.append("language example does not demonstrate independent prompt and spoken languages")
            if speech["source_text"] != speech["rendered_text"]:
                errors.append("language example changes source speech")
        fixture_path = REPOSITORY / "benchmarks/gemini_language_chibi_cases_v1.json"
        if fixture_path.is_file():
            cases = json.loads(fixture_path.read_text(encoding="utf-8")).get("cases", [])
            if len(cases) != 12:
                errors.append("language/chibi offline fixture must contain exactly 12 cases")
        style_schema = json.loads((REPOSITORY / "project_state/schemas/project_visual_profile.schema.json").read_text(encoding="utf-8"))
        if style_schema.get("properties", {}).get("full_chibi_scene", {}).get("default") is not False:
            errors.append("full_chibi_scene must default to false")
        authority_text = (REPOSITORY / "00_CORE/DATA_AUTHORITY.md").read_text(encoding="utf-8").lower()
        if "writer" not in authority_text or "director" not in authority_text or "promptengine" not in authority_text:
            errors.append("Writer/Director/PromptEngine authority statements missing")
        director_text = "\n".join(path.read_text(encoding="utf-8") for path in (REPOSITORY / "skills/05-director").rglob("*") if path.is_file() and path.suffix in {".md", ".yaml", ".json"})
        for term in ("default_bounded_retrieval", "selection_rule", "conflicts_with", "approval"):
            if term not in director_text.lower():
                errors.append(f"Director retrieval/conflict evidence missing {term}")
        for relative in FROZEN_FILES:
            expected = self._frozen_hashes()[relative]
            baseline = self.baseline or {"files": self._frozen_hashes()}
            if baseline["files"].get(relative) != expected:
                errors.append(f"frozen contract hash changed: {relative}")
        if (REPOSITORY / "seedance/platforms/dola.yaml").is_file():
            dola = (REPOSITORY / "seedance/platforms/dola.yaml").read_text(encoding="utf-8")
            if "current_tag_syntax_status: UNKNOWN" not in dola or "emit_invented_tag: false" not in dola:
                errors.append("Dola unknown-syntax fail-closed rule missing")
        if (REPOSITORY / "project_state/templates/PROJECT_VISUAL_PROFILE.json").is_file():
            profile = json.loads((REPOSITORY / "project_state/templates/PROJECT_VISUAL_PROFILE.json").read_text(encoding="utf-8"))
            if profile.get("profile_status") != "STYLE_UNRESOLVED":
                errors.append("project style template must start unresolved")
        if any(path.suffix in {".pyc", ".pyo"} for path in REPOSITORY.rglob("*") if path.is_file()):
            errors.append("bytecode found in exported repository")
        forbidden_code = [
            path for path in REPOSITORY.rglob("*.py")
            if path.name not in {"build_from_production.py", "generate_word_guide.py"}
        ]
        if forbidden_code:
            errors.append("unexpected Python source exported: " + ", ".join(_relative(p) for p in forbidden_code))
        errors.extend(self._relative_link_errors())
        errors.extend(self._secret_scan())
        if include_document and not (REPOSITORY / "docs/generated/TAB2_GEMINI_SKILLS_KIEN_TRUC_VAN_HANH_VI.docx").is_file():
            errors.append("generated Vietnamese Word document missing")
        if errors:
            raise SystemExit("Repository validation failed:\n" + "\n".join(errors))

    def _relative_link_errors(self) -> list[str]:
        errors = []
        for path in REPOSITORY.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                local = target.split("#", 1)[0]
                if not local:
                    continue
                if not (path.parent / local).resolve().exists():
                    errors.append(f"broken relative link {path.relative_to(REPOSITORY)} -> {target}")
        return errors

    def _secret_scan(self) -> list[str]:
        patterns = [
            re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", re.I),
            re.compile(r"(?i)\b(?:api[_-]?key|password|secret|access[_-]?token|refresh[_-]?token|cookie)\b\s*[:=]\s*['\"][^'\"]{8,}"),
            re.compile(r"\b(?:sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,})\b"),
            re.compile(r"(?i)[A-Z]:\\Users\\[^\\\s]+"),
        ]
        findings = []
        for path in REPOSITORY.rglob("*"):
            if not path.is_file() or path.suffix in {".docx", ".zip"}:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if any(pattern.search(text) for pattern in patterns):
                findings.append(f"secret-pattern match: {path.relative_to(REPOSITORY)}")
        return findings


WORD_BUILDER_SOURCE = r'''from __future__ import annotations

import json
from pathlib import Path
import zipfile
from docx import Document
from docx.shared import Inches, Pt

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs" / "generated" / "TAB2_GEMINI_SKILLS_KIEN_TRUC_VAN_HANH_VI.docx"

def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")

def add_source_note(doc, relative: str) -> None:
    doc.add_paragraph(f"Nguồn trong repository: {relative}", style="Caption")

def add_skill(doc, relative: str, label: str) -> None:
    path = ROOT / relative
    doc.add_heading(label, level=2)
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            doc.add_heading(line[3:], level=3)
        elif line.strip().startswith("- "):
            doc.add_paragraph(line.strip()[2:], style="List Bullet")
        elif line.strip():
            doc.add_paragraph(line.strip())
    add_source_note(doc, relative)

def main() -> None:
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.65)
    section.bottom_margin = Inches(0.65)
    doc.styles["Normal"].font.name = "Aptos"
    doc.styles["Normal"].font.size = Pt(10)
    doc.add_heading("Kiến trúc và vận hành Tab 2 Gemini Skills", 0)
    doc.add_paragraph("Tài liệu này được tổng hợp chỉ từ repository tab2-gemini-skills. Repository là gói tham chiếu portable; production vẫn là source of truth và không giao runtime authority cho Gemini.")
    skills = [
        ("00 orchestrator", "skills/00-orchestrator/SKILL.md"),
        ("01 story-memory", "skills/01-story-memory/SKILL.md"),
        ("02 continuity", "skills/02-continuity/SKILL.md"),
        ("03 writer", "skills/03-writer/SKILL.md"),
        ("04 enrichment", "skills/04-enrichment/SKILL.md"),
        ("04b visual-completion", "skills/04b-visual-completion/SKILL.md"),
        ("04c action-interpreter", "skills/04c-action-interpreter/SKILL.md"),
        ("04d action-choreography", "skills/04d-action-choreography/SKILL.md"),
        ("04e chibi-performance", "skills/04e-chibi-performance/SKILL.md"),
        ("05 director", "skills/05-director/SKILL.md"),
        ("06 prompt-engine", "skills/06-prompt-engine/SKILL.md"),
        ("07 quality-audit", "skills/07-quality-audit/SKILL.md"),
        ("08 seedance", "skills/08-seedance/SKILL.md"),
        ("09 style-resolution", "skills/09-style-resolution/SKILL.md"),
    ]
    topics = [
        ("1. Tổng quan hệ thống", "README.md"),
        ("2. Sơ đồ pipeline", "00_CORE/WORKFLOW.md"),
        ("3. Cấu trúc repository", "README.md"),
        ("4. Giải thích từng folder", "README.md"),
        ("5. Giải thích từng skill", "__SKILLS__"),
        ("6. Authority", "00_CORE/DATA_AUTHORITY.md"),
        ("7. Quy trình đưa tiểu thuyết vào", "skills/00-orchestrator/SKILL.md"),
        ("8. Style questionnaire", "skills/09-style-resolution/style_questionnaire.yaml"),
        ("9. Story Memory", "skills/01-story-memory/SKILL.md"),
        ("10. Continuity", "skills/02-continuity/SKILL.md"),
        ("11. Writer WHAT", "skills/03-writer/SKILL.md"),
        ("12. Visual Completion", "skills/04b-visual-completion/SKILL.md"),
        ("13. Safe vs forbidden inference", "00_CORE/CREATIVE_BOUNDARY.md"),
        ("14. Action Interpreter", "skills/04c-action-interpreter/SKILL.md"),
        ("15. Action Choreography", "skills/04d-action-choreography/SKILL.md"),
        ("16. Chibi performance", "skills/04e-chibi-performance/SKILL.md"),
        ("17. Language policy", "language/LANGUAGE_POLICY.md"),
        ("18. Director HOW", "skills/05-director/SKILL.md"),
        ("19. Seedance", "skills/08-seedance/SKILL.md"),
        ("20. Dola", "seedance/platforms/dola.yaml"),
        ("21. Character references", "seedance/reference_binding/multi_reference.yaml"),
        ("22. @Image handling", "seedance/platforms/dola.yaml"),
        ("23. Timeline 5/10/15s", "seedance/timing/README.md"),
        ("24. Chibi/comedy", "seedance/vfx/comedic.yaml"),
        ("25. Anime", "skills/09-style-resolution/style_presets.yaml"),
        ("26. Chinese 3D", "skills/09-style-resolution/style_presets.yaml"),
        ("27. Wuxia/Xianxia", "seedance/vfx/wuxia.yaml"),
        ("28. VFX", "seedance/vfx/fantasy.yaml"),
        ("29. Prompt structure", "seedance/PROMPT_CONTRACT.yaml"),
        ("30. Quality Audit", "skills/07-quality-audit/SKILL.md"),
        ("31. Sheet export", "seedance/sheet_export/README.md"),
        ("32. Ví dụ end-to-end", "benchmarks/END_TO_END_PORTABLE_EXAMPLE.yaml"),
        ("33. Known unknowns", "audit/production_capability_audit.json"),
        ("34. Missing capabilities", "audit/production_capability_audit.json"),
        ("35. Checklist bổ sung", "audit/USER_GAP_CHECKLIST.md"),
        ("36. Ngôn ngữ prompt và ngôn ngữ thoại", "language/LANGUAGE_POLICY.md"),
        ("37. Prompt tiếng Anh / thoại tiếng Việt", "language/examples/vi_source_en_prompt_vi_speech.json"),
        ("38. Thoại nội tâm", "language/inner_monologue_policy.yaml"),
        ("39. Chibi nội tâm", "skills/04e-chibi-performance/inner_monologue/routing.yaml"),
        ("40. Chibi nói chuyện", "skills/04e-chibi-performance/inner_monologue/spoken_chibi.yaml"),
        ("41. Chibi cử động tượng trưng", "skills/04e-chibi-performance/inner_monologue/symbolic_action.yaml"),
        ("42. Đấm/đá thật và đấm/đá chibi", "skills/04e-chibi-performance/grammars/fight_pantomime.yaml"),
        ("43. Khóc thật và khóc chibi", "skills/04e-chibi-performance/grammars/crying.yaml"),
        ("44. Ranh giới thế giới thật / non-diegetic", "skills/04e-chibi-performance/constraints/diegetic_boundary.yaml"),
        ("45. Ví dụ hoàn chỉnh", "benchmarks/vi_chibi_inner_monologue_example.yaml"),
    ]
    doc.add_heading("Nội dung", level=1)
    for heading, relative in topics:
        doc.add_heading(heading, level=1)
        if relative == "__SKILLS__":
            for label, skill_path in skills:
                add_skill(doc, skill_path, label)
            continue
        if relative.endswith(".json"):
            data = json.loads(read(relative))
            if heading.startswith("33."):
                for item in data["capabilities"]:
                    if item["status"] != "VERIFIED":
                        doc.add_paragraph(f"{item['id']} — {item['status']}: {'; '.join(item['known_gaps'])}", style="List Bullet")
            elif heading.startswith("34."):
                for item in data["capabilities"]:
                    if item["status"] in {"NOT_IMPLEMENTED", "MISSING", "UNKNOWN"}:
                        doc.add_paragraph(f"{item['id']}: {item['what_is_evidenced']} Missing: {'; '.join(item['known_gaps'])}", style="List Bullet")
            else:
                doc.add_paragraph(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            text = read(relative)
            for line in text.splitlines():
                if line.startswith("#"):
                    continue
                if line.strip().startswith("- "):
                    doc.add_paragraph(line.strip()[2:], style="List Bullet")
                elif line.strip():
                    doc.add_paragraph(line.strip())
        add_source_note(doc, relative)
    audit = json.loads(read("audit/production_capability_audit.json"))
    doc.add_heading("Bảng trạng thái thành phần", level=1)
    table = doc.add_table(rows=1, cols=6)
    table.style = "Light Shading Accent 1"
    headers = ["COMPONENT", "STATUS", "SOURCE", "WHAT IT DOES", "MISSING", "RECOMMENDED NEXT ACTION"]
    for cell, value in zip(table.rows[0].cells, headers):
        cell.text = value
    for item in audit["capabilities"]:
        row = table.add_row().cells
        values = [
            item["id"], item["status"], "; ".join(item["production_sources"]),
            item["what_is_evidenced"], "; ".join(item["known_gaps"]),
            "Kiểm tra bằng chứng và gap; chỉ bổ sung khi có production evidence hoặc quyết định migration rõ ràng.",
        ]
        for cell, value in zip(row, values):
            cell.text = value
    doc.core_properties.title = "Kiến trúc vận hành Tab 2 Gemini Skills"
    doc.core_properties.author = "Tab 2 Gemini Skills repository"
    doc.core_properties.created = __import__("datetime").datetime(2026, 10, 7)
    doc.core_properties.modified = __import__("datetime").datetime(2026, 10, 7)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)
    normalize_docx_zip(OUT)
    manifest_path = ROOT / "SOURCE_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    source_production_files = sorted({
        source
        for metadata in manifest["files"].values()
        for source in metadata["source_production_files"]
    })
    manifest["files"]["docs/generated/TAB2_GEMINI_SKILLS_KIEN_TRUC_VAN_HANH_VI.docx"] = {
        "source_production_files": source_production_files,
        "source_skill_version": None,
        "schema_version": "VIETNAMESE_TAB2_GEMINI_GUIDE_V1",
        "distribution_version": manifest["distribution_version"],
        "status": "GENERATED_FROM_VALIDATED_PORTABLE_REPOSITORY",
        "known_gaps": ["Documents describe portable package behavior only; production-only unknowns are explicitly listed in the document."],
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(OUT)

def normalize_docx_zip(path: Path) -> None:
    fixed_time = (2020, 1, 1, 0, 0, 0)
    temp_path = path.with_suffix(".normalized.docx")
    with zipfile.ZipFile(path, "r") as source, zipfile.ZipFile(temp_path, "w") as target:
        for name in sorted(source.namelist()):
            info = zipfile.ZipInfo(name, date_time=fixed_time)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = source.getinfo(name).external_attr
            target.writestr(info, source.read(name))
    temp_path.replace(path)

if __name__ == "__main__":
    main()
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()
    builder = ExportBuilder()
    if args.validate:
        builder.validate(include_document=True)
    else:
        builder.build()
        print(f"Built and validated {REPOSITORY}")


if __name__ == "__main__":
    main()
