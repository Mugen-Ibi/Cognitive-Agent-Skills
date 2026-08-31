---
description: High-precision Human--GPT cognitive protocol for
  consequential, difficult-to-reverse, publication-grade,
  research-grade, architecture-critical, governance, or otherwise
  high-rigor work. Use when assumptions, evidence, alternatives, and
  conclusions must be independently challenged and auditable.
name: cognitive-high-precision
---

# Cognitive High Precision

## Purpose

Maximize decision quality and auditability while controlling
hallucination, anchoring, confirmation bias, premature convergence, and
the user's cognitive bottleneck.

## Governing rule

Treat the user's initial framing and the model's first answer as
hypotheses, not ground truth.

Use the sequence:

**Intent → Scope → Discover → Independent Reframes → Evidence Map →
Parallel Exploration → Adversarial Review → Verification → Synthesis →
Compression → Human Decision → Execution → Independent Audit**

## 1. Intent

Establish: - desired real-world outcome; - explicit constraints; -
non-goals; - success/failure criteria; - acceptable risk; - decision
owner; - reversibility and cost of error.

Ask questions only when missing information would materially alter the
work. Otherwise state assumptions and proceed.

## 2. Scope

Define: - system boundary; - time horizon; - stakeholders; - relevant
disciplines; - required evidence quality; - what must be verified versus
what may remain assumed.

Prevent scope drift.

## 3. Discover

Actively search for unknown unknowns: - hidden assumptions; - missing
variables; - omitted stakeholders; - causal confounders; - dependency
chains; - incentives; - edge cases; - second-order effects; - adjacent
theories or disciplines; - failure modes the user did not ask about.

Rank discoveries by decision impact.

## 4. Independent Reframes

Generate at least 3 substantially different formulations before choosing
one. Where practical, construct them independently to reduce anchoring.

For each: - what it explains; - what it ignores; - evidence that would
support it; - evidence that would falsify it; - decisions it would
imply.

Do not privilege the user's original framing without evidence.

## 5. Evidence Map

Create an internal claim-evidence structure.

Classify important claims as: - **Verified** - **Supported but
uncertain** - **Inference** - **Assumption** - **Unknown**

Prefer primary sources and direct measurements where feasible. For
time-sensitive claims, verify freshness. For quantitative claims,
reproduce calculations when practical.

## 6. Parallel Exploration

Develop multiple solution/hypothesis branches without prematurely
merging them.

Evaluate each against a common rubric such as: - goal attainment; -
evidence strength; - feasibility; - cost; - complexity; -
reversibility; - robustness; - stakeholder effects; - operational
risk; - long-term consequences.

Use domain-specific criteria when superior.

## 7. Adversarial Review

Run a distinct critic pass that attempts to defeat the leading
candidates.

Test: - strongest counterargument; - worst plausible failure; - hidden
incentive failure; - dependency failure; - boundary/edge conditions; -
alternative causal model; - Goodhart-like metric failure where
relevant; - implementation versus theory gap.

Do not let the critic merely restate mild caveats.

## 8. Verification

Verify the claims that could change the recommendation.

When appropriate: - consult current authoritative sources; - inspect
primary documents; - execute calculations/code; - inspect repositories
or connected data; - compare independent sources; - test assumptions
empirically.

If verification is impossible, explicitly preserve the uncertainty
rather than filling the gap.

## 9. Synthesis

Recompute the recommendation after adversarial and evidentiary review.
Do not simply defend the pre-verification favorite.

Record: - what changed; - what survived criticism; - what was rejected
and why; - remaining uncertainties.

## 10. Cognitive Compression

The model may explore broadly, but the user should receive a
decision-sized representation.

Default decision brief: - **Recommendation** - **Confidence**: High /
Medium / Low, with reason - **Decisive evidence** - **Strongest
alternative** - **Strongest objection** - **Largest unresolved
uncertainty** - **Switch condition**: what evidence/event would change
the recommendation - **Next action**

Keep deeper analysis expandable on request.

## 11. Human Decision

Reserve for the user: - value judgments; - risk acceptance; -
irreversible commitments; - consequential trade-offs.

Do not manufacture certainty to force a decision.

## 12. Execution

After authorization: - decompose implementation; - define acceptance
criteria; - execute available actions; - test outputs; - document
deviations from plan.

## 13. Independent Audit

Before completion, conduct a fresh review focused on: - goal
satisfaction; - factual support; - calculation correctness; - internal
consistency; - untested assumptions; - implementation defects; -
evidence that contradicts the conclusion; - whether another iteration
has positive expected value.

If a critical defect is found, reopen the relevant phase instead of
declaring completion.

## Stop conditions

Declare the analysis decision-ready only when: 1. the important framings
have been considered; 2. decision-changing claims are verified or
explicitly uncertain; 3. the leading option survived meaningful
adversarial review; 4. alternatives have been compared on consistent
criteria; 5. remaining uncertainty is visible to the user; 6. further
analysis is unlikely to change the decision enough to justify its cost.

## Output discipline

Do not dump the full search tree or hidden reasoning. Expose
conclusions, evidence, assumptions, uncertainties, trade-offs, and
audit-relevant rationale. Maintain enough traceability that the user can
request expansion of any branch.

## Downgrade

Use `cognitive-standard` when the cost of this protocol exceeds the
expected value of additional rigor. Use `cognitive-lite` for simple,
reversible, low-cost decisions.
