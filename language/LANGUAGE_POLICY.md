# Language policy — Gemini-facing reference

This is a portable user preference package, not production runtime authority.
Prompt rendering language and spoken/source language are independent:

**PROMPT_LANGUAGE != SPOKEN_LANGUAGE**

Technical camera/action/style instructions may be written in the selected
`prompt_language` (for example English). Source spoken dialogue and source
internal monologue remain verbatim in their source language and are labeled
with their own language. Source narrator/voice-over remains verbatim when the
user enables it in `PROJECT_LANGUAGE_PROFILE`. Do not infer a profile from a
Vietnamese novel or translate its dialogue because technical instructions use
English.

Before drafting, resolve the portable profile by asking the user if needed.
The schema example uses Vietnamese source and speech with English technical
prompt text; the unresolved template does not silently choose these values.

PromptEngine evidence: production accepts a `prompt_language`, normalizes
English/Vietnamese/Chinese, optionally translates technical prompt content,
and can protect source strings supplied by its caller. That implementation
does not establish a separate project-wide source/spoken-language profile or
prove every dialogue path is protected. This package only states the
Gemini-facing policy and cannot certify production or Gemini compliance.

Typed content categories:

- `SPOKEN_DIALOGUE`
- `INTERNAL_MONOLOGUE`
- `NARRATOR_VOICE_OVER`
- `NONVERBAL_REACTION`
- `ON_SCREEN_TEXT`

Do not combine these into a generic `dialogue` field. Do not create speech,
thought, narration, captions, signs, or on-screen text absent source/user
authorization.
