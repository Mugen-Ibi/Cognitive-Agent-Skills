# Agent routing in v4

The marketplace distributes one skill, `cognitive-router`. Its first decision is who can complete the task. The selected model is the baseline. The router compares candidates only when the host advertises them and the task gives a reason to switch. Its second decision is how much verification the deliverable needs.

## Selecting an executor

| Situation | Routing decision |
|---|---|
| Complex coding or professional analysis with interacting constraints | Consider GPT-6.2 Astra if its capabilities justify moving the work |
| Bounded, repetitive coding with a meaningful turnaround requirement | Consider GPT-6.2 Sol if the expected saving exceeds the handoff cost |
| Work that depends on inspecting a live visual surface | Consider a visual specialist only if it can access that surface |
| A tie, a small task, or high cost of transferring context | Continue in the current agent |
| An explicit model lock, budget ceiling, or delegation restriction | Limit eligible candidates to those satisfying the constraint |

These are qualitative preferences from the Codex model catalog. The host's advertised capabilities govern each invocation. No benchmark-derived speedup, cost ratio, or universal ranking is assumed.

## Executing a route

A host may support a scoped override directly. Codex can also dispatch one worker with an explicit model. A fresh context receives the task, required inputs, user constraints, and acceptance criteria. The worker performs the task directly. The parent waits, checks the result, and returns it in the original conversation. The worker's model applies to the delegated work. The parent keeps its session and model selection.

Tool access, scope, and permissions must hold in the execution context. The router checks in-flight state and partial changes before resuming a failed handoff. If no eligible route is exposed, it completes the feasible work in the current context and reports a material shortfall. A strict model requirement still applies.

## Analysis and packaging

The existing Lite, Standard, High Precision, and evidence references remain conditional. Any eligible executor may apply any needed depth. The package uses native host tools, with a portable manifest and a Codex compatibility manifest pointing to the same skill. Implicit discovery depends on the host. See the [evaluation procedure](EVALUATION.md) for how to distinguish a proposed route from completed execution.
