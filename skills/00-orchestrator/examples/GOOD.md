# GOOD example

The object below is a minimal portable exchange illustration for this stage.
It contains no new production behavior; validate it against the package schema.

```json
{
  "state_scope": "PORTABLE_WEB_STATE_ONLY",
  "status": "BLOCKED",
  "failed_stage": "CONTINUITY",
  "reason": "Required continuity result is blocked.",
  "recommended_return_stage": "CONTINUITY",
  "checks": {
    "continuity": "BLOCKED"
  },
  "source_refs": []
}
```
