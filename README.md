# Cognitive Agent Skills

[日本語](README.ja.md)

`cognitive-router` automatically selects an agent to carry out the task. The model you selected is the starting point. When another available agent has a material advantage, the router sends it the work, checks the result, and returns it in the same conversation.

For example, a complex cross-service migration may go from GPT-6.2 Sol to Astra. A large batch of straightforward edits with a tight deadline may go from Astra to Sol. For a one-line fix, staying in the current context usually takes less time. These are routing preferences based on the host's model descriptions. Actual availability, tools, context-transfer cost, and your constraints determine the choice.

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

The host can select the skill for complex or specialist work and decision support. Invoke it explicitly to request routing on any task.

```text
Use Cognitive Router to design and verify a migration that tolerates replay and failover.
Use Cognitive Router for this batch of mechanical edits. Prioritize turnaround time.
Use only my selected model. Use Cognitive Router in High Precision mode to audit this proposal.
```

On Codex, the router can give one worker an explicit model and wait for its output. The main chat retains the model shown in the picker. If the host cannot dispatch to a better model, the current agent completes the work within its capabilities. An explicit model lock or a request to avoid delegation takes precedence. A request for advice about models only returns a recommendation.

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
