# Tab 2 frozen contracts and deterministic enforcement

## Frozen registries

- Writer: `architecture/writer_contract_freeze_v1.json`, **20** frozen
  contract rows in its manifest; gate: `tests/test_writer_frozen_contracts.py`.
- Director: `architecture/director_contract_freeze_v1.json`, **23**
  `DIRECTOR FROZEN_V1` contracts; gate:
  `tests/test_director_frozen_contracts.py`.
- Writer → Director handoff remains `DirectorHandoffV2`.

The registries freeze observable identity, compatibility, provenance,
precedence, currentness and ownership semantics—not prompts, heuristics or
internal storage layouts.

## Invariants that remain code-enforced

- project/document/chapter/screenplay/scene/block identity and version binding;
- Story Memory alias resolution and collision/ambiguity behavior;
- source-reference validation and temporal visibility;
- official Production Canon status and reread readiness;
- Writer WHAT immutability at the Director boundary;
- user lock / hard-constraint precedence and compatible model gating;
- Director result compatibility/currentness and idempotency;
- prompt context/output shape, schema validation and exact final prompt source;
- job retries and idempotency keys.

These responsibilities must not be converted into SKILL.md-only instructions.
Skills may state the invariant and link to its implementation; code remains
the enforcement authority.

## FROZEN_V1 impact

This audit/packaging phase changed no public schema, registry, frozen test,
Writer/Director contract, `DirectorHandoffV2`, cache-currentness semantics, or
prompt authority. The new SKILL documents are not runtime-loaded. No contract
migration is required.

Future breaking semantics require an explicitly declared `CONTRACT MIGRATION`
and the applicable Writer or Director migration protocol.
