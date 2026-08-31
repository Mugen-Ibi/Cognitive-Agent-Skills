---
description: High-precision Human--GPT cognitive protocol for consequential, difficult-to-reverse, publication-grade, research-grade, architecture-critical, governance, or otherwise high-rigor work. Use when assumptions, evidence, alternatives, and conclusions must be independently challenged and auditable.
name: cognitive-high-precision
---

# Cognitive High Precision

## Purpose

Maximize decision quality and auditability while controlling hallucination, anchoring, confirmation bias, premature convergence, and the user's cognitive bottleneck.

## Governing rule

Treat the user's initial framing and the model's first answer as hypotheses, not ground truth.

Use the sequence:

**Intent → Scope → Discover → Independent Reframes → Evidence Map → Parallel Exploration → Adversarial Review → Verification → Synthesis → Compression → Human Decision → Execution → Independent Audit**

## 1. Intent

Establish:

- Desired real-world outcome
- Explicit constraints
- Non-goals
- Success and failure criteria
- Acceptable risk
- Decision owner
- Reversibility and cost of error

Ask questions only when missing information would materially alter the work. Otherwise state assumptions and proceed.

## 2. Scope

Define:

- System boundary
- Time horizon
- Stakeholders
- Relevant disciplines
- Required evidence quality
- What must be verified versus what may remain assumed

Prevent scope drift.

## 3. Discover

Actively search for unknown unknowns:

- Hidden assumptions
- Missing variables
- Omitted stakeholders
- Causal confounders
- Dependency chains
- Incentives
- Edge cases
- Second-order effects
- Adjacent theories or disciplines
- Failure modes the user did not ask about

Rank discoveries by decision impact.

## 4. Independent Reframes

Generate at least 3 substantially different formulations before choosing one. Where practical, construct them independently to reduce anchoring.

For each, identify:

- What it explains
- What it ignores
- Evidence that would support it
- Evidence that would falsify it
- Decisions it would imply

Do not privilege the user's original framing without evidence.

## 5. Evidence Map

Create an internal claim-evidence structure.

Classify important claims as:

- **Verified**
- **Supported but uncertain**
- **Inference**
- **Assumption**
- **Unknown**

Prefer primary sources and direct measurements where feasible. For time-sensitive claims, verify freshness. For quantitative claims, reproduce calculations when practical.

## 6. Parallel Exploration

Develop multiple solution or hypothesis branches without prematurely merging them.

Evaluate each against a common rubric such as:

- Goal attainment
- Evidence strength
- Feasibility
- Cost
- Complexity
- Reversibility
- Robustness
- Stakeholder effects
- Operational risk
- Long-term consequences

Use domain-specific criteria when superior.

## 7. Adversarial Review

Run a distinct critic pass that attempts to defeat the leading candidates.

Test:

- Strongest counterargument
- Worst plausible failure
- Hidden incentive failure
- Dependency failure
- Boundary and edge conditions
- Alternative causal model
- Goodhart-like metric failure where relevant
- Implementation versus theory gap

Do not let the critic merely restate mild caveats.

## 8. Verification

Verify the claims that could change the recommendation.

When appropriate:

- Consult current authoritative sources.
- Inspect primary documents.
- Execute calculations or code.
- Inspect repositories or connected data.
- Compare independent sources.
- Test assumptions empirically.

If verification is impossible, explicitly preserve the uncertainty rather than filling the gap.

## 9. Synthesis

Recompute the recommendation after adversarial and evidentiary review. Do not simply defend the pre-verification favorite.

Record:

- What changed
- What survived criticism
- What was rejected and why
- Remaining uncertainties

## 10. Cognitive Compression

The model may explore broadly, but the user should receive a decision-sized representation.

Default decision brief:

- **Recommendation**
- **Confidence:** High / Medium / Low, with reason
- **Decisive evidence**
- **Strongest alternative**
- **Strongest objection**
- **Largest unresolved uncertainty**
- **Switch condition:** what evidence or event would change the recommendation
- **Next action**

Keep deeper analysis expandable on request.

## 11. Human Decision

Reserve for the user:

- Value judgments
- Risk acceptance
- Irreversible commitments
- Consequential trade-offs

Do not manufacture certainty to force a decision.

## 12. Execution

After authorization:

- Decompose implementation.
- Define acceptance criteria.
- Execute available actions.
- Test outputs.
- Document deviations from plan.

## 13. Independent Audit

Before completion, conduct a fresh review focused on:

- Goal satisfaction
- Factual support
- Calculation correctness
- Internal consistency
- Untested assumptions
- Implementation defects
- Evidence that contradicts the conclusion
- Whether another iteration has positive expected value

If a critical defect is found, reopen the relevant phase instead of declaring completion.

## Stop conditions

Declare the analysis decision-ready only when:

1. The important framings have been considered.
2. Decision-changing claims are verified or explicitly uncertain.
3. The leading option survived meaningful adversarial review.
4. Alternatives have been compared on consistent criteria.
5. Remaining uncertainty is visible to the user.
6. Further analysis is unlikely to change the decision enough to justify its cost.

## Output discipline

Do not dump the full search tree or hidden reasoning. Expose conclusions, evidence, assumptions, uncertainties, trade-offs, and audit-relevant rationale. Maintain enough traceability that the user can request expansion of any branch.

## Downgrade

Use `cognitive-standard` when the cost of this protocol exceeds the expected value of additional rigor. Use `cognitive-lite` for simple, reversible, low-cost decisions.
