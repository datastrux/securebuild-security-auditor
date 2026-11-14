# RELEASE GATE — human decision

Require a dated release candidate ID, test matrix, findings register and approved exceptions.

Review:
- Critical/high security findings and documented risk treatment.
- Functional and domain-specific integrity tests.
- Dependency and supply-chain status.
- Browser, accessibility, responsive and performance checks where in scope.
- Embedded-host compatibility, CSP and actual deployment headers.
- Privacy/telemetry destinations, rollback and monitoring.

Decision: RECOMMEND RELEASE / RECOMMEND HOLD / INSUFFICIENT EVIDENCE. Never represent the recommendation as an authorization. List NOT RUN items and residual risks prominently.
