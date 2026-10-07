# Gemini Stable Live Acceptance

## Verdict

`GEMINI_STABLE_LIVE_PARTIAL`

The application was run with the existing `GEMINI_CONTENT_ANALYSIS_ENABLED=true`
opt-in set for the validation process only. The real Gemini provider returned
valid structured preflight responses for LIGHT and DEFAULT, and live
`StoryReasoningProvider` discovery returned an evidence-backed name-discrepancy
candidate. The configured DEEP model was unavailable and was recorded as
unavailable; its defined fallback is DEFAULT.

The live flow did **not** complete: a real resolution request failed at the
provider layer and raised `StoryReasoningUnavailable`. A follow-up using a
globally bounded request budget again failed closed: discovery succeeded in
one HTTP request, then resolution received four HTTP 429 responses (one
attempt per credential, bounded to `max_retries + 1`, four by default). No
Production Canon repair was applied, no Canon Critic ran after a repair, and no
live Writer reread or official Story Scene was created. This report does not
claim live end-to-end repair acceptance.

## Authorized setting and model preflight

- Setting authority: existing `GEMINI_CONTENT_ANALYSIS_ENABLED` environment
  opt-in read by `GeminiConfig`. The persisted settings store has credentials
  but no content-analysis toggle. The opt-in was set only in the PowerShell
  process launching the disposable validation runtime; it was not persisted or
  applied to unrelated machine configuration.
- Runtime `content_analysis_enabled`: **true** during the live preflight and
  smoke invocations.
- Configured credentials: **5**. No credential value, substring, key label, or
  secret-bearing settings output is recorded.
- Models were tested sequentially through `ApplicationFactory` →
  `GeminiClient` → existing `KeyManager`/`KeyRotation` → Google provider.

| Role | Configured model | Live preflight | Effective routing after preflight |
|---|---|---|---|
| LIGHT | `gemini-3.1-flash-lite` | PASS — structured JSON accepted | `gemini-3.1-flash-lite` |
| DEFAULT | `gemini-3.5-flash` | PASS — structured JSON accepted | `gemini-3.5-flash` |
| DEEP | `gemini-3.1-pro-preview` | UNAVAILABLE | Falls back to configured DEFAULT, `gemini-3.5-flash` |

The preflight made one small role-specific structured-output request per
configured model role in the recorded successful preflight run. No source story
was included. The DEEP model was not accepted as live-available. The settings
configuration was not changed.

The short discovery smoke used the real LIGHT model and returned a valid
structured issue. Its live label was `Character Name Discrepancy`, bound to
references for the correct and variant names. The label is consumed as an
ordinary string, not checked against a closed issue-type enum. A live smoke
variant with the manager's work context established did not emit a separate
manager/profile issue. A truly novel defect family was not independently
demonstrated live.

## Live request outcomes and coverage

| Acceptance item | Result |
|---|---|
| Real Gemini JSON preflight | PASS for LIGHT and DEFAULT; DEEP unavailable |
| Real StoryReasoningProvider discovery | PASS; schema/evidence validation accepted the name discrepancy |
| Free-form issue type accepted | PASS for the live string label; novel unseen defect family not proven |
| Role-only manager false positive | Not emitted in the smoke fixture where work context was established |
| Real resolution | FAIL CLOSED: four HTTP 429 responses across four credentials; no resolution accepted |
| Safe repair / Production Canon overlay | NOT RUN after resolution failure |
| Source Story immutability | Preserved: live smoke submitted ephemeral text/evidence only; no source chunks or user projects were changed |
| Repair provenance | No repair was applied, so no live repair provenance trace exists |
| Canon Critic after repair | NOT RUN |
| Temporary Scene Probe | No live workflow reached the probe. Offline integration tests continue to verify diagnostic-only authority and no official scene promotion |
| Duration-aware Segment Probe | No live workflow reached the probe. Offline configured-duration tests remain green |
| Live probe-failure diagnosis | NOT RUN |
| Live cache duplicate-call proof | NOT COMPLETED; offline tests verify same-key hit and source/model/prompt invalidation |
| Live credential failover | Four distinct credential attempts observed for resolution; the global attempt budget prevented per-key retry multiplication |
| Writer second full reread | NOT REACHED |
| Official scene live trace | NOT REACHED |

Provider details and credentials were not printed or copied into this report.
The latest disposable live run instrumented the provider boundary safely:
discovery made one successful request; resolution made four requests, each
returning HTTP 429, across four distinct credential attempts. Earlier live
resolution before the bounded-failover fix made 22 requests (six 503 and
fourteen 429), demonstrating retry multiplication. The latest run is bounded
to four total attempts per logical request; no additional live calls were
made after the failed resolution.

## Production hardening from live evidence

1. Live discovery revealed that a terse role-only action could be treated as a
   continuity defect because a participant/location was not introduced.
   Discovery instructions now explicitly treat incidental role-only
   participants and concise actions as valid source writing, and prohibit
   inferring missing staging or scene transitions from that alone. A subsequent
   live fixture that established the work context returned only the name
   discrepancy, not a manager/profile issue.
2. Live output can contain non-verbatim or unavailable evidence. Evidence
   validation now reports whether references or exact-quote evidence failed
   without echoing model output or provider details. Invalid responses remain
   uncached and fail closed.
3. Proposed changes still require exact, verbatim source evidence bound to
   issue references. Safe derivations may use a normalized value when its
   words are grounded in that quote; the conservative canonical
   `location=dorm_room` normalization is accepted from “returns to dorm”.
   Corrected facts still require an exact quoted value. Unsupported staging
   such as `lying_on_bed` remains blocked.
4. Canonical preflight requests validate the expected role-tagged JSON shape.
   Model-unavailable errors remain distinct from credential errors; optional
   role fallback does not mark a valid key invalid.
5. Provider HTTP 408/429/5xx, timeout, and network failures retain typed,
   sanitized classifications. `GeminiClient` enforces one `max_retries + 1`
   attempt budget across the entire key pool rather than multiplying retries
   by credential count. Transient/network failures use the existing backoff;
   rate limits rotate to another available key without retrying the limited
   key.

No second client, key manager, settings store, reasoner, model router, scene
enrichment, or local NLP/ML system was introduced.

## Offline verification after production changes

| Validation | Result |
|---|---:|
| Focused Gemini infrastructure, reasoning connector, StoryReasoningProvider, and Full Story Continuity tests | 52 passed |
| Combined targeted Gemini, Story Memory, semantic foundation, adaptation, sequence, duration, continuity, readiness, and Professional Writer matrix | 154 passed |
| Frozen Writer and Director gates | 26 passed |
| Full Python suite | 1,838 passed in 568.44 seconds |
| Python syntax compilation | passed |

The offline full suite does not require network access. No Writer or Director
frozen contracts, registries, or frozen assertions changed. Contract migration
is not required.

## Remaining limitations

- The DEEP role model was unavailable in this live environment. DEFAULT
  fallback was confirmed by routing logic and offline tests, but a live
  deep-task completion through DEFAULT was not established.
- The live resolution failure prevented proof of a real repair, its provenance,
  post-repair Canon Critic, temporary probes, reread, or official scene.
- The bounded live resolution still encountered four rate limits. No further
  live calls were made to avoid additional quota use.
- Cache hit behavior, failover ownership, repair idempotency, malformed output,
  and API failure semantics have deterministic offline coverage but were not
  all demonstrated against live requests in this acceptance run.
- The live role-only control was not flagged when its work context was
  established; this does not establish that the model will never overflag
  concise incidental actions in other story contexts.

Until real resolution, repair, critique, probes, full reread, and official
scene creation all succeed through the live Professional Writer path, keep the
verdict `GEMINI_STABLE_LIVE_PARTIAL`.
