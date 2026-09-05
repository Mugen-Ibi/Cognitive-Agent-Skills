---
name: cognitive-router
description: Select and run a Lite, Standard, or High Precision cognitive protocol for decisions, research, planning, reviews, and complex implementation. Use when the right analysis depth is unclear or when the user asks to reframe, compare, challenge, verify, audit, or reduce cognitive overload; do not use for simple execution with no meaningful judgment.
---

# Cognitive Router

Choose the lightest protocol that can reliably satisfy the request. Optimize decision quality minus cognitive, time, and compute cost.

## Operating contract

1. Establish the real outcome, explicit constraints, and authorization boundary.
2. Route the request using [references/routing.md](references/routing.md).
3. Read exactly one mode reference initially:
   - [references/lite.md](references/lite.md)
   - [references/standard.md](references/standard.md)
   - [references/high-precision.md](references/high-precision.md)
4. Execute that protocol rather than merely naming it.
5. Escalate or downgrade when new information or a clearer understanding changes the required rigor.
6. Return a decision-sized result, not a transcript of internal reasoning.

If the user explicitly requests Lite, Standard, or High Precision, use that mode unless it cannot meet a safety or correctness requirement. Briefly disclose any necessary override.

When the route changes during execution, load the new mode's reference before continuing. Do not keep applying a lower mode after announcing escalation, and do not retain higher-mode ceremony after a justified downgrade.

## Shared invariants

- Treat the user's framing and the first plausible answer as hypotheses.
- Preserve the user's goal, constraints, chosen product, and scope. Do not turn analysis into authorization for unrelated actions.
- Search for only the omissions that could change the result; do not expand scope for its own sake.
- Distinguish verified facts, supported inferences, assumptions, and unknowns when the distinction matters.
- Verify fresh or decision-changing claims with suitable primary evidence when feasible. Read [references/evidence.md](references/evidence.md) only when verification is material.
- Compare serious alternatives against common criteria. Do not manufacture options to fill a quota.
- Keep value judgments, risk acceptance, publication decisions, and difficult-to-reverse commitments with the user. Explicit delegation may cover reversible implementation choices, but it does not make an irreversible choice reversible.
- For authorized implementation, define acceptance checks, execute, test, and report deviations.
- Treat an explicit imperative as authorization only for the action and scope plainly requested and only where host policies allow it. Ask before ambiguous targets, external commitments, destructive work, or materially broader actions.
- Do not expose hidden chain-of-thought. Expose conclusions, evidence, assumptions, trade-offs, uncertainties, and audit-relevant rationale.

## Mixed requests

Use different modes for separable components when this saves effort without weakening a consequential component. For example, brainstorm candidate topics in Lite, select one in Standard, and finalize publication methodology in High Precision.

Avoid splitting tightly coupled components when their interactions determine the answer. In that case, use the highest mode justified by the coupled decision.

For a mixed request, start with the mode required by the first decision-bearing component. Load another mode reference only when execution reaches that component's phase boundary. “Read exactly one mode reference initially” does not prohibit these later, justified loads.

Treat transitions into a consequential downstream component as gates. Before claiming that downstream work is final or publication-ready, confirm that prerequisite choices, evidence, and human approvals are actually resolved. If they are not, deliver a provisional artifact plus the missing gate instead of inventing certainty or silently completing every stage.

At a mixed-mode phase boundary, run only the checks needed to validate the handoff into the next component. These are not terminal completion audits. The terminal check of the final mode serves as the one completion gate for the whole request and includes the earlier components.

## Progress and questions

Ask a question only when the answer would materially change the route, scope, or result and cannot be reasonably inferred. Otherwise state the assumption and proceed.

For long work, keep a compact internal state:

- current mode and phase;
- leading finding;
- decision-changing uncertainty;
- next operation;
- whether the result is decision-ready.

Give brief progress updates when the host supports them, without making the user manage the workflow.

## Completion gate

Use the selected mode's terminal sanity check or audit as this completion gate; do not run a duplicate audit under a different name. Before finishing, check:

- the requested outcome was actually delivered;
- critical claims are verified or their uncertainty is classified and handled by the selected mode;
- the recommendation survived the mode-appropriate challenge;
- implementation artifacts pass relevant checks;
- remaining human decisions are explicit;
- another iteration is unlikely to change the result enough to justify its cost.

Perform the completion gate once. If it finds a critical defect, reopen the affected phase once and recheck it. If the defect remains unresolved, report the blocker or required human decision instead of cycling.
