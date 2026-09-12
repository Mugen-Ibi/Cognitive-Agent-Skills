# Architecture: v3 outcome contracts

Status: proposed for merge; 2026-09-12.

## Basis

The [OpenAI article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) recommends precise discovery descriptions, conditional references, less prescribed process, and explicit completion boundaries. The choices below are this project's application of that guidance, not measured performance claims.

## Decision

Keep one `cognitive-router` skill distributed by the existing skills-only plugin and marketplace. Preserve its public name and reference paths. Change the runtime contract from mandatory protocol execution to decision support proportional to consequence and uncertainty.

| v2 constraint | v3 decision | Reason |
|---|---|---|
| Broad reviews/research/implementation trigger | Competing options, uncertain framing, explicit invocation | Avoid competing with ordinary execution skills |
| Always read routing and one mode | Inline depth guidance; conditional references | Direct choices need no extra reads |
| Five numerical dimensions and thresholds | Qualitative consequence and reliance | Avoid false precision and routing work |
| Six to thirteen ordered stages | Observable outcome and relevant criteria | Allow task-dependent order |
| Reframe and option counts | Material alternatives only | Avoid manufactured choices |
| Generic human decision phase | Existing scope and authority determine boundaries | Avoid renewed approval for authorized work |
| One defect-repair retry | Continue useful recoverable repairs within scope | Avoid premature stopping |
| Mode-matching as main evaluation | Completion, boundary, evidence, user burden | Evaluate utility rather than ceremony |

## Runtime and compatibility

Discovery selects the skill for decision support. The entrypoint can handle Lite directly; Standard, High Precision, ambiguous routing, and evidence references are conditional. Mixed tasks use local rigor without a mandatory transition state machine.

Lite, Standard, and High Precision remain accepted user vocabulary, not model selectors or API reasoning-effort controls. Host permissions remain authoritative. A review request does not authorize implementation; an authorized implementation request should continue through relevant verification.

No new MCP server, agent orchestrator, model-specific fork, personal-memory store, or always-loaded AGENTS.md is needed. This repository has no AGENTS.md to simplify. Do not add one merely to repeat the skill.

The manifest paths are retained. Product-surface and Claude Code installation compatibility are not established by this redesign; consult current platform documentation and perform installation checks before release. Installed copies do not update merely because this branch changes.

## Trade-offs and validation

Less prescription may cause weaker models to miss useful analysis. Compare v2, v3, and no-skill baselines on identical tasks before claiming improvement or adding model-specific guidance. The narrowed trigger may miss implicit requests; evaluate discovery separately from explicit invocation. Historical v2 reports do not validate v3.

Version 3.0.0 reflects changed routing and completion semantics despite stable paths. See [Evaluation](EVALUATION.md) and [Migration](MIGRATION.md).
