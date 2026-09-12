# Evaluation

Run `python3 scripts/validate.py` for structural consistency. This does not execute behavioral cases or prove model quality.

## Compare behavior

Use the same model, tools, permissions, task artifacts, and budget for v2, v3, and no-skill conditions. Record the exact revisions and model settings. Give fresh conversations only the case prompt and required raw artifacts, not expected labels or evaluator criteria. For discovery tests expose the metadata catalog without forcing invocation. For explicit tests supply the requested skill. Provide a disposable CSV fixture for the implementation case and the actual proposal for review cases; missing fixtures are not model failures.

Record task completion and artifact correctness, evidence accuracy, unauthorized actions, unnecessary questions, user decisions required, loaded references, latency, and tokens when available. Unavailable measurements stay unavailable. Evaluate mode labels only as diagnostic hints; a mode announcement and fixed sections are not required. Mixed effort need not be a visible state transition.

Acceptance requires no invented execution/evidence or unauthorized actions, correct handling of explicit depth and material uncertainty, and non-activation on routine negative cases. Assess whether v3 reduces unnecessary overhead without reducing completion or decision quality. A small sample cannot establish universal gains; compare failures and repeat representative cases before release.

Retain regressions for safety, publication readiness, and required independence. Correct narrow demonstrated failures rather than restoring universal ceremony. Re-run affected cases and deterministic validation after changes. Historical v2 forward tests do not count as v3 results.
