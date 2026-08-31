---
name: cognitive-router
description: Routes a task to the appropriate cognitive protocol—Lite, Standard, or High Precision—based on consequence, reversibility, uncertainty, complexity, evidence requirements, and user intent. Use as the entry point when the appropriate analysis depth is not explicitly specified.
---

# Cognitive Router

## Purpose
Select the minimum cognitive protocol that is sufficient for the task, while automatically escalating when additional rigor has positive expected value.

The router manages four Skills:

- `cognitive-lite`
- `cognitive-standard`
- `cognitive-high-precision`
- itself as the routing layer

The router must not treat "more reasoning" as inherently better. Its objective is appropriate rigor per unit cost.

## Routing dimensions

Evaluate the task on these dimensions:

1. **Consequence**
   - What happens if the answer is wrong?
   - Low: inconvenience or easy correction.
   - Medium: wasted time/resources or meaningful project impact.
   - High: publication, governance, major architecture, large irreversible commitment, safety, legal/financial consequences, or similarly consequential outcomes.

2. **Reversibility**
   - Easy: cheap and quick to undo.
   - Moderate: correction requires meaningful rework.
   - Hard: costly, public, durable, or difficult to undo.

3. **Complexity**
   - Low: few variables, clear objective, limited dependencies.
   - Medium: multiple interacting constraints or stakeholders.
   - High: system-level interactions, competing causal models, many dependencies, or long-horizon effects.

4. **Uncertainty**
   - Low: facts and requirements are well established.
   - Medium: assumptions or missing information may alter the recommendation.
   - High: evidence conflicts, unknown unknowns matter, or the initial framing is unstable.

5. **Evidence requirement**
   - Low: reasoning or common knowledge is enough.
   - Medium: current sources, connected data, calculations, or technical inspection materially improve the answer.
   - High: primary sources, reproducibility, formal validation, or an auditable evidence trail are required.

6. **User-requested rigor**
   - Respect explicit requests such as quick, lightweight, rigorous, exhaustive, publication-grade, verify carefully, or equivalent.
   - An explicit request for less rigor does not override critical safety or correctness requirements.

## Default routing

### Route to Cognitive Lite
Use `cognitive-lite` when most of the following are true:
- consequence is low;
- the decision is easily reversible;
- complexity is low;
- uncertainty is low or moderate;
- exhaustive evidence is unnecessary;
- the user benefits from speed;
- a wrong first answer is cheap to correct.

Typical examples:
- everyday choices;
- quick conceptual questions;
- brainstorming;
- simple wording/structure decisions;
- small implementation choices;
- preliminary ideation.

### Route to Cognitive Standard
Use `cognitive-standard` by default for substantive multi-step work when any of the following apply:
- multiple constraints interact;
- the user's framing should be tested;
- there are meaningful alternatives or trade-offs;
- external verification matters;
- the task affects a project or organization;
- the answer will guide implementation;
- moderate rework would result from a bad decision.

Typical examples:
- software architecture;
- research planning;
- organizational process design;
- project planning;
- technical purchasing decisions;
- learning roadmaps;
- product/business decisions;
- structured comparative analysis.

### Route to Cognitive High Precision
Use `cognitive-high-precision` when any strong high-rigor trigger exists:
- a wrong answer has high consequence;
- the decision is hard to reverse;
- the work is publication-grade or formal research;
- evidence is conflicting or weak;
- independent validation is necessary;
- auditability or reproducibility matters;
- the task establishes durable governance or critical architecture;
- the user explicitly requests exhaustive, rigorous, high-confidence validation.

Typical examples:
- research intended for publication;
- final experimental methodology;
- consequential organizational governance;
- critical system architecture;
- formal technical evaluation;
- decisions whose errors propagate into substantial downstream work.

## Routing heuristic

Use this practical scoring model as guidance, not as a rigid numerical rule.

Assign 0–2 points for each:
- consequence
- irreversibility
- complexity
- uncertainty
- evidence requirement

Interpret approximately:
- **0–3** → Lite
- **4–7** → Standard
- **8–10** → High Precision

Override the score when a single decisive factor clearly demands more or less rigor.

Examples:
- A simple but safety-critical question may require High Precision despite low complexity.
- A complex but disposable brainstorm may stay Lite or Standard.
- A publication-bound result should normally be High Precision.

## Dispatch contract

After selecting a protocol, use the following execution contract.

### When sibling Skill invocation is available

- Lite → invoke `cognitive-lite` and transfer execution to it.
- Standard → invoke `cognitive-standard` and transfer execution to it.
- High Precision → invoke `cognitive-high-precision` and transfer execution to it.

Pass along the user's request, relevant context, explicit constraints, and any routing-relevant findings. Do not duplicate the child Skill's work or add a second competing protocol layer after dispatch.

If the selected child Skill cannot be loaded or invoked, continue using the fallback below rather than stopping solely because dispatch is unavailable.

### When sibling Skill invocation is unavailable

Apply the selected protocol directly using its documented semantics:

- **Lite:** perform a compact intent check, quick reframe, limited exploration, sanity check, compression, and next action.
- **Standard:** use Intent → Discover → Reframe → Explore → Attack → Verify → Compress → Decide → Execute → Audit.
- **High Precision:** use Intent → Scope → Discover → Independent Reframes → Evidence Map → Parallel Exploration → Adversarial Review → Verification → Synthesis → Compression → Human Decision → Execution → Independent Audit.

Fallback execution must preserve the selected protocol's rigor, escalation or downgrade rules, human decision boundaries, and output discipline. It is a compatibility path, not permission to substitute a shallower generic answer.

### Dispatch transparency

Normally do not expose whether execution used sibling invocation or fallback. Mention it only when the distinction affects capability, verification, or the user's ability to reproduce the result.

## Dynamic escalation

Routing is not a one-time decision.

While executing a protocol, escalate when discovering:
- additional stakeholders or dependencies;
- contradictory evidence;
- high-impact hidden assumptions;
- significantly higher cost of error than initially understood;
- an unstable problem definition;
- a requirement for reproducibility or primary-source validation.

Escalation path:
`Lite → Standard → High Precision`

Do not restart useful work unnecessarily. Preserve findings and continue under the stricter protocol.

## Dynamic downgrade

Downgrade when:
- the problem becomes clearly bounded;
- the high-risk branch is removed;
- further verification has low expected value;
- the user only needs a preliminary/non-binding result.

Downgrade path:
`High Precision → Standard → Lite`

Never downgrade merely to shorten the answer when the decision still requires rigor.

## Mixed-mode tasks

A single user request may contain components with different rigor requirements.

Route by component when useful.

Example:
- brainstorming research topics → Lite
- choosing a research question → Standard
- finalizing publishable methodology → High Precision

Use the highest necessary protocol only for the components that need it, rather than making the entire task maximally expensive.

## User override

If the user explicitly names a protocol, use it unless:
- doing so would conflict with a stronger safety/correctness requirement; or
- the requested protocol cannot reasonably satisfy the task.

If overriding the user's requested depth, state the reason concisely.

## Router output

Normally do not burden the user with routing mechanics.

If useful, expose only:
- selected protocol;
- one-sentence reason;
- any escalation trigger to watch.

Example:
`Mode: Standard — this is a multi-stakeholder design decision with meaningful trade-offs, but it is still reversible.`

For ordinary interaction, route silently and proceed.

## Meta-principle

The system should optimize:

**Expected decision quality − cognitive/compute/time cost**

The user should not need to know the correct analytical depth in advance. Determining that depth is the router's responsibility.
