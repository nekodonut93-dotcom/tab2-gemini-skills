# Tab 2 Prompt / Skill package architecture

**Decision state:** documentation and reference package proposal; not a runtime
migration. Production loading, routing and prompt behavior are unchanged.

## Proposed load hierarchy

```text
root AGENTS.md + architecture authority documents
        ↓
00 orchestration and boundaries
01 Story Memory / temporal context
02 continuity and Canon gates
03 Writer WHAT
04 evidence-bounded enrichment
05 Director core → INDEX.yaml → selected concepts only
06 PromptEngine and model adapters
07 quality/frozen/quota regression map
```

Top-level reference skills are grouped by existing responsibilities, not new
creative capabilities. The Director package does not contain a giant prompt
catalog: `skills/05-director/INDEX.yaml` indexes verified categories and
evidence records so consumers can select relevant knowledge without loading
everything.

## Required record separation

1. **DIRECTING_KNOWLEDGE:** why/when a cinematic choice is appropriate (for
   example, an evidenced camera movement purpose or pacing consequence).
2. **PROMPT_SYNTAX:** literal structured prompt layout, model-specific terms,
   section order, capabilities or unsupported fields.
3. **DETERMINISTIC_CODE:** validation, precedence, temporal/source boundaries,
   cache identity, retry/idempotency and contract gates. This stays executable;
   documentation only explains and links to it.

Do not promote user/imported samples, DRAFT knowledge packages, or unverified
Skill-store state to active skills. Keep examples small and source-bound; link
existing large prompt sample corpora instead of copying them.

## Manifest and lifecycle

Each skill manifest carries identity, SemVer version, owner/category,
description, applicability/avoidance, IO, dependencies/conflicts, compatible
models, authority, prohibited changes, production source/function links,
related tests, prompt/schema version identities, and status.

- **MAJOR:** breaking behavior, semantics, or compatibility.
- **MINOR:** additive capability/concept.
- **PATCH:** bug fix or clarification without behavior change.

Skill version must reference current prompt/schema identities; it must not
rename or replace existing production cache identities. Packaging remains
usable in Gemini web, ChatGPT web, OpenAI API, and Gemini API because core
content is model-neutral; provider syntax belongs only in adapters.

## Duplicate and conflict treatment

Inventory classifications are `EXACT_DUPLICATE`, `SEMANTIC_DUPLICATE`,
`MODEL_VARIANT`, and `LEGITIMATE_VARIANT`. Report canonical candidates,
differences and merge strategy only. No semantic duplicate is deleted
automatically. Responsibility overlaps are tracked separately as
`DUPLICATED_RESPONSIBILITY`.

The index uses evidence-backed selectors for category, intent, scene type,
energy, duration, camera motion, framing, model, dependencies and conflicts.
Unknown selectors are not synthesized into recommendations.

## Runtime safety

This package is not registered or loaded by ApplicationFactory. Existing
router/injector/Director and PromptFacade boundaries remain untouched. It
cannot call providers, mutate Story Memory, bypass approval, write a Director
result, or compile `final_prompt`.

See inventory (production reference: `architecture/audits/TAB2_PROMPT_SKILL_INVENTORY.md`),
Director index (production reference: `skills/05-director/INDEX.yaml`), and
ADR-0001 (production reference: `architecture/ADR/0001-reference-skill-packaging.md`).
