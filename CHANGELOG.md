# Changelog

## 2.0.1 - 2026-09-06

- Add a repository marketplace manifest so `codex plugin marketplace add Mugen-Ibi/Cognitive-Agent-Skills` can discover the Plugin.
- Validate the marketplace entry and its link to the Plugin manifest in CI.
- Document executable repository and local installation steps.
- Align Plugin metadata and project documentation with the Apache-2.0 license.

## 2.0.0 - 2026-09-05

- Package the project as a skills-only Plugin for supported Chat, Work, and Codex surfaces.
- Consolidate four active Skills into one adaptive `cognitive-router` Skill.
- Move Lite, Standard, High Precision, routing, and evidence guidance into progressively loaded references.
- Remove sibling-Skill dispatch and duplicated fallback semantics.
- Add Skill UI metadata, deterministic package validation, behavioral evaluation cases, and CI.
- Add architecture, migration, and evaluation documentation in English; update English and Japanese READMEs.
- Add mixed-mode readiness gates, calibrated boundary routing, explicit dynamic reference loading, truthful review-independence labels, and bounded repair audits after independent testing.

## 1.x

- Initial standalone `cognitive-router`, `cognitive-lite`, `cognitive-standard`, and `cognitive-high-precision` Skills.
