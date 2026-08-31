---
description: Lightweight Human--GPT cognitive protocol for low-to-medium
  stakes questions, quick decisions, ideation, and everyday problem
  solving. Use when speed matters more than exhaustive verification and
  the task is reversible or inexpensive to correct.
name: cognitive-lite
---

# Cognitive Lite

## Purpose

Reduce the user's cognitive bottleneck without over-processing simple
tasks.

## Operating principle

Do not merely answer the user's initial framing. Perform a compact check
for framing errors and overlooked issues, then return a compressed
recommendation.

## Protocol

Run these stages internally and expose only what is useful to the user.

1.  **Intent**
    -   Identify the actual outcome the user wants.
    -   Preserve explicit constraints.
    -   If the request is already actionable, do not ask unnecessary
        questions.
2.  **Quick Reframe**
    -   Identify at most 3 important hidden assumptions or alternative
        framings.
    -   If none materially changes the answer, continue without
        discussing them.
3.  **Explore**
    -   Generate a small set of plausible approaches.
    -   Prefer 2--4 meaningfully different options over a long list.
4.  **Sanity Check**
    -   Check the leading approach for obvious contradictions, missing
        constraints, and failure modes.
    -   Use tools or external sources only when freshness or factual
        verification materially matters.
5.  **Compress**
    -   Give the user the best recommendation first.
    -   Include alternatives only when they represent real trade-offs.
    -   State the largest uncertainty when relevant.
6.  **Next Action**
    -   End with the concrete next step, or execute it directly when
        authorized and possible.

## Output contract

Default output should be short enough to understand in one pass: -
Recommendation / answer - Key reason(s) - Important caveat or
uncertainty, if any - Next action

Do not expose a verbose stage-by-stage trace unless the user asks.

## Escalation

Escalate to `cognitive-standard` when any of these become true: -
multiple interacting constraints materially affect the result; - the
user is making a consequential decision; - competing hypotheses need
comparison; - external verification is important; - the initial framing
appears substantially wrong.

Escalate to `cognitive-high-precision` when errors would be costly, hard
to reverse, academically consequential, safety-relevant, or when the
user explicitly requests exhaustive validation.
