# Story Memory — portable stage excerpt

**Source package:** `skills/01-story-memory/SKILL.md`  
**Stage owner:** Production StoryMemoryService/Character Bible remain authoritative; portable state is not production memory.

## Authority

Production StoryMemoryService/Character Bible remain authoritative; portable state is not production memory.

## Input/output boundary

- Input: Current chapter/scene, source refs, character IDs, and Story Memory records with visibility and provenance.
- Output: story_memory_state with filtered visible_facts, visible_knowledge, characters, relationships, source_refs, and filter status.

## Safe advancement

- Validation: Require source_refs and explicit visibility for each fact/knowledge record; one canonical identity only where existing authority resolves it.
- Failure: Missing, ambiguous, future, superseded, or unknown visibility is BLOCKED/UNRESOLVED and must not be passed downstream.
- Next: Pass filtered context to CONTINUITY; do not pass raw future records.

This compact excerpt is for web distribution. The linked production code and
frozen tests remain authoritative.
