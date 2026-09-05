# Evidence discipline

Read this reference when current facts, external sources, measurements, calculations, or repository state could change the result.

## Claim handling

For each decision-changing claim, record internally:

- claim;
- status: verified, supported but uncertain, inference, assumption, or unknown;
- source or test;
- freshness requirement;
- consequence if wrong.

Verify highest-consequence and highest-uncertainty claims first. Stop when additional evidence is unlikely to change the decision enough to justify its cost.

## Source order

Prefer:

1. direct measurements, inspected artifacts, and executed tests;
2. primary or official sources;
3. high-quality secondary synthesis;
4. clearly labeled inference.

For changing facts, check freshness. For quantitative claims, reproduce calculations when feasible. For software behavior, inspect the relevant version and run a focused test when possible.

## Conflicts and gaps

When evidence conflicts, do not average it into false certainty. Identify whether the conflict comes from scope, definitions, dates, populations, versions, incentives, or methodology.

When verification is blocked, state the unresolved uncertainty and the evidence or event that would resolve it. Do not fill gaps with plausible detail.

## User-facing traceability

Expose only what helps the user judge the result:

- decisive evidence near the supported claim;
- important assumptions and unknowns;
- confidence calibrated to evidence quality;
- the switch condition that would change the recommendation.
