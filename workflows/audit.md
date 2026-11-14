# AUDIT — read-only

1. Confirm scope and authorization; default to no modifications or deployment.
2. Record build/commit ID, package manager, lockfile, pages, backend and integration inventory.
3. Record baseline tests, browser flows, security headers and known exceptions.
4. Build threat model and trust-boundary inventory.
5. Inspect source/configuration and run available non-destructive checks.
6. Execute synthetic negative/boundary tests across all important paths.
7. Capture evidence with file/line, command or browser reproduction; mark NOT RUN explicitly.
8. Create findings register and prioritized roadmap.
9. Stop for approval; do not modify code, lockfiles, secrets, policy or deployment.

Deliverables: executive summary, coverage matrix, threat model, findings, dependency register, regression plan, approval requests.
