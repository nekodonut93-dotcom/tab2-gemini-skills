# BAD example

Reject or block this behavior: Do not rewrite the whole pipeline, silently repair unsupported facts, claim frozen-gate success from web checks, or call providers.

Do not silently repair it into a passing result. Preserve the failure and
recommend the narrowest return stage.
