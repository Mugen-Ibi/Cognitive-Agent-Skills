# Architecture decision record: v2

Status: Accepted
Date: 2026-09-05

## Decision

Implement the cognitive system as one adaptive Skill and distribute it as a skills-only Plugin.

The Plugin is not a competing cognitive implementation. It is the installable package around the Skill:

```text
Plugin package
└── cognitive-router Skill
    ├── routing entrypoint
    ├── Lite protocol reference
    ├── Standard protocol reference
    ├── High Precision protocol reference
    └── conditional evidence reference
```

## Verified platform constraints

OpenAI's current documentation distinguishes the two layers:

- A Skill packages instructions and supporting resources for a repeatable workflow.
- A Plugin is an installable bundle that can include Skills, connectors, or both.
- Standalone Skills are available in the ChatGPT desktop app, Codex CLI, and the IDE extension.
- Skills bundled in Plugins are available in Chat and Work across supported ChatGPT web, desktop, and mobile surfaces, and in supported Codex surfaces.
- Plugins are not available in the Codex IDE extension, so the bundled Skill remains independently installable there.
- Skills use progressive disclosure: name and description are discovered first, `SKILL.md` is loaded after selection, and supporting references are loaded only when needed.

Sources:

- [Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Plugins](https://learn.chatgpt.com/docs/plugins)
- [Package your plugin](https://developers.openai.com/plugins/build/plugins)

These are current product behaviors, not permanent compatibility promises. Recheck them before a public release.

## Alternatives considered

| Design | Cross-surface reach | Trigger clarity | Context efficiency | Portability | Verdict |
|---|---:|---:|---:|---:|---|
| Four standalone Skills | Low | Low | Low | High | Reject as primary distribution |
| Four Skills bundled in one Plugin | High | Medium | Medium | High | Viable compatibility design |
| One monolithic Skill in one Plugin | High | High | Medium | High | Reject: all modes load together |
| One adaptive Skill with references in one Plugin | High | High | High | High | Selected |

### Why not retain four active Skills

The v1 router attempted to transfer execution to sibling Skills and duplicated a fallback summary. This creates four problems:

1. sibling invocation is not a portable Skill primitive across hosts;
2. four overlapping descriptions compete for implicit activation;
3. every installed Skill adds discovery metadata before the relevant instructions are loaded;
4. the router and child Skills can drift semantically.

The v2 design has one discovery surface and one routing authority. Mode details remain separate references, so selecting Lite does not require loading High Precision instructions.

### Why not use an MCP server

The protocol changes reasoning and workflow, not access to an external system. An MCP server would add hosting, authentication, privacy, availability, and review obligations without providing a necessary capability. The Skill can use whatever first-party or installed tools the host already exposes.

Add MCP only if a future version requires a deterministic shared service, persistent external state, or a tool that cannot be expressed safely as instructions or a local script.

## Runtime flow

1. The host matches the `cognitive-router` name and description, or the user invokes it explicitly.
2. The entrypoint reads `routing.md` and selects the minimum sufficient mode.
3. It reads exactly one mode reference initially.
4. It loads `evidence.md` only when external verification can change the result.
5. It performs the selected protocol, adapting the mode if new risk or uncertainty appears.
6. It returns a compressed, audit-relevant result and preserves consequential human decisions.

## Boundaries

- The router controls analytical depth, not model selection or product billing.
- It does not grant permissions, bypass host policies, or authorize external actions.
- It does not require the user to inspect internal reasoning.
- It does not promise factual accuracy without suitable evidence.
- It avoids fixed output templates when a direct answer is sufficient.

## Versioning

The move from four independently invocable Skills to one adaptive Skill is a breaking change and therefore begins at `2.0.0`.

- Patch: wording and validation fixes with unchanged routing behavior.
- Minor: backward-compatible modes, references, or evaluation coverage.
- Major: changes to invocation, routing semantics, or output contracts.

## Deferred decisions

- License selection remains with the repository owner.
- Public Plugin Directory submission is not performed by repository changes alone.
- Visual identity assets are optional and intentionally omitted until a stable brand is chosen.
