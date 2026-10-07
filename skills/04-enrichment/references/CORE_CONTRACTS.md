# Portable Tab 2 core contracts

**PORTABLE_WEB_STATE_ONLY guidance.** This package is for Gemini Web and
ChatGPT Web workflows. It does not replace production code, persistence, or
the frozen contract registries.

- Story Memory = persisted source-backed authority. A portable web state file
  is only a working copy and is not production Story Memory.
- Production Canon = derived continuity analysis/gate, not persisted truth.
- Writer owns WHAT: events, people, chronology, exact dialogue, relationships,
  objects, locations, knowledge, and outcomes.
- Director owns HOW: visual execution only, based on an accepted Writer scene.
- PromptEngine is the sole production final-assembly authority. A web model
  may produce a portable prompt draft but must not claim production
  PromptEngine validation.
- Respect source provenance, scene/chapter visibility, currentness, and
  character identity. Future or superseded facts are not visible by default.
- No future knowledge leak; unknown visibility means BLOCKED / UNRESOLVED.
- Do not invent dialogue, unsupported relationship semantics, locations, or
  props.
- Enrichment cannot change event, outcome, or state. It is optional and
  presentation-only.
- Fail closed when actor, evidence, identity, visibility, authority, or model
  compatibility is unresolved.

Frozen production identities remain unchanged: Writer FROZEN_V1,
DIRECTOR FROZEN_V1, and DirectorHandoffV2. Web schemas below are portable
exchange shapes, not replacements for those contracts.
