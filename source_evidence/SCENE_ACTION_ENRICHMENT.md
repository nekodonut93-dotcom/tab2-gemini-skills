# Scene Action Enrichment

## Status

Offline acceptance: **PASS**  
Live Gemini acceptance: **SCENE_ACTION_ENRICHMENT_LIVE_PARTIAL**

This change adds a bounded, derived visual-expression pass to the existing
official Story Scene workflow. It does not change Source Story, Production
Canon, frozen Writer or Director contracts, or introduce a parallel
Screen Adaptation authority.

## Integration and authority

The official screenplay flow first completes Production Canon analysis and the
Writer full-canon reread. Only when both completion markers and a source hash
are present does `ScreenplayApplicationService.create_draft` call
`DeterministicWriterProvider.enrich_official_scene` for completed scenes. The
call occurs before screenplay validation, duration segmentation, sequence
planning, and persistence.

The existing `StoryReasoningProvider` uses the configured reasoning client and
DEFAULT model role for `enrich_scene_visuals`. Its operation-specific prompt
version and context digest participate in the existing persistent reasoning
cache. The resulting derived actions and provenance are recorded in the
existing `writer_screen_adaptation` context. Source Story and Production Canon
remain unmodified; generated descriptions are ordinary screenplay action
blocks and continue through existing validation and Director handoff paths.

## Proposal context and safety checks

The reasoning request is scene-scoped and includes bound source evidence,
scene goal/action/outcome, characters, established emotion, heading/time,
narrative layer, existing props and actions, exact dialogue, continuity
requirements, and adjacent-scene summaries. It does not include output
duration.

The model may propose open-ended visual expression types. Local validation
then rejects proposals without valid bound source evidence, confidence below
0.80, a known anchor or character, compatible reality layer, continuity
support, or required prop support. It also rejects duplicate actions,
Director camera instructions, and consequential/state-changing proposals.
Accepted actions are inserted as a derived adaptation layer anchored to an
existing block; dialogue and source-event content are preserved.

Conservative eligibility skips scenes that already have at least two action
blocks, and skips a one-action scene when no emotion is established. Missing
bound source evidence is explicitly skipped. No-op and unavailable reasoning
results leave the scene unchanged and are reported in the existing adaptation
context. Provider unavailability is not represented as successful enrichment.

Writer Critic checks enrichment provenance, duplicate actions, consequence and
state metadata, continuity basis, overload, and whether the enriched scene
fingerprint has become stale. Existing Screen Adaptation and Writer-to-Director
V2 handoff remain the downstream authorities.

## Focused verification

The official-flow integration test verifies that enrichment runs after the
full Canon reread, persists with the screenplay, leaves the source text and
stored story chunk unchanged, is accepted by Writer Critic, becomes stale
when its underlying scene changes, appears in the existing Director V2
handoff, and reuses the persistent reasoning cache after reopening the
runtime.

The enrichment tests also cover open-ended enrichment types, no-op and
unavailable behavior, consequence and unsupported-prop rejection, continuity,
dialogue preservation, dream-layer preservation, malformed cross-scene
responses, and duplicate/cache idempotency.

## Generalization lock baseline

`tests/fixtures/writer_action_grounding_baseline_v1.json` is the permanent,
checked-in 20-safe / 10-unsafe structural-grounding benchmark. The earlier
20-safe / 10-unsafe audit cases could not be reconstructed from available
repository logs or session artifacts, so this fixture is explicitly a new
`BASELINE_V1`; it is not an exact before/after replay.

Structural actor aliases are assembled from the current scene's Character
Bible names, resolved Story Memory identity names and recorded aliases, and
Writer context character scope. Only identities in the current scene are
included. Pronouns resolve only for a single current-scene character or a
uniquely gender-matched character when every participant's gender is known;
ambiguous actors and unmapped cross-script names remain unresolved. No
transliteration is inferred.

The baseline reports 100% safe acceptance and 100% unsafe rejection. Five of
30 cases are unresolved, including the emotion-only and ambiguity controls
plus two novel unsafe sentence forms; unresolved cases fail closed. The
five-chapter quota acceptance still observes 5 discovery calls, 0 enrichment
calls, 0 Director semantic calls, and 0 embedding calls.

Current-workspace results:

- Writer enrichment and integration regression matrix: **250 passed**
- Frozen Writer and Director contract gates: **26 passed**
- Full Python suite: **1855 passed in 607.14s**

No frozen Writer or Director contract, registry, or frozen test was changed.
Contract migration is not required.

## Live acceptance

One disposable Vietnamese-scene enrichment operation was attempted on
2026-10-05 using the runtime-created `GeminiClient`,
`StoryReasoningProvider`, configured DEFAULT role, and the canonical
`DeterministicWriterProvider.enrich_official_scene` entry point. The content
analysis opt-in was set only in that process environment. The repository's
configured Gemini settings supplied **5 credentials**; no credential values
were printed or changed. The configured role was `DEFAULT`, routed to
`gemini-3.5-flash`.

The operation reached the real Gemini provider dispatch but returned
`ENRICHMENT_UNAVAILABLE` after **4 provider dispatch attempts** within the
existing bounded retry/failover path. The exact upstream status category was
not exposed by the canonical enrichment outcome. No further live calls were
made. The result was not converted into an AI no-op or cached as a successful
result.

| Acceptance check | Result |
|---|---|
| Screen Adaptation remains the single staging authority | YES |
| Real external Gemini request occurred | YES; one logical enrichment operation, 4 bounded dispatch attempts |
| Live enrichment succeeded | NO — `LIVE_SCENE_ENRICHMENT_NOT_VERIFIED` |
| Actual live free-form `enrichment_type` | Not available; provider returned unavailable |
| Live free-form type accepted / safe visual action applied | Not exercised; no valid live response |
| First-call cache | Unavailable result; no successful result cached |
| Second identical live call / live cache hit | Skipped to avoid further quota use |
| Unsupported consequential proposal blocked | YES in offline local-gate tests; no live proposal was returned |
| Offline no-op handling | YES; covered by regression tests |
| Role-only no-op case | `SKIPPED_FOR_QUOTA` |
| Exact Vietnamese dialogue | YES; exact before/after string comparison |
| Disposable Source Story snapshot | YES; hash unchanged |
| Disposable Canon fact snapshot | YES; hash unchanged |
| Continuity facts and semantic scene fields | YES; unchanged |
| Duration triggered another enrichment call | NO; duration is not an enrichment input |
| Production source code changed for this attempt | NO |
| Frozen Writer/Director contracts changed | NO |
| Contract migration required | NO |

The fixture contained the established anger/look action and an explicit
already-seated continuity fact; unsupported violence, object-breaking, leaving,
and attack were excluded from its Canon snapshot. Since the provider failed,
the returned scene was unchanged. Successful safe enrichment and free-form
type handling remain established by offline tests, not by live output.

The existing local safety gate was exercised offline with scripted
state-changing proposals. Unsupported consequential proposals were rejected;
the same tests verify unsupported props, continuity conflicts, and
Director-level camera instructions are rejected. Offline no-op behavior,
cache-hit behavior, and persistent cache reuse are also covered.

Writer Critic acceptance and stale-enrichment detection, persistence, and the
existing Director V2 handoff were verified by the official-flow integration
test. No new handoff or quality authority was introduced.

Regression results for the unchanged production implementation:

- Scene enrichment, Screen Adaptation, StoryReasoning, and Gemini tests:
  **63 passed** (rerun after the live attempt)
- Frozen Writer and Director gates: **26 passed** (rerun after the live attempt)
- Broader Writer enrichment/integration matrix: **250 passed**
- Full Python suite: **1855 passed in 607.14s** (latest complete suite run;
  no production code changed afterward)

## Limitations

Live Gemini enrichment and actual model-produced content remain unverified:
**LIVE_SCENE_ENRICHMENT_NOT_VERIFIED**. This acceptance therefore remains
**SCENE_ACTION_ENRICHMENT_LIVE_PARTIAL**, not PASS. Live Case B and a second
identical request were intentionally skipped; consequently live cache-hit and
live duplicate-external-call prevention were not directly observed in this
attempt. Offline cache/idempotency and official persistence coverage remain
green.

Eligibility is intentionally conservative: a one-action scene without an
established emotion is skipped, and an already filmable scene with two or more
action blocks is not sent for enrichment. Automatic emotion derivation for
those skipped one-action scenes is outside this change.
