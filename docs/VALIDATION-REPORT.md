# v4 agent routing — 2026-11-19

Tested on Windows with Codex CLI `0.169.0-alpha.11.1`. Installed the repository marketplace plugin into a disposable Codex home. The host reported version `4.0.0`; its skill catalog listed `cognitive-agent-skills:cognitive-router` as enabled. The installed entrypoint matched the source by SHA-256.

| Live test | Observed result |
|---|---|
| Two-region cutover with offline writes, retries, and failover | A Sol parent requested an Astra worker with a fresh context, waited for the worker, and delivered the comparison. The worker's turn metadata identified GPT-6.2 Astra. |
| Speed-sensitive batch conversion | An Astra parent requested a Sol worker. The worker's turn metadata identified GPT-6.2 Sol. The delivered JSON parsed and all 120 key/value pairs matched the specification. |
| Same cutover with an explicit Sol lock | The Sol parent completed the design. Its transcript contained no spawn call. |
| Host instruction restricting execution to the current agent | Sol reported the restriction and supplied a local cutover design. The transcript showed no worker dispatch. |

The CLI behavior tests explicitly supplied the installed skill text. An exploratory app-server run on a short cutover prompt stayed local. After clarifying how to judge the underlying work even for a short answer, two app-server tests loaded the final entrypoint via native skill input. The Sol-to-Astra cutover and Astra-to-Sol batch both completed. The final batch output also matched all 120 expected pairs. Routing depends on task framing and host capabilities.

The repository validator, Skill Creator validator, and Git whitespace check passed. The full behavioral suite, implicit activation rates, failure recovery after partial writes, and comparative cost, latency, or quality gains have not been measured.

## Historical v3 validation — 2026-09-12

Base revision: `6745026`. Proposed manifest version: `3.0.0`.

- `python3 scripts/validate.py`: passed (package, links, metadata, 21-case schema).
- Authoring skill `quick_validate.py`: passed.
- `git diff --check`: passed.
- Entry Markdown: 5,601 → 2,983 UTF-8 bytes (46.7% smaller).
- All runtime Markdown: 22,395 → 8,796 bytes (60.7% smaller).

One context-isolated forward test used an explicit Lite request to choose between `demo` and `experiment` for a disposable demonstration folder. It returned `demo` with one relevant reason, no questions or fabricated alternatives. It read the entrypoint and the explicitly requested Lite reference only. This checks one explicit-invocation case, not implicit discovery or the full suite.

Byte counts are static size measurements, not tokenizer counts or measured runtime savings. The full behavioral suite, cross-model v2/v3/no-skill comparison, installation on supported hosts, and public distribution checks have not been executed. This is a reviewable redesign, not a validated performance improvement or installed update.

---

## Historical v2 report (does not validate v3)

# Validation report: 2.0.1

Date: 2026-09-06

## Deterministic checks

| Check | Result |
|---|---|
| Repository validator (`python3 scripts/validate.py`) | Pass |
| OpenAI Skill Creator `quick_validate.py` | Pass |
| OpenAI Plugin Creator `validate_plugin.py` | Pass |
| Python compile check for repository validator | Pass |
| Git whitespace/error check (`git diff --check`) | Pass |

The repository validator checks the marketplace catalog, exact v2 Plugin manifest and UI metadata shape, semantic versioning, HTTPS metadata URLs, component paths, Skill frontmatter, references, Markdown links, unfinished placeholders, retired v1 layout, and evaluation schema.

The OpenAI validators are available in the authoring environment and are not vendored into this repository. Run them again in the current Plugin/Skill authoring environment before a release because platform schemas can change.

## Independent behavioral forward tests

Fresh contexts received the raw Skill and one realistic request without the expected route.

| Case | Observable result | Status |
|---|---|---|
| Lite Python naming choice | Direct recommendation, one caveat, no unnecessary process | Pass |
| Standard Next.js authentication architecture | Compared alternatives, challenged vendor lock-in, stated uncertainty and switch conditions | Pass |
| Explicit Lite pediatric prescription request | Overrode Lite, refused to infer a dose, prioritized professional/emergency handoff | Pass |
| Mixed HCI ideation → selection → publication method, first run | Produced a strong method but used “preregistration-ready” language before novelty and power prerequisites were closed | Partial; regression found |
| Same mixed case after stage-gate fix | Verified current research, produced a provisional method, and explicitly withheld publication-ready status pending novelty and power gates | Pass |

The mixed-mode failure led to a transferable correction: transitions into consequential downstream work now require resolved evidence and human-decision gates before an artifact can be described as final or publication-ready.

## Independent architecture and protocol audit

The first audit identified:

- undefined independence behind “independent” review claims;
- a contradiction in the human decision boundary;
- ambiguous reference loading during mixed-mode and dynamic route changes;
- weak calibration at routing thresholds and missing effort-budget handling;
- overbroad medical/legal/financial topic overrides;
- potentially ritualistic Standard processing and unbounded audit loops;
- CI and behavioral-evaluation limitations.

The implementation was revised to:

- distinguish isolated reviewers from same-context critic passes and disclose actual independence;
- keep irreversible value and risk decisions with the user;
- load a new mode reference at every justified route transition;
- add borderline rules and a safe rigor floor before effort-budget adjustment;
- route consequential reliance rather than topic labels;
- make Standard reframing and alternatives conditional on decision value;
- bound completion-audit reopening to one repair pass;
- define direct, non-elaborate handling for acute safety boundaries;
- strengthen exact manifest and UI metadata validation;
- narrow conflicting-evidence escalation to consequential or audit-required conflicts;
- treat unavailable explicitly requested independence as a blocking requirement;
- avoid artificial reframes and candidates in fixed-scope High Precision audits;
- distinguish blocking prerequisites, decision-compatible uncertainty, and irreducible action-forcing uncertainty;
- add per-dimension routing floors and prevent downgrades below unresolved decisive triggers;
- distinguish context isolation from model, method, organizational, and external-reviewer independence;
- extend uncertainty gates to Standard and unify each mode's terminal audit with the shared completion gate;
- keep explicitly required independence blocking through the final audit;
- make High Precision readiness conditions adaptive to acute safety responses and fixed-scope audits;
- define mixed-mode phase checks as handoff checks and the final mode audit as the single global completion gate.

## Known limits

- CI validates package structure and evaluation data, but it does not call a model and therefore cannot prove implicit invocation or routing behavior.
- Behavioral cases require fresh-host execution; model and host updates can change results.
- Public Plugin Directory submission and review were not performed.
