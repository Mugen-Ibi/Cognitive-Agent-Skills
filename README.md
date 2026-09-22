# Cognitive Agent Skills

[日本語](README.ja.md)

Cognitive Agent Skills adds a `cognitive-router` skill that turns uncertain problems and competing options into actionable recommendations. It adjusts the depth of analysis to the consequences of the task and can continue through implementation when the user authorizes it.

Use it for decisions, research planning, architecture, reviews, and other work where the framing or trade-offs are not yet clear. Routine questions and straightforward edits do not need it.

## Installation

### Plugin marketplace (recommended)

Use this method in a host that supports Plugin marketplaces.

1. Open the host's Plugin manager and choose the option to add a marketplace.
2. Enter the repository source:

   ```text
   Mugen-Ibi/Cognitive-Agent-Skills
   ```

3. Install **Cognitive Agent Skills** from the added marketplace.
4. Start a new conversation so the installed skill is available.

The exact menu names may differ between hosts and product versions.

### Standalone skill

If your host supports Agent Skills but not Plugin marketplaces:

1. Clone or download this repository.
2. Copy the following directory into the Skills directory used by your host:

   ```text
   plugins/cognitive-agent-skills/skills/cognitive-router
   ```

3. Restart or reload the host, then start a new conversation.

Consult your host's documentation for the location of its Skills directory. Compatibility with a specific host should be verified in that host; the repository validator only checks this package's structure.

## Usage

The skill may be selected automatically when a request involves uncertain framing, meaningful trade-offs, or consequential decisions. You can also invoke it explicitly:

```text
Use Cognitive Router to compare these approaches and recommend one.
Use Cognitive Router in Standard mode to review this architecture.
Use Cognitive Router in High Precision mode to audit this methodology.
```

The skill does not change the selected model, reasoning-effort setting, available tools, or permissions.

## Analysis depth

| Depth | Use when |
|---|---|
| Lite | The decision is easy to reverse and a quick recommendation is enough |
| Standard | Several constraints or meaningful trade-offs interact |
| High Precision | The result will support consequential, difficult-to-reverse, or auditable work |

The router normally chooses the smallest sufficient depth. An explicit depth request takes precedence when appropriate for the task.

## Updating

Repository changes do not automatically update an installed copy. Use the host's Plugin update function, or replace the standalone `cognitive-router` directory with the version from the latest release.

After updating, start a new conversation before checking the behavior.

## Development

Run the package validator from the repository root:

```bash
python3 scripts/validate.py
```

This checks package consistency, not the quality of model decisions. See [Architecture](docs/ARCHITECTURE.md), [Evaluation](docs/EVALUATION.md), and the [Validation report](docs/VALIDATION-REPORT.md) for maintainer documentation.

Licensed under [Apache-2.0](LICENSE).
