# Seedance portable prompt drafting

## Authority

This package creates a portable, user-reviewable Seedance prompt draft and
copyable sheet rows. It is not registered in production and does not replace
Writer, Director, PromptFacade, PromptEngine, PromptLanguageRenderer, or their
deterministic validation. Production final-prompt authority remains
PromptFacade → PromptEngine.

## Required sequence

1. Require an accepted Writer scene and current visible context.
2. Require a resolved `PROJECT_VISUAL_PROFILE`. If absent, return
   `STYLE_UNRESOLVED`, ask the user to choose a style, and stop before any
   Seedance prompt draft.
3. Bind only user-confirmed or UI-confirmed reference syntax. If Dola syntax
   cannot be verified from its current UI, return `REFERENCE_BINDING_UNVERIFIED`.
4. Keep Writer WHAT immutable. Apply visual completion and action choreography
   only as bounded presentation proposals; retain evidence and origin labels.
5. Build a timeline target for 5, 10, or 15 seconds using the matching
   strategy. Durations are targets, not frame-perfect locks.
6. Draft the ordered sections in `prompt_structure/seedance_prompt_v1.yaml`
   into `prompt_draft`. Do not include internal reasoning in the prompt text.
7. Create one copyable export row per prompt/scene/shot as required by the
   selected output scope; do not call a Sheets API.

## VFX and style

VFX depend on the resolved profile, explicit source/context, and the applicable
VFX policy together. The word "sword" alone never authorizes a trail, energy
arc, impact, or magic. `none` and `realistic_only` do not permit fantasy VFX.
Unknown style or unknown platform/model syntax remains unresolved, never
silently defaulted.

## Reference integrity

Keep identity, clothing, environment, action, camera, and style references in
separate roles. Preserve the uploaded assets' confirmed UI tags verbatim.
Single-image I2V may use an implicit uploaded image; do not invent `@Image1`.
Never blend reference roles or claim identity features not present in the
trusted identity source.

## Timing and output

Use `timing/5s.yaml`, `10s.yaml`, or `15s.yaml`; choose adaptive segments from
the scene's actual beats and ensure target durations sum to the selected clip
duration. Do not force empty beats or change scene order/outcome to fill time.
The internal `seedance_scene_package.schema.json` and `sheet_export.schema.json`
are portable interchange schemas only. CSV and XLSX-ready rows use the fields
in `sheet_export/README.md`; no spreadsheet service is invoked.

## Stop conditions

Return a non-success status instead of a prompt draft when style is unresolved,
Writer readiness is blocked, source/identity/visibility is unresolved,
reference binding is unverified, or the draft changes narrative state.
Quality audit must verify story truth, temporal visibility, Writer WHAT,
style, references, duration, VFX policy, end state, and absence of invented
platform syntax.
