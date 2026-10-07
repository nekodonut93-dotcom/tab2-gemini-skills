# Tab 2 Gemini Skills

An independent, portable Gemini-facing reference repository built from
verified production architecture, frozen registries, existing Gemini
distribution files, source skills, schemas, fixtures and test mappings.

**Production remains the source of truth. This repository is not runtime
authority.** It contains no production application Python implementation.
The only Python script is the deterministic exporter/validator.

## Build from the production workspace

From the parent production workspace:

```powershell
py -3.13 tab2-gemini-skills\build_from_production.py --build
```

The build reads the parent workspace, copies only reference material, runs
offline package validation, writes a provenance index, and verifies source
contract hashes against the recorded baseline. The first build creates the
frozen-hash baseline from the observed production snapshot; subsequent builds
fail if either frozen registry differs. Run the production frozen tests
separately before distributing.

Generate the Vietnamese Word guide only after a successful build:

```powershell
py -3.13 tab2-gemini-skills\generate_word_guide.py
```

The Word generator reads only files inside this repository. Neither command
makes a live Gemini/OpenAI call or invokes production API routes.

## Top-level layout

- `00_CORE/`: authority, workflow, creative boundary and failure rules.
- `project_state/`: portable project templates and schemas.
- `skills/`: 14 Gemini-facing stage/reference packages.
- `language/`: portable profile and typed-source-text rules.
- `seedance/`: consolidated Seedance, timing, reference and Dola guidance.
- `source_evidence/`: selected architecture docs and frozen registry snapshots.
- `audit/`: evidence-based capability classifications.
- `benchmarks/`: offline synthetic contract cases and mapped production tests.
- `validation/`: hash baseline, test map and build checks.
- `docs/generated/`: generated Vietnamese architecture guide after validation.

`SOURCE_MANIFEST.json` maps every packaged file to source production paths,
skill/schema version, distribution version, reference-only status and known
gaps.
