# Full v1 review

[日本語](REVIEW.ja.md)

Review date: 2026-09-05
Scope: repository structure, Skill behavior, routing, cross-surface compatibility, distribution, validation, documentation, and maintenance.

## Executive finding

The core idea was sound: route work by consequence, reversibility, complexity, uncertainty, and evidence needs; challenge the initial frame; and compress the result for human judgment. The v1 implementation was a useful protocol prototype but not a complete cross-surface product package.

The decisive issue was architectural: Skills and Plugins were treated as alternatives. In the current platform model, Skills author workflows and Plugins distribute them. Version 2 therefore retains the cognitive protocol as a Skill and wraps it in a skills-only Plugin.

## Findings

| Severity | v1 finding | Consequence | v2 response |
|---|---|---|---|
| High | No Plugin manifest or installable package | The repository was not a Plugin and could not provide the intended Chat/Work distribution path | Added `.codex-plugin/plugin.json` in a valid Plugin root |
| High | Router depended on optional sibling-Skill dispatch | Behavior varied by host; failure required duplicated fallback behavior | Replaced dispatch with one Skill and local references |
| High | No deterministic validation or behavioral eval set | Structural or routing regressions could reach users unnoticed | Added validator, CI, cases, and pass criteria |
| Medium | Four overlapping Skill descriptions were active | Greater implicit-trigger competition and discovery metadata cost | Reduced the active surface to one Skill |
| Medium | Protocol semantics existed in multiple files and fallback summaries | Router and child protocols could drift | Established one entrypoint and one canonical reference per mode |
| Medium | No Skill UI metadata | Weaker discovery and invocation UX | Added `agents/openai.yaml` |
| Medium | Installation guidance assumed generic Skill support | It did not distinguish Chat/Work, Plugin, CLI, desktop, and IDE surfaces | Added a platform-aware architecture and migration guide |
| Medium | No declared breaking-change path | Consumers could not predict migration impact | Set Plugin version `2.0.0` and added a changelog |
| Open | No license selected | External reuse rights remain undefined | Preserved owner control; documented the decision as deferred |

## Strengths preserved

- Minimum sufficient rigor rather than maximum reasoning by default.
- Dynamic escalation and downgrade.
- The user's initial framing is treated as a hypothesis.
- Discovery, reframing, adversarial review, verification, and compression are delegated to the model.
- Values, risk acceptance, and irreversible commitments remain human-owned.
- High Precision preserves an auditable evidence distinction without exposing chain-of-thought.
- Mixed-mode transitions use readiness gates so early ideation cannot silently become an unverified final artifact.

## Protocol changes

### Router

- Uses decisive overrides before a numerical heuristic.
- Treats the score as guidance rather than a rigid classifier.
- Adds an explicit non-trigger boundary for simple execution with no meaningful judgment.
- Loads one mode initially and supports mixed-mode work only for separable components.

### Lite

- Remains deliberately small.
- Limits reframing and option generation to decision-relevant items.
- Escalates when verification or interacting constraints become central.

### Standard

- Preserves the v1 sequence of intent, discovery, reframing, exploration, attack, verification, compression, decision, execution, and audit.
- Makes the output contract flexible enough for direct answers while retaining a default decision brief.

### High Precision

- Preserves independent reframing, evidence mapping, parallel candidate exploration, adversarial review, synthesis, and independent audit.
- Adds a visible decision-ready gate and prevents rigor from becoming needless output volume.

### Evidence

- Separates evidence discipline into a conditional reference.
- Prioritizes direct inspection and primary sources.
- Stops verification when additional evidence has low expected decision value.

## Remaining uncertainties

- Implicit invocation quality is model- and host-dependent; repository validation cannot prove it.
- Public Plugin Directory acceptance requires the platform submission and review process, which is outside repository validation.
- Product availability can change; the cited official documentation must be checked again before release.
- The behavioral eval set is a baseline and should grow from real failures rather than speculative cases.

## Recommendation

Adopt v2 as the main architecture. Do not restore the three protocol modes as active sibling Skills unless a host demonstrates a concrete need for individually addressable Skill chips that outweighs trigger competition and semantic drift. If that need appears, implement thin explicit-only adapters in a future minor release rather than duplicating protocol bodies.
