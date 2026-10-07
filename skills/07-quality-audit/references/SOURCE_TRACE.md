# Source trace

- Source reference skill: `skills/07-quality-audit/SKILL.md`
- Source manifest: `skills/07-quality-audit/manifest.yaml`
- Source identity/version: `tab2.quality-and-regression-audit` / `1.1.0`
- Distribution package status: web reference only; no production registration.

## Production implementation

- `architecture/writer_contract_freeze_v1.json`
- `architecture/director_contract_freeze_v1.json`
- `tests/fixtures/writer_action_grounding_baseline_v1.json`

## Source functions

- `benchmark test in tests/test_writer_action_grounding_benchmark.py`

## Tests

- `tests/test_writer_frozen_contracts.py`
- `tests/test_director_frozen_contracts.py`
- `tests/test_writer_action_grounding_benchmark.py`
- `tests/test_tab2_targeted_quota_acceptance.py`
- `tests/test_jobs.py`
- `tests/test_gemini_seedance_skill_contracts.py`

## Architecture and contracts

- `architecture/TAB2_FROZEN_CONTRACTS.md`
- `architecture/TAB2_QUOTA_CACHE_RETRY.md`
- `architecture/writer_contract_freeze_v1.json`
- `architecture/director_contract_freeze_v1.json`

This source trace is navigational evidence, not a replacement for reading the
implementation, test, or frozen registry.
