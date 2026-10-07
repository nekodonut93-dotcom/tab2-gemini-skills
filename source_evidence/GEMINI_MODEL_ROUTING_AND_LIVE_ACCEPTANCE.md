# Gemini Model Routing and Live Story-Repair Acceptance

## Verdict

`GEMINI_MODEL_ROUTING_AND_LIVE_PARTIAL`

The latest live follow-up is recorded in
GEMINI_STABLE_LIVE_ACCEPTANCE.md (production reference: `architecture/GEMINI_STABLE_LIVE_ACCEPTANCE.md`):
LIGHT and DEFAULT live preflight passed, DEEP was unavailable, and live
discovery returned a schema-valid name discrepancy. Live resolution failed
closed before any repair or official scene. The content-analysis setting was
enabled only in the authorized validation process; it was not persisted.

## Configuration audit

The previous active generation default was `gemini-2.0-flash`, referenced by
`GeminiConfig`, the Google provider constructor, the environment fallback, and
the existing factory-to-Writer wiring. The stored `data/gemini_settings.json`
currently contains credentials only; it has no model-role or
`content_analysis_enabled` fields. The Gemini settings API currently manages
credentials only. The existing model configuration authority is
`GeminiConfig`: environment values override model fields in the existing
settings-store payload, which override role defaults. The legacy
`GEMINI_GENERATION_MODEL` environment setting remains a compatibility override
for the default reasoning role.

Active production defaults are now:

| Role | Default | Environment override |
|---|---|---|
| DEFAULT_REASONING_MODEL | `gemini-3.5-flash` | `GEMINI_DEFAULT_REASONING_MODEL` (or legacy `GEMINI_GENERATION_MODEL`) |
| LIGHT_REASONING_MODEL | `gemini-3.1-flash-lite` | `GEMINI_LIGHT_REASONING_MODEL` |
| DEEP_REASONING_MODEL | `gemini-3.1-pro-preview` | `GEMINI_DEEP_REASONING_MODEL` |

The defaults follow the requested semantic-role configuration. The current
follow-up performed live preflight: LIGHT and DEFAULT were available; DEEP was
unavailable and routes to DEFAULT. Role values that name the listed retired
Gemini 2.0 Flash variants or contain `live` are rejected for
story text/JSON work. The retired strings remain only in this rejection guard;
they are not active defaults or fallbacks. A Google model-catalog page was
inspected, but this does not substitute for the required authenticated
per-model preflight.

The Google provider accepts a per-request text-model override without mutating
its shared default. The existing `GeminiClient` still owns key selection,
rotation, quota accounting, retries, and transport. `StoryReasoningProvider`
routes chapter discovery to LIGHT; cross-chapter reconciliation and
critical/ambiguous resolution to DEEP; ordinary resolution, Canon Critic, and
probe diagnosis to DEFAULT. If LIGHT or DEEP is unavailable, it retries using
the configured DEFAULT role. A model-not-found response does not mark a valid
credential as failed. The actual selected model is included in the reasoning
cache key and trace; cached results therefore cannot cross model identities.

## Live setting and preflight

The safe configuration audit used the existing Gemini settings store and
environment without printing credentials:

- Configured credentials: **5**.
- Content analysis: **enabled for the authorized validation process only**;
  the normal persisted settings authority remains unchanged.
- Current effective model-role configuration: DEFAULT
  `gemini-3.5-flash`, LIGHT `gemini-3.1-flash-lite`, DEEP
  `gemini-3.1-pro-preview`.
- Persisted model-role fields: **none** in the current settings file.
- Actual effective models: LIGHT `gemini-3.1-flash-lite`, DEFAULT
  `gemini-3.5-flash`, DEEP fallback policy `gemini-3.5-flash`.
- Preflight: LIGHT and DEFAULT PASS; DEEP unavailable.
- Live Story Repair: real discovery succeeded; resolution subsequently failed
  closed. The full live acceptance remains PARTIAL.

`StoryReasoningProvider.preflight_configured_models()` validates distinct
configured role models through `GeminiClient` with a small role-tagged
structured JSON response. Optional unavailable LIGHT/DEEP models are marked
unavailable and fall back to DEFAULT; an unavailable DEFAULT prevents
reasoning from being accepted. The live role tests and their limitations are
documented in the stable live-acceptance report.

## Safety and error behavior

- One `StoryReasoningProvider` and the existing `GeminiClient` remain the
  reasoning and provider authorities.
- Disabled content analysis does not register a `GeminiClient` and therefore
  cannot silently dispatch a model request.
- Retired model and Gemini Live model values are rejected for story text roles.
- The provider model override is per request and does not mutate shared
  provider configuration.
- `GeminiModelUnavailable` is distinct from credential failure; it allows
  optional-role fallback without disabling API keys.
- Malformed structured output fails closed. The client does not mark a
  credential invalid for a model-generated malformed/invalid response.
- Safe overlay changes require exact, verbatim evidence bound to source
  references. Conservative normalized safe derivations may be distinct from
  the quote only when grounded in that quote; unsupported model-generated
  staging cannot be applied as a canon overlay.
- Provider error details are not appended to StoryReasoningProvider errors,
  reducing the risk of sensitive response data reaching application reports.
- `GeminiClient` bounds attempts across the entire key pool at
  `max_retries + 1` per logical request, preventing per-key retry
  multiplication. The latest live resolution made four attempts and all four
  were rate limited; no further calls were made.

## Files changed

- `ai_agent_brain/gemini/config.py` — reasoning-role defaults, environment and
  existing-store overrides, and retired/Live model validation.
- `ai_agent_brain/gemini/provider.py` — request-scoped model selection and
  unavailable-model detection.
- `ai_agent_brain/gemini/client.py`, `retry_handler.py`, and `exceptions.py` —
  canonical structured model preflight, safe model-unavailable handling, and
  total logical-request retry/failover budget.
- `application/runtime/application_factory.py` — role wiring and safe runtime
  status exposure.
- `application/screenwriter_intelligence/story_reasoning.py` — role routing,
  effective-model cache identity, optional-role fallback, role preflight,
  tighter incidental-participant instructions, and evidence failure reporting.
- `application/screenwriter_intelligence/full_story_continuity.py` — records
  effective model IDs, retries conflicting proposals through DEEP before
  acceptance, and separates exact source quotes from conservative normalized
  derivations.
- `tests/test_gemini_infrastructure.py` and `tests/test_story_reasoning.py` —
  offline role/configuration/fallback/cache/opt-in coverage.
- `architecture/GEMINI_LIVE_STORY_REPAIR_ACCEPTANCE.md` — marked as the
  historical pre-model-routing report.

No frozen Writer or Director contract, registry, or frozen test was changed.
Contract migration is not required.

## Verification

All commands ran against this workspace after the production changes:

| Validation | Result |
|---|---:|
| Focused Gemini infrastructure, reasoning connector, StoryReasoningProvider, and Full Story Continuity tests | 52 passed |
| Combined targeted Gemini, Story Memory, semantic foundation, adaptation, sequence, duration, continuity, readiness, and Professional Writer matrix | 154 passed |
| Frozen Writer and Director contract gate | 26 passed |
| Full Python suite | 1,838 passed in 568.44 seconds |
| `py_compile` for changed production and test modules | passed |

Live discovery and a common free-form issue label were verified; real
resolution, applied overlay, live critic, temporary Scene/Segment probes, live
diagnosis, API cache call-count behavior, and Writer official-scene trace are
**not verified**. See the detailed live report. Offline tests remain
deterministic and network-free.

## Remaining limitations

1. The DEEP model did not pass live preflight; DEFAULT fallback is configured,
   but a live deep-task fallback request was not completed.
2. Live discovery succeeded, but resolution failed. The real story-repair
   acceptance remains incomplete and PARTIAL.
3. The bounded live resolution failed with four rate-limit responses across
   four distinct credential attempts. Earlier per-key retry multiplication
   produced 22 calls (six 503 and fourteen 429); one logical request is now
   limited to four attempts by default. Quota was not deliberately altered.
4. The settings service does not currently persist model-role selection. Role
   overrides are available through the existing environment/config path; the
   current credentials settings API was not expanded into a second model
   settings authority.
