# Cognitive Agent Skills

[日本語](README.ja.md)

Decision support for competing options and uncertain problem framing. One `cognitive-router` skill helps produce actionable recommendations and complete authorized work while keeping the user's decision burden small.

Version 3 replaces fixed cognitive sequences with outcome contracts. It preserves Lite, Standard, and High Precision as effort preferences, without changing the host model or permissions.

| Depth | Intended use |
|---|---|
| Lite | Disposable or easily corrected choices; normally no reference reads |
| Standard | Interacting constraints and meaningful trade-offs |
| High Precision | Consequential reliance, costly reversal, or required auditability |

Routine execution and explanation do not need implicit activation. Explicit invocation remains available:

```text
Use Cognitive Router to compare these approaches and recommend one.
Use Cognitive Router in High Precision mode to audit this methodology.
Implement the accepted approach within the agreed scope and verify the result.
```

## Package

- `.agents/plugins/marketplace.json`: repository marketplace.
- `plugins/cognitive-agent-skills/.codex-plugin/plugin.json`: plugin manifest.
- `plugins/cognitive-agent-skills/skills/cognitive-router/`: independently packaged skill with conditional references and UI metadata.
- `evals/cases.json`: behavioral scenarios, not automated model results.
- `scripts/validate.py`: deterministic package validation.

The existing marketplace installation target is `Mugen-Ibi/Cognitive-Agent-Skills`; the standalone skill path is shown above. Installation UI and host support must be checked against current platform documentation. Repository changes do not automatically update installed copies.

## Development

```bash
python3 scripts/validate.py
```

This checks package consistency, not decision quality. See [Architecture](docs/ARCHITECTURE.md), [Evaluation](docs/EVALUATION.md), [Migration](docs/MIGRATION.md), and [Validation report](docs/VALIDATION-REPORT.md).

Manifest version: `3.0.0`. License: [Apache-2.0](LICENSE).
