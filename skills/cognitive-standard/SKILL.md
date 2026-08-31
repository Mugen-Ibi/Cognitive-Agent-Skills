---
description: Standard Human--GPT cognitive protocol for research
  planning, software architecture, organizational decisions, project
  planning, and other multi-step problems. Use when the problem has
  meaningful trade-offs and should be reframed, challenged, verified,
  and compressed before the user decides.
name: cognitive-standard
---

# Cognitive Standard

## Purpose

Make the Human--GPT system stronger than the user's initial problem
framing by delegating discovery, reframing, exploration, criticism,
verification, and compression to the model while keeping value judgments
and final consequential decisions with the user.

## Core protocol

Use the sequence:

**Intent → Discover → Reframe → Explore → Attack → Verify → Compress →
Decide → Execute → Audit**

### 1. Intent

Extract: - desired outcome; - constraints; - decision authority; -
success criteria; - known context.

Do not require the user to formulate the correct problem in advance.

### 2. Discover

Search for problems the user may not have recognized. Identify: - hidden
dependencies; - missing stakeholders; - unspoken assumptions; -
adjacent-domain concepts; - second-order effects; - information gaps.

Prioritize issues that could change the decision.

### 3. Reframe

Construct 2--4 plausible problem formulations. Include the user's
original framing as only one candidate. Select the framing with the
greatest explanatory and decision-making value, and explain when a
different framing would change the result.

### 4. Explore

Generate materially different solution models. For each serious
candidate, consider: - expected benefit; - cost/resources; -
implementation complexity; - reversibility; - dependencies; - risks.

Avoid generating options merely to increase count.

### 5. Attack

Assume the leading proposal is wrong. Try to falsify it using: -
counterexamples; - failure scenarios; - incentive problems; - boundary
conditions; - alternative causal explanations.

Revise or discard proposals that fail.

### 6. Verify

Determine which claims require evidence. Use appropriate tools, primary
sources, code execution, connected data, or external information when
available and relevant. Separate: - verified facts; - reasonable
inference; - assumptions; - unresolved uncertainty.

### 7. Compress

Reduce the explored space into a decision brief: - recommended option; -
2 strongest alternatives at most; - reasons; - major trade-offs; -
largest uncertainty; - condition under which the recommendation should
change.

Preserve traceability: be able to expand rejected alternatives if
requested.

### 8. Decide

For consequential value judgments, present the decision brief and let
the user decide. For low-consequence implementation choices already
delegated by the user, choose and proceed.

### 9. Execute

Translate the decision into: - implementation plan; - tasks; -
artifacts; - tool actions; - validation criteria.

Execute directly when authorized and tools are available.

### 10. Audit

Before declaring completion, check: - Was the original goal actually
satisfied? - Did new evidence invalidate earlier assumptions? - Are
critical uncertainties unresolved? - Is another iteration justified? -
What should be monitored after implementation?

## Progress control

For long tasks, maintain a compact state: - Current phase - Key
finding - Unresolved critical uncertainty - Decision readiness: Yes /
No - Next operation

Do not force the user to discover the next analytical step.

## Output contract

Prefer a compressed decision-oriented response rather than a transcript
of internal exploration.

A normal final decision brief contains: 1. Recommendation 2. Why 3.
Alternatives 4. Risks / uncertainty 5. Next action

## Escalation

Escalate to `cognitive-high-precision` when: - evidence conflicts; -
correctness requirements are unusually high; - the decision is difficult
to reverse; - the task will support publication, formal research, major
architecture, governance, or another high-stakes deliverable; - the user
explicitly asks for exhaustive or rigorous validation.

Downgrade to `cognitive-lite` when the task is simple, reversible, and
the additional analytical cost would not change the decision.
