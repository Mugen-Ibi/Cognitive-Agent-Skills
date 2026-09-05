# Validation report: 2.0.0

Date: 2026-09-05

## Deterministic checks

| Check | Result |
|---|---|
| Repository validator (`python3 scripts/validate.py`) | Pass |
| OpenAI Skill Creator `quick_validate.py` | Pass |
| OpenAI Plugin Creator `validate_plugin.py` | Pass |
| Python compile check for repository validator | Pass |
| Git whitespace/error check (`git diff --check`) | Pass |

The repository validator checks the exact v2 manifest and UI metadata shape, semantic versioning, HTTPS metadata URLs, component paths, Skill frontmatter, references, Markdown links, unfinished placeholders, retired v1 layout, and evaluation schema.

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
- License selection remains unresolved and blocks clear external redistribution rights.
