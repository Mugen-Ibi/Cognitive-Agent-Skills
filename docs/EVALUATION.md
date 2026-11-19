# Evaluation

Run `python3 scripts/validate.py` to check package metadata, references, and fixture consistency. The behavioral cases in `evals/cases.json` require a separate host run.

## Agent routing

Run each case with a fresh conversation and the specified host fixture. Set the starting model, expose only the listed worker targets, and simulate the stated failure when specified. A host fixture describes the test environment. Keep its expected route and evaluator notes out of the prompt. For implicit discovery, expose the catalog normally. For explicit invocation, load the packaged skill. Record the host version and model catalog.

| Observation | Pass condition |
|---|---|
| Executor | A material advantage leads to the expected target. Ties, model locks, and handoff overhead keep work local. |
| Dispatch | For a worker route, observe the native tool call, explicit target, worker result, and parent delivery. A suggested model name alone is insufficient. |
| Availability | Unavailable or denied routes yield an accurate fallback. A timed-out or partially completed write is reconciled before any retry. |
| Completion | The delivered answer or checked artifact satisfies the task and its original constraints. Workers execute directly and stay within the task. |
| Reporting | Any switch is described at the scope the host confirms. Distinguish requested and confirmed models. |

## Analysis and discovery

Retain the earlier decision-support cases. For the implementation case supply a disposable CSV fixture. Provide the proposal for review cases. Check explicit depth, safety, publication readiness, required independence, permission boundaries, and non-activation on routine requests. A mode announcement is optional.

To measure an improvement, compare the same starting model with and without the skill on identical inputs, permissions, and budgets. Record task success, elapsed time, tokens when available, and handoff failures. Read the dated [validation report](VALIDATION-REPORT.md) for the tests actually performed.
