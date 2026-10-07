# Fail-closed outcomes

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
