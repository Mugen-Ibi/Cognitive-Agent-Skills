# High Precision protocol

Use for consequential, difficult-to-reverse, publication-grade, governance, safety, or audit-critical work.

High Precision means high reliability, not automatic verbosity. For an acute safety, legal, medical, or financial boundary, prioritize the direct safe action, missing facts, professional or emergency handoff, and uncertainty. Do not mechanically generate three reframes or multiple options when that would delay or obscure the safe response.

## Sequence

1. **Intent** — establish the real-world outcome, constraints, non-goals, success and failure criteria, acceptable risk, decision owner, and cost of error.
2. **Scope** — define system boundary, time horizon, stakeholders, disciplines, evidence threshold, and what may remain assumed.
3. **Discover** — rank hidden assumptions, omitted stakeholders, confounders, dependency chains, incentives, edge cases, and second-order effects by decision impact.
4. **De-anchored reframes** — when the framing is contestable, create substantially different formulations before choosing one; use at least three when the decision space genuinely supports them. Where possible, formulate them before seeing the leading recommendation or use separate criteria to reduce anchoring. For a fixed-scope audit, keep the scope fixed and construct competing failure hypotheses instead of artificial reframes. Identify what each formulation or failure hypothesis explains, ignores, supports, falsifies, and implies.
5. **Evidence map** — classify important claims as verified, supported but uncertain, inference, assumption, or unknown.
6. **Parallel exploration** — when real alternatives exist, develop multiple candidates without prematurely merging them. Compare goal attainment, evidence, feasibility, cost, reversibility, robustness, stakeholder effects, operational risk, and long-term consequences. For a fixed artifact, evaluate the artifact and materially different remediation paths without inventing candidate solutions.
7. **Adversarial review** — conduct a distinct critic pass against the leading candidates. Distinguish context, model, method, organizational, and external-reviewer independence. A fresh context using the same model is only context-isolated; do not call it broadly independent. When the user explicitly requires independence, establish which dimension is required and satisfy it. If the host cannot, return a provisional result or blocker rather than claiming the deliverable or decision is final. Test the strongest counterargument, worst plausible failure, incentive and dependency failures, boundary conditions, alternative causal models, metric gaming, and the implementation gap.
8. **Verification** — verify every claim whose status could change the recommendation. Reproduce calculations or execute tests when practical. Preserve uncertainty when verification is impossible.
9. **Synthesis** — recompute the recommendation after criticism and evidence; record what survived, changed, and was rejected.
10. **Compression** — reduce the result to a human-sized, traceable decision brief.
11. **Human decision** — reserve value judgments, risk acceptance, irreversible commitments, and consequential trade-offs for the user.
12. **Execution** — after authorization, implement against explicit acceptance criteria and document deviations.
13. **Final audit** — prefer a reviewer with the required independence dimension when available and justified. If no independence dimension was explicitly required, a context-isolated or fresh-pass audit is an acceptable fallback when named accurately. If the user required a specific independence dimension and it remains unavailable, the result stays provisional or blocked. Check goal satisfaction, factual support, consistency, untested assumptions, defects, contradicting evidence, and the value of another iteration. This audit fulfills the shared completion gate; do not run a duplicate audit.

Do not label an artifact final, publication-ready, or decision-ready while a decision-changing prerequisite remains unverified. For research, this commonly includes novelty and related-work review, operational definitions, ethics requirements, sampling feasibility, and an evidence-based power analysis. Provide a provisional design and the exact closure tests when those prerequisites are missing.

## Decision-ready gate

First classify every unresolved uncertainty:

- **Blocking prerequisite:** without resolving it, the requested deliverable could be unsafe, invalid, unusable, or falsely represented as final. Do not call the work decision-ready.
- **Decision-compatible uncertainty:** the user can make a reversible or conditional decision within the stated risk tolerance, with a contingency and switch condition. Keep it explicit and allow a conditional decision.
- **Irreducible action-forcing uncertainty:** the uncertainty cannot be reduced enough before a real deadline, yet inaction is itself a consequential choice. Bound what is known, compare options including delay or no action, define contingencies and monitoring, and present the residual risk for explicit human acceptance. The analysis may be decision-ready, but the risk is not resolved.

Apply the following conditions only where they are relevant to the deliverable. An acute safety response can be complete when it establishes the safe boundary and handoff; it does not need artificial alternatives. A fixed-scope audit uses failure hypotheses in place of competing framings.

The work is decision-ready only when:

1. decision-relevant framings or fixed-scope failure hypotheses were considered where applicable;
2. decision-changing claims are verified, decision-compatible, or explicitly bounded as irreducible action-forcing uncertainties for human acceptance;
3. the leading recommendation, artifact assessment, or safe response survived the applicable challenge;
4. real alternatives were compared on consistent criteria when alternatives exist;
5. remaining uncertainty and human choices are visible;
6. every explicitly required independence dimension was satisfied, or the result remains provisional or blocked;
7. further analysis is unlikely to change the decision enough to justify its cost.

## Default decision brief

- Recommendation
- Confidence and reason
- Decisive evidence
- Strongest alternative
- Strongest objection
- Largest unresolved uncertainty
- Switch condition
- Human decision required
- Next action

Do not turn rigor into needless volume. Keep the evidence trail expandable.
