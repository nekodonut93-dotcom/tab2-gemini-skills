# Gemini full-pipeline benchmark status

## Evidence available

`gemini_seedance_skill_cases_v1.json` is a synthetic offline contract fixture.
`gemini_language_chibi_cases_v1.json` is an offline deterministic contract
fixture for independent language profiles and symbolic chibi safety.
Production regressions are mapped in `../validation/production_test_map.json`.
Neither is a full-pipeline Gemini Web benchmark.

## Full-pipeline benchmark: NOT RUN

No live Gemini/OpenAI calls are made by this repository. A future user-run
benchmark must evaluate source → portable state/visibility → continuity →
Writer WHAT → conditional enrichment → optional visual/action references →
Director HOW → Seedance prompt draft → quality audit. Record the model and
version, prompt and repository versions, input fixture ids, expected hard
invariants, output artifacts, repeatability, failures, and reviewer decision.
Do not convert the absence of a live run into a passing score.

Cases already present in the source fixture cover profile gating, Dola
reference uncertainty, action specificity, style examples and sheet output.
They do not measure the model's behavior.
