# Cognitive Agent Skills

[日本語](README.ja.md)

An adaptive Human–AI reasoning system that matches analytical rigor to the cost of being wrong.

Version 2 packages one canonical `cognitive-router` skill as a skills-only plugin. The skill selects Lite, Standard, or High Precision, loads only the selected protocol, and returns a decision-sized result. This replaces the former four-skill dispatch design.

## Why the hybrid design

- **Skill is the implementation.** `SKILL.md` and its references define the cognitive workflow.
- **Plugin is the distribution boundary.** It makes the workflow installable across supported ChatGPT Chat, Work, and Codex surfaces.
- **One adaptive skill avoids collisions.** It removes sibling-skill dispatch assumptions and reduces implicit-trigger and metadata overhead.
- **The skill remains portable.** Codex CLI and IDE users can install the bundled `cognitive-router` directory as a standalone skill.

No MCP server is included. The workflow uses the host's available tools and evidence sources without adding an external service or authentication boundary.

## Modes

| Mode | Best for | Default behavior |
|---|---|---|
| Lite | reversible, low-cost questions and ideation | quick reframe and sanity check |
| Standard | multi-step work with meaningful trade-offs | explore, attack, verify, execute, audit |
| High Precision | consequential, hard-to-reverse, publication or governance work | evidence map, independent reframes, adversarial review, independent audit |

The router can use different modes for separable parts of one request and can escalate or downgrade as the true risk becomes clearer.

## Repository layout

```text
plugins/cognitive-agent-skills/
├── .codex-plugin/plugin.json
└── skills/cognitive-router/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
        ├── routing.md
        ├── lite.md
        ├── standard.md
        ├── high-precision.md
        └── evidence.md
docs/
├── ARCHITECTURE.md
├── EVALUATION.md
├── MIGRATION.md
├── RELEASE.md
├── REVIEW.md
└── VALIDATION-REPORT.md
evals/cases.json
scripts/validate.py
```

## Use

After installing the plugin, ask normally or invoke the bundled skill explicitly:

```text
Use Cognitive Router to evaluate this migration plan and recommend the right approach.
```

You can override the route when the needed rigor is already known:

```text
Use Cognitive Router in High Precision mode to audit this publication methodology.
```

The normal output contains conclusions, evidence, assumptions, trade-offs, uncertainty, and next actions—not hidden chain-of-thought.

## Install for local development

Clone the repository and use `plugins/cognitive-agent-skills` as the plugin root in a supported local marketplace or plugin development workflow.

For standalone Codex skill use, copy or link:

```text
plugins/cognitive-agent-skills/skills/cognitive-router
```

into a user- or repository-scoped skills directory. Standalone skills and plugin availability differ by product surface; see [Architecture](docs/ARCHITECTURE.md) and the current official OpenAI documentation before distribution.

## Validate

```bash
python3 scripts/validate.py
```

The validation checks the plugin manifest, skill frontmatter, UI metadata, internal links, protocol inventory, evaluation schema, and retired v1 layout. CI runs the same command.

Behavioral evaluation cases and the manual procedure are in [Evaluation](docs/EVALUATION.md).

The complete v1 findings and disposition are in [Full review](docs/REVIEW.md).

The exact checks, forward-test outcomes, corrections, and limitations are in the [Validation report](docs/VALIDATION-REPORT.md).

## Migration from v1

Version 2 is a breaking packaging and invocation change. The separate `cognitive-lite`, `cognitive-standard`, and `cognitive-high-precision` skills are now protocol references selected by `cognitive-router`. See [Migration](docs/MIGRATION.md).

## Project status and license

The plugin manifest is versioned as `2.0.0`. A license has not been selected; copyright remains with the repository owner. Choose and add a license before public redistribution or accepting contributions that depend on explicit reuse rights.
