# Cognitive Agent Skills

A small Human–AI cognitive protocol suite designed to reduce the user's problem-framing and evaluation bottlenecks.

The suite lets an AI explore beyond the user's initial framing, challenge its own proposals, verify decision-changing claims, and compress the result into a human-sized decision brief. Use the router as the default entry point, or invoke a specific protocol when the appropriate depth is already known.

## Skills

| Skill | Purpose |
|---|---|
| `cognitive-router` | Selects the appropriate protocol and dynamically escalates or downgrades rigor. |
| `cognitive-lite` | Fast protocol for low-stakes, reversible tasks. |
| `cognitive-standard` | Default protocol for substantive multi-step analysis and decisions. |
| `cognitive-high-precision` | Rigorous, auditable protocol for high-consequence or publication-grade work. |

## Installation

Clone the repository:

```bash
git clone https://github.com/Mugen-Ibi/Cognitive-Agent-Skills.git
```

Install the skill directories using the mechanism supported by your AI or agent runtime. For a Codex-compatible local installation, copy the directories under `skills/` into your configured skills directory while preserving each directory name and its `SKILL.md` file.

```text
<skills-directory>/
├── cognitive-router/
│   └── SKILL.md
├── cognitive-lite/
│   └── SKILL.md
├── cognitive-standard/
│   └── SKILL.md
└── cognitive-high-precision/
    └── SKILL.md
```

Install all four skills when you want automatic routing. Installing a child skill by itself is also valid when you intend to invoke that protocol directly.

Runtime support for one skill invoking another varies. The router therefore uses a dual strategy: it dispatches to an installed sibling skill when invocation is available, and otherwise applies the selected protocol's documented semantics itself.

## Usage

Use `cognitive-router` when you want the system to choose the appropriate depth:

```text
Use cognitive-router to evaluate this migration plan and recommend the safest approach.
```

Invoke a child protocol directly when the desired level of rigor is known:

```text
Use cognitive-lite to help me choose between these two reversible options.
```

```text
Use cognitive-standard to compare these architecture alternatives.
```

```text
Use cognitive-high-precision to review this publication-bound methodology.
```

The protocols normally expose conclusions, evidence, assumptions, trade-offs, and next actions—not a verbose trace of internal reasoning.

## Examples

### Quick reversible decision

```text
Use cognitive-router to choose a naming convention for this small internal script.
```

Expected route: `cognitive-lite`, because the consequence and cost of correction are low.

### Multi-constraint project decision

```text
Use cognitive-router to compare three authentication architectures for our product.
```

Expected route: `cognitive-standard`, because constraints, trade-offs, implementation impact, and verification all matter.

### Publication-grade evaluation

```text
Use cognitive-router to audit the methodology and evidence for this paper before submission.
```

Expected route: `cognitive-high-precision`, because reproducibility, primary evidence, adversarial review, and auditability are required.

## Routing examples

| Task | Typical route | Why |
|---|---|---|
| Brainstorm possible workshop titles | Lite | Low consequence and easy to revise |
| Select a research question | Standard | Competing framings and meaningful trade-offs |
| Finalize a publishable experimental method | High Precision | High evidence and reproducibility requirements |
| Sketch a disposable prototype | Lite or Standard | Complexity may be high, but reversibility limits the required rigor |
| Answer a simple safety-critical question | High Precision | A single high-consequence factor overrides low complexity |

Routing is dynamic. A task can escalate when contradictory evidence, hidden dependencies, or a higher cost of error appears. It can downgrade when the problem becomes bounded or additional analysis no longer has positive expected value. Mixed-mode requests may use different protocols for different components.

## Protocol selection

Use `cognitive-router` as the default entry point when the appropriate depth is not known in advance.

The router evaluates consequence, reversibility, complexity, uncertainty, evidence requirements, and explicit user preference. It can escalate or downgrade during execution as new information changes the expected value of additional rigor.

## Design philosophy

- **Appropriate rigor, not maximum rigor.** The system optimizes expected decision quality against cognitive, compute, and time cost.
- **The initial framing is a hypothesis.** The protocols look for hidden assumptions, alternative formulations, and decision-changing omissions.
- **Challenge before commitment.** Serious proposals are tested against counterexamples, failure modes, and competing causal explanations.
- **Verify what could change the decision.** Evidence effort is proportional to consequence, uncertainty, and reversibility.
- **Compress for human judgment.** Broad exploration is reduced to a concise, traceable decision brief.
- **Keep consequential choices human-owned.** The user retains value judgments, risk acceptance, and irreversible commitments.
- **Escalate and downgrade dynamically.** Rigor changes as the true shape of the task becomes clearer.

## Architecture

```text
User Intent
    |
    v
Cognitive Router
    |
    +--> Cognitive Lite
    |
    +--> Cognitive Standard
    |
    `--> Cognitive High Precision
             |
             +-- dynamic downgrade/escalation
```

When sibling skill invocation is supported, the router transfers execution to the selected child skill. When it is unavailable, the router executes the same protocol semantics directly as a fallback.

## Repository structure

```text
Cognitive-Agent-Skills/
├── README.md
└── skills/
    ├── cognitive-router/
    │   └── SKILL.md
    ├── cognitive-lite/
    │   └── SKILL.md
    ├── cognitive-standard/
    │   └── SKILL.md
    └── cognitive-high-precision/
        └── SKILL.md
```

Each skill is self-contained in its own directory. `cognitive-router` is the recommended entry point when the necessary depth is unknown.

## Versioning

The project intends to use Semantic Versioning once releases begin:

- **Patch** releases clarify wording or fix formatting without changing protocol behavior.
- **Minor** releases add backward-compatible guidance, routing criteria, or optional capabilities.
- **Major** releases change protocol semantics, output contracts, or routing behavior in ways that may affect existing usage.

Until the first tagged release, the `main` branch should be treated as pre-release and may evolve.

## License note

No license has been selected yet. Copyright remains with the repository owner, and the absence of a license does not grant permission to copy, modify, or redistribute the contents. Add an explicit license before encouraging external reuse or accepting contributions that depend on defined reuse terms.
