# Data authority

| Data | Authority | Gemini package boundary |
|---|---|---|
| Novel/source text and provenance | Source document | Cite and preserve exact evidence |
| Persisted identity, facts, knowledge and temporal visibility | StoryMemoryService / repository | Portable copy is not persisted Story Memory |
| Cross-chapter continuity/Production Canon | FullStoryContinuityAnalyzer derived gate | Do not promote its report to persisted source |
| Story events, identity, exact dialogue, relationship and outcome | Writer / ScreenplayApplicationService | Downstream is read-only |
| Visual-completion/action/choreography proposal | Portable reference layers only | Cannot change story state or imply production acceptance |
| Cinematic HOW | DirectorFacade / canonical Director workflow | Cannot mutate Writer WHAT |
| Final prompt text | PromptFacade → PromptEngine | Seedance portable `prompt_draft` is not a final production prompt |
| Visual style | Explicit project user preference | `PROJECT_VISUAL_PROFILE` is not Story Memory |
| Technical and spoken language preferences | Explicit project language preference | `PROJECT_LANGUAGE_PROFILE` is portable and distinct from Story Memory |
| Dola tag behavior | Current Dola UI only when confirmed | Unknown means REFERENCE_BINDING_UNVERIFIED |

Production reference: `source_evidence/architecture/TAB2_DATA_AUTHORITY.md`.
