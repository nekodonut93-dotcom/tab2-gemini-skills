# PromptEngine — portable stage excerpt

**Source package:** `skills/06-prompt-engine/SKILL.md`  
**Stage owner:** Production PromptFacade → PromptEngine is the sole production final-assembly authority.

## Authority

Production PromptFacade → PromptEngine is the sole production final-assembly authority.

## Input/output boundary

- Input: Writer scene, Director plan, verified model adapter, prompt structure, and language preference.
- Output: prompt_package with linked inputs, structured sections, final_prompt if supported, validation warnings, and refs.

## Safe advancement

- Validation: Check references, writer_what_preserved=true, duration if required by supplied contract, model syntax evidence, and prompt completeness.
- Failure: Missing input, unsupported/unverified adapter, incomplete required structure, or Writer WHAT drift blocks output.
- Next: Send package to QUALITY AUDIT; Sora remains UNVERIFIED / INCOMPLETE because no checked-in production template was found.

This compact excerpt is for web distribution. The linked production code and
frozen tests remain authoritative.
