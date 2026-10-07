# Quality, frozen-contract and quota audit

Use this reference to map each observable behavior to its deterministic
validator, frozen gate and offline regression. Report measured fixture results
as fixture-specific; do not present them as universal cost limits.

- Writer registry and gate: `writer_contract_freeze_v1.json`,
  `test_writer_frozen_contracts.py`.
- Director registry and gate: `director_contract_freeze_v1.json`,
  `test_director_frozen_contracts.py`.
- Handoff shape/ownership: `DirectorHandoffV2`.
- Grounding generalization: permanent `BASELINE_V1` fixture and benchmark;
  historical audit matrix was unavailable, so no before/after equivalence is
  claimed.
- Five-chapter quota acceptance is the exact scripted scenario in
  `test_tab2_targeted_quota_acceptance.py`, not a universal ceiling.
- Never weaken frozen tests, change registries or skip the production path to
  make an audit pass.
- For portable Seedance drafts, separately report profile resolution,
  reference-binding status, Writer WHAT preservation, style/VFX compliance,
  timeline target, identity continuity, and export-row completeness. Such
  checks do not certify PromptEngine output or Gemini model quality.

## Implementation and tests

- Quota/cache/retry: `architecture/TAB2_QUOTA_CACHE_RETRY.md`
- Contracts: `architecture/TAB2_FROZEN_CONTRACTS.md`
- Grounding: `architecture/SCENE_ACTION_ENRICHMENT.md`
- Tests: frozen gates, Writer/Story Memory/continuity suites, PromptEngine
  assembly suites, the targeted five-chapter quota test, and
  `tests/test_gemini_seedance_skill_contracts.py`.
