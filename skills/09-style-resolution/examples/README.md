# Style resolution examples

## BLOCKED — no profile exists

Return `STYLE_UNRESOLVED`, ask which style to use, and stop before final-prompt
drafting. Do not infer from a novel's genre, setting, or character details.

## GOOD — explicit preset selection

The user selects `cn_3d_comedic_chibi`. Save the preset values and the user's
selection in the project's portable `PROJECT_VISUAL_PROFILE.json`. Keep it
separate from Story Memory.

## BAD — inferred style

The novel contains swords and a historical setting, so the assistant silently
selects `wuxia_cinematic`. This is invalid because the user did not choose it.
