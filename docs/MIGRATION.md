# Migration to v3

The plugin and skill names, marketplace target, reference paths, and implicit-invocation policy remain unchanged. Update the installed package through the host's supported update mechanism after release; this branch does not update existing installations.

The behavior changes: ordinary explanation and execution no longer invite routing, numerical scores and mandatory stage sequences are removed, and prior authorization carries through relevant verification. Explicit Lite / Standard / High Precision requests still work. Integrations must not depend on a mode announcement, fixed output headings, or a routing score.

Use the behavioral comparison in [Evaluation](EVALUATION.md) before adopting v3 in consequential workflows. Roll back by installing the prior released package through the host; do not overwrite unrelated user settings.

---

## Historical v1 to v2 migration

# Migration from v1 to v2

Version 2 replaces four active Skills with one adaptive `cognitive-router` Skill packaged inside `cognitive-agent-skills`.

## Mapping

| v1 invocation | v2 invocation |
|---|---|
| `cognitive-router` | `cognitive-router` |
| `cognitive-lite` | `cognitive-router` with Lite mode |
| `cognitive-standard` | `cognitive-router` with Standard mode |
| `cognitive-high-precision` | `cognitive-router` with High Precision mode |

The cognitive semantics are preserved and refined, but the three mode names are no longer separately installed Skills.

## Why this is a major version

- Existing direct references to the three child Skill identifiers must change.
- The repository's install root moved from `skills/` to `plugins/cognitive-agent-skills/`.
- The Plugin manifest is now the distribution entrypoint for Chat and Work.
- Protocol details moved into progressively loaded references.

## Upgrade procedure

1. Remove or disable the four v1 Skill installations to prevent duplicate implicit triggers.
2. Install the v2 Plugin from `plugins/cognitive-agent-skills` on a supported Plugin surface.
3. For an IDE or standalone Codex setup, install only `plugins/cognitive-agent-skills/skills/cognitive-router` as a Skill.
4. Start a new conversation or session so the host discovers the new package.
5. Run one Lite, one Standard, and one High Precision smoke request from [Evaluation](EVALUATION.md).

## Prompt migration

Replace:

```text
Use cognitive-high-precision to review this methodology.
```

with:

```text
Use cognitive-router in High Precision mode to review this methodology.
```

Ordinary prompts that invoked `cognitive-router` require no change.

## Rollback

Version 1 remains available through Git history. If a host cannot load Plugin-bundled Skills, install the v2 `cognitive-router` directory as a standalone Skill before considering a rollback; it has no Plugin-only runtime dependency.
