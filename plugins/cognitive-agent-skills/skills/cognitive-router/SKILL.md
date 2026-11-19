---
name: cognitive-router
description: Automatically route work to the best available agent and model for the task. Use for complex engineering, specialist tool work, decisions with competing options, or explicit routing requests. Handle routine edits and explanations directly unless routing would materially help.
---

# Cognitive Router

Deliver the requested outcome with the best available executor. Treat the user's selected model as the starting preference. A clear instruction such as “only use this model”, “no delegation”, or a budget ceiling is a constraint. If the user only wants a model recommendation, answer without dispatching.

## Select and run the agent

1. Identify what determines success for this request. Compare the current agent with targets actually exposed by the host on required tools, access to artifacts, task difficulty, latency, and any user constraints. A model name alone does not establish tool access. Keep the current agent on ties, for short tasks where handoff costs more than it saves, or when there is no supported better route.
2. On hosts advertising these models, prefer `gpt-6.2-sol` for bounded coding batches when turnaround dominates and `gpt-6.2-astra` for complex engineering or professional analysis where interacting constraints can invalidate an otherwise plausible answer. Judge the work behind the deliverable even if the user wants a short response. Prefer a visual/computer-use specialist such as `gpt-6.1-terra` when interaction is the limiting factor and it can access the relevant surface. Use the host's current capability descriptions if they differ.
3. When a permitted target has a material advantage, **execute the route automatically**. Use the host's scoped model selection if exposed, otherwise delegate the deliverable to one model-selectable worker. On Codex use the native spawn tool with the explicit advertised model ID. When its schema offers `fork_turns`, use `none` for an override and send a self-contained brief. Include the relevant inputs or accessible paths, scope, constraints, requested depth, and acceptance check. Instruct the worker to execute directly and return its result without rerouting. If already the designated worker, do the work locally.
4. Await the worker, handle follow-up in the same worker when appropriate, and verify the returned artifact or answer before delivering it. Give a brief reason and identify the actual execution path when switching. A child executes its assigned work while the parent chat keeps its selected model. Only report a confirmed model when the host identifies it; distinguish a requested model from a verified one.

If the preferred target, override, or delegation is unavailable, finish what the current agent can do and disclose the limitation when it affects the result or an explicitly requested route. If a running handoff times out, check its status before retrying. After failure, inspect partial work before resuming; keep a single writer for each affected artifact. Respect strict model pins even on fallback. Use the host's existing controls and permissions throughout.

## Choose analysis depth within the route

Use consequence, reversibility, and decision-changing uncertainty to choose effort; no numerical score or mode announcement is needed.

- **Lite:** a disposable or easily corrected choice. Answer directly with the decisive reason; no reference is normally needed.
- **Standard:** interacting constraints or meaningful trade-offs. Use [standard.md](references/standard.md) when comparison or reframing needs structure.
- **High Precision:** consequential reliance, costly reversal, or an explicitly required audit trail. Use [high-precision.md](references/high-precision.md) for these decisions.

Honor an explicit mode request while retaining necessary evidence and safety checks. Increase rigor for the affected part when new evidence raises the stakes. High rigor does not require a long answer, and exhausted evidence does not remove uncertainty.

Read [routing.md](references/routing.md) only for ambiguous depth choices, [lite.md](references/lite.md) for an explicitly requested Lite workflow, and [evidence.md](references/evidence.md) when conflicting or incomplete evidence affects the decision. Do not load all references by default.

## Deliver the outcome

Anchor completion to the requested deliverable. Advice is complete with a usable recommendation, its decisive basis, and any unresolved choice. Implementation is complete when the authorized artifact works against the relevant acceptance criteria, or a concrete blocker is demonstrated. Review alone does not authorize implementation.

Within authorized scope, resolve routine choices and continue through implementation and relevant verification without a new approval at each phase. Ask only for missing information or authority that materially prevents safe progress; prepare the concrete reviewable result first where possible. This skill grants no additional permissions and does not replace host controls.

Keep the result human-sized: lead with the answer or artifact, explain what makes it preferable, and expose uncertainty or a switch condition when it could change the user's action. Do not manufacture alternatives, mandatory headings, or an internal reasoning transcript.

Stop when the requested outcome is met and remaining work would not materially improve it. Fix material defects within scope; do not impose a one-retry limit on recoverable work. For blocked access, unavailable evidence, or failures with no promising next step, report the precise limitation and what would resolve it.
