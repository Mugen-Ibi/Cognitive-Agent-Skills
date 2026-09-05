# Routing

Route by expected cost of error, not by how intellectually interesting the request appears.

## Decision order

1. Honor an explicit mode request unless a higher safety or correctness threshold is necessary.
2. Check decisive overrides.
3. Score the remaining task dimensions as a guide.
4. Adjust for mixed-mode components and new evidence during execution.

## Decisive overrides

Use High Precision when one of these is central to a deliverable that will be relied upon:

- consequential safety, legal, medical, or financial action;
- publication-grade research or formal methodology;
- durable governance or architecture with costly reversal;
- conflicting evidence that can change a consequential or hard-to-reverse decision, or that must be resolved for an auditable deliverable;
- an explicit request for rigorous, exhaustive, auditable, or independently challenged work.

Use Lite despite surface complexity when the output is deliberately disposable, exploratory, inexpensive to correct, and not being represented as verified.

## Scored dimensions

Score each dimension from 0 to 2:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Consequence | inconvenience | meaningful rework | serious downstream harm |
| Reversibility | easy | moderate | costly or public |
| Complexity | few independent variables | interacting constraints | system-level dependencies |
| Uncertainty | established | important assumptions | unstable framing or conflicts |
| Evidence | reasoning is enough | current evidence helps | auditability or primary evidence required |

Default interpretation:

- 0–3: Lite
- 4–7: Standard
- 8–10: High Precision

The score informs judgment; it does not override a decisive condition. The dimensions are correlated signals, not independent measurements, so do not present the sum as scientific precision.

Apply these floors before interpreting the total:

- any score of 2 for consequence, irreversibility, complexity, uncertainty, or evidence requires at least Standard;
- consequence 2 plus irreversibility 2 normally requires High Precision;
- evidence 2 requires High Precision when primary evidence and an audit trail are essential to the deliverable; otherwise it sets a Standard floor;
- a decisive override still takes precedence.

At a 3/4 or 7/8 boundary, choose the lower mode when the decision is reversible and a cheap later check can catch an error. Choose the higher mode when errors are asymmetric, propagate downstream, or cannot be detected before harm. If the classification itself is uncertain, begin with Standard and reassess after the first decision-changing verification.

## Effort budget

After establishing the safe rigor floor, account for the user's urgency, desired depth, cognitive bandwidth, and the time or cost of verification. These factors adjust how much exploration and evidence gathering to perform inside the selected mode; they do not justify routing below a safety, publication, or irreversible-decision requirement.

## Mode boundaries

### Lite

Use for ideation, quick explanation, low-cost wording or naming choices, and reversible preliminary decisions. The objective is a useful answer with a compact framing and sanity check.

### Standard

Use for substantive multi-step work, architecture that remains revisable, project or research planning, organizational choices, and comparisons with meaningful trade-offs. This is the default when several constraints interact.

### High Precision

Use for hard-to-reverse or high-consequence decisions, publication-bound research, durable governance, critical architecture, and work requiring an auditable evidence trail or independent challenge.

## Dynamic changes

Escalate when discovering contradictory evidence, additional stakeholders, hidden dependencies, a larger cost of error, or a need for reproducibility. Preserve completed work and continue under the stricter mode.

Downgrade only when every decisive trigger that established the higher safe rigor floor has been removed, satisfied, or shown not to apply. A bounded problem or low marginal value of more evidence can reduce effort inside the current mode, but cannot by itself cross the safe floor. When a High Precision evidence search is exhausted, preserve the residual uncertainty under that mode rather than downgrading. Never downgrade merely to shorten the answer.

## Calibration examples

| Request | Route | Decisive reason |
|---|---|---|
| Brainstorm workshop titles | Lite | disposable and reversible |
| Compare authentication approaches for a prototype | Standard | interacting technical trade-offs |
| Approve production identity architecture | High Precision | durable security consequences |
| Generate possible research questions | Lite | exploratory stage |
| Select the research question | Standard | framing affects downstream work |
| Finalize a publishable experiment | High Precision | reproducibility and publication |
