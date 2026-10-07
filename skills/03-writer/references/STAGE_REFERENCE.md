# Writer — portable stage excerpt

**Source package:** `skills/03-writer/SKILL.md`  
**Stage owner:** Writer and ScreenplayApplicationService own WHAT; production readiness controls Director handoff.

## Authority

Writer and ScreenplayApplicationService own WHAT; production readiness controls Director handoff.

## Input/output boundary

- Input: Current chapter, relevant Story Memory, visible knowledge, relationships, source refs, and continuity result.
- Output: writer_scene records with identity/order, refs, events, actions, exact dialogue, relationship facts, outcome state, and unresolved items.

## Safe advancement

- Validation: Check writer_scene schema, exact refs, character and relationship identity, visible knowledge, and no camera/lens/movement/prompt-syntax fields.
- Failure: Missing evidence, identity conflict, unresolved visibility, or story-state drift blocks the scene/handoff.
- Next: A valid scene proceeds to optional ENRICHMENT; Writer readiness still gates any Director use.

This compact excerpt is for web distribution. The linked production code and
frozen tests remain authoritative.
