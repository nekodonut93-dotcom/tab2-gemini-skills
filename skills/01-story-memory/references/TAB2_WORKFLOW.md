# Portable workflow

`INGEST → STORY MEMORY → CONTINUITY → WRITER → ENRICHMENT → DIRECTOR → PROMPT ENGINE → QUALITY AUDIT`

Move forward only when the current stage has a valid output, required evidence,
and no unresolved blocker. A stage may be skipped only when its contract says
it is optional (enrichment may return `NONE`). The orchestrator coordinates;
it does not perform child-stage responsibilities.

Before Writer or Director uses portable records, filter every fact, knowledge
item, relationship, and event by its visibility markers and the requested
chapter/scene. Missing, contradictory, or unknown visibility yields
`BLOCKED` / `UNRESOLVED`; never infer that a character knows a later reveal.

For Gemini portable video-prompt work, check the separate
`PROJECT_VISUAL_PROFILE.json` preference before Writer/Director prompt work.
If no resolved user choice exists, return `STYLE_UNRESOLVED`, ask the user, and
stop. This profile is not Story Memory and cannot change story semantics.

Production mappings: Story Memory / `StoryMemoryService`; derived continuity /
`FullStoryContinuityAnalyzer`; Writer / `ScreenplayApplicationService`;
Director / `DirectorFacade` + canonical workflow; final assembly /
`PromptFacade` → PromptEngine. See each package's source trace.
