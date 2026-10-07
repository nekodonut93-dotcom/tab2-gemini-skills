# 04E Chibi Performance and Inner-Monologue Visualizer

## ROLE
Route source-established inner monologue and reactions into an optional,
short chibi performance without changing story reality.

## AUTHORITY
This package is reference-only presentation guidance. Writer owns story WHAT,
source dialogue and source internal monologue. Story Memory remains the
persisted authority. Director owns production HOW. PromptFacade → PromptEngine
remains sole production final-prompt authority.

## INPUT
Accepted Writer scene, typed source expressions/actions, current chapter and
scene visibility, resolved PROJECT_VISUAL_PROFILE and PROJECT_LANGUAGE_PROFILE,
source references, scene tone, character personality and adjacent beats.

## OUTPUT
A contextual mode choice or no insert; typed source text remains unchanged.
Each symbolic action uses `CHIBI_SYMBOLIC_ACTION`, `representation_scope:
NON_DIEGETIC`, and `story_state_effect: NONE`.

## WORKFLOW
1. Distinguish SPOKEN_DIALOGUE, INTERNAL_MONOLOGUE, NARRATOR_VOICE_OVER,
   NONVERBAL_REACTION and ON_SCREEN_TEXT.
2. Preserve each source string verbatim and carry its own language label.
3. Require a resolved visual profile. If `chibi_insertions` is false, do not
   create a chibi insert.
4. If `inner_monologue` is false, do not render the source thought as speech
   or voice-over; a grounded nonverbal reaction may still be considered. If
   inner monologue is enabled but chibi is disabled, use source-faithful
   ordinary voice/reaction. If both are enabled, choose contextually among voice-only,
   chibi-spoken monologue, nonverbal reaction, symbolic pantomime or brief
   emotion burst. Do not force every monologue into chibi.
5. Choose from candidate pools using scene tone, character personality,
   selected style, intensity, timing, previous beat and next beat. Never map
   one emotion to one fixed gesture.
6. Keep the insert brief and return immediately to the same main-world scene,
   identity, dialogue, props and end state. Use a full-chibi scene only when
   the user profile explicitly sets `full_chibi_scene: true`.
7. Keep actual action choreography and chibi symbolic choreography in
   separate namespaces: `REAL_ACTION` requires source-event evidence; symbolic
   pantomime uses `CHIBI_SYMBOLIC_ACTION`.

## ALLOWED
- CHIBI_SPOKEN_MONOLOGUE using exact source internal-monologue text.
- CHIBI_NONVERBAL_REACTION without added words.
- CHIBI_SYMBOLIC_PANTOMIME and CHIBI_EMOTION_BURST with no real-world effect.
- Symbolic air punches/kicks, exaggerated tears, motion marks or other
  profile/style-supported candidates.
- A nonverbal chibi reaction when no source monologue exists, if contextual
  comedy and the selected profile support it.

## FORBIDDEN
- Invented, paraphrased or translated source dialogue or internal monologue.
- Any new thought when source contains no internal monologue.
- A real punch/kick, real target contact, injury or fight created from symbolic
  anger or pantomime.
- Real crying unless the source establishes it.
- Turning a symbolic chibi action into an event in Story Memory.
- Changing location, relationship, knowledge, possession, physical state,
  outcome or plot event.
- Extending chibi style to the whole scene unless explicitly selected.

## FAIL CONDITIONS
Unresolved style/language profile; chibi disabled; unsupported real-world
action/crying; missing source text for voiced content; symbolic action lacks
NON_DIEGETIC/NONE markers; story state changes; or no clear return to the
main-world scene.

## VALIDATION
Check source-text equality, content type and language, chibi permission,
duration/bounds, namespace separation, `representation_scope`,
`story_state_effect`, real-world target/injury state, and return continuity.
Do not claim production validation.

## NEXT STAGE
Pass separate source expression and optional symbolic visual records to the
Seedance portable draft. Writer WHAT and Story Memory remain unchanged.

## REFERENCES
- `grammars/`
- `inner_monologue/`
- `constraints/`
- `examples/`
- `../language/` in the independent distribution
- `../../architecture/TAB2_DATA_AUTHORITY.md`
- `../../architecture/TAB2_FROZEN_CONTRACTS.md`
