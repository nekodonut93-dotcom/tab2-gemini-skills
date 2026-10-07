# Gemini Tab 2 portable core contracts

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
