# Tab 2 Output Sheets / Scene Copy Phase 2

## 1 Files Changed

Added:

- tab2_output_projection.py (production reference: `application/tab2_output_projection.py`)
- test_tab2_output_projection_phase2.py (production reference: `tests/test_tab2_output_projection_phase2.py`)
- This report

Updated:

- professional_canonical_pipeline.py (production reference: `application/professional_canonical_pipeline.py`)
- project_workspace.py (production reference: `application/services/project_workspace.py`)
- routes.py (production reference: `application/api/routes.py`)
- server.py (production reference: `application/api/server.py`)
- application-adapter.js (production reference: `ui/application-adapter.js`)
- application_factory.py (production reference: `application/runtime/application_factory.py`)
- test_professional_writer_workflow.py (production reference: `tests/test_professional_writer_workflow.py`)

No Writer, Director, PromptEngine, Sheet export, Character Reference, chapter
splitter, or long-story algorithms were changed.

## 2 Existing UI Reused

The existing Tab 2 Story UI was reused:

- Character Sheet table
- Scene Prompt Sheet table
- Scene detail area
- existing Story workspace panel anchor

No parallel Sheet subsystem or new Tab was created.

## 3 Output Projection Architecture

```text
Quick Story result ───────┐
                          ├─ Tab2OutputProjection → Character rows
Professional canonical ──┘                         Video Prompt rows
                                                    Scene Copy rows
```

The projection layer is read-only. It does not analyze Story, run Director,
run PromptEngine, mutate Writer artifacts, or create new Scene truth.

## 4 Professional Result Adapter

`Tab2OutputProjection.professional()` consumes the canonical pipeline result:

```text
DirectorHandoffV2
Director results
VideoPromptPackage results
Writer character snapshot
```

It produces stable Character Sheet and Video Prompt Sheet rows with identity
metadata.

## 5 Quick Result Adapter

`Tab2OutputProjection.quick()` consumes the existing Quick Story result shape,
including its `story_identity`, `scenes`, `characters`, and `video_prompts`.

Quick scene order is preserved from the result sequence. No alphabetical ID
sorting is introduced.

## 6 Character Sheet

Professional rows use existing Writer character data from the screenplay
context snapshot. Available fields include:

- character ID
- name
- appearance
- costume
- personality
- relationships where present
- project/document/screenplay identity

Missing values remain empty. Characters are not reconstructed from prompts and
no Character Reference bridge was added.

## 7 Video Prompt Sheet

Each row represents an existing Writer Scene / Director output unit.

Displayed fields include, where available:

- project/document/chapter/screenplay/scene identity
- scene order
- characters
- environment
- action
- duration
- camera
- lighting
- motion
- composition
- style
- model
- final video prompt
- status

No shot subdivision is invented when the Director result does not provide one.

## 8 Scene Copy View

The existing Story workspace now renders a Scene Copy View for canonical
Professional output. Each Scene has its own Copy Prompt button.

## 9 Copy Behavior

Copy uses only `VideoPromptPackage.final_prompt`.

It does not copy:

- JSON metadata
- Director traces
- identity metadata
- neighboring scenes

Successful copy displays `Đã sao chép prompt` without reloading the page or
mutating project data.

## 10 Identity Mapping

Projection preserves:

- project ID
- document ID when available
- chapter ID
- screenplay ID
- scene ID
- provenance from the canonical Prompt package

UI row indexes are never used as identity.

## 11 Prompt Source of Truth

The displayed prompt is exactly the final prompt produced by:

```text
PromptFacade
→ PromptEngine
→ VideoPromptPackage.final_prompt
```

The projection layer does not call PromptEngine again.

## 12 Persistence

Professional canonical output is persisted at the existing project workspace:

```text
<project>/analysis/professional_output.json
```

The workspace provides `save_professional_output()` and
`load_professional_output()`. Existing Quick Story persistence remains
unchanged.

## 13 Quick Compatibility

Quick Story continues to render through its existing path and now has a shared
projection adapter available without changing its orchestration.

No `ui-project` fallback or cross-project lookup was added.

## 14 Tests

Focused Phase 2 projection and pipeline tests cover:

- Professional prompt rows use the exact final prompt.
- Director values appear only from Director output.
- Scene order and IDs remain correct.
- Quick projection preserves existing order and identity.
- Professional output persists and reloads.
- Existing canonical pipeline and Story behavior remain green.

## 15 Full Regression

Final results:

- Full Python suite: `1032 passed`
- JavaScript UI suite: `5/5 passed`

## 16 Remaining Long Story Work

Not implemented:

- chapter splitting
- pagination redesign
- long-story orchestration
- Character Reference bridge
- Writer improvements
- Director improvements

## 17 Final Acceptance

Phase 2 is accepted when:

- Professional output appears in Character Sheet.
- Final prompts appear in Video Prompt Sheet.
- Scenes appear in Scene Copy View.
- Every Scene has a Copy Prompt action.
- Copied text equals the canonical final prompt.
- No second prompt generation pipeline exists.
- Sheet remains projection-only.
- Identity remains correct.
- Quick Story remains compatible.
- Full Python and JavaScript regression suites pass.
