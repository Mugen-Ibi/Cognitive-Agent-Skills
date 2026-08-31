# Cognitive Agent Skills

A small Human–AI cognitive protocol suite designed to reduce the user's problem-framing and evaluation bottlenecks.

## Skills

| Skill | Purpose |
|---|---|
| `cognitive-router` | Automatically selects and dynamically escalates/downgrades protocol depth. |
| `cognitive-lite` | Fast protocol for low-stakes, reversible tasks. |
| `cognitive-standard` | Default protocol for substantive multi-step analysis and decisions. |
| `cognitive-high-precision` | Rigorous, auditable protocol for high-consequence or publication-grade work. |

## Architecture

```text
User Intent
    |
    v
Cognitive Router
    |
    +--> Lite
    |
    +--> Standard
    |
    `--> High Precision
             |
             +-- dynamic downgrade/escalation
```

The core design principle is to let the AI explore beyond the user's initial framing, challenge its own proposals, verify decision-changing claims, and compress the result back into a human-sized decision brief.

## Suggested repository layout

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

## Protocol selection

Use `cognitive-router` as the default entry point when the appropriate depth is not known in advance.

The router evaluates consequence, reversibility, complexity, uncertainty, evidence requirements, and explicit user preference. It can escalate or downgrade during execution as new information changes the expected value of additional rigor.

## License

No license has been selected yet. Add one before encouraging external reuse.
