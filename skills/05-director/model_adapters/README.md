# Model adapters — evidence status

Model adapters are separate from DIRECTING_KNOWLEDGE and prompt structure.
These records are reference-only and do not imply API capability.

| Model | Distribution status | Evidence |
|---|---|---|
| Seedance | VERIFIED_REFERENCE | Profile/template/adapter found; formatter tests exist |
| Veo | VERIFIED_REFERENCE | Profile/template/adapter found |
| Kling | VERIFIED_REFERENCE | Profile/template/adapter found; formatter tests exist |
| Sora | UNKNOWN / INCOMPLETE | Profile and registry entry found; checked-in PromptEngine template not found |
| Others in inventory | UNKNOWN | Do not infer adapter from a Skill compatibility list |

Required literal status: `SORA_PROMPT_TEMPLATE_STATUS = UNVERIFIED / INCOMPLETE`.
No Sora template or fallback is supplied by this distribution.
