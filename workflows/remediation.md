# REMEDIATE — explicit approval required

1. Quote approved finding IDs and exact scope. If approval is ambiguous, ask.
2. Preserve baseline, create reversible change boundary, and record current state.
3. Add tests that reproduce confirmed defect before patching when practical.
4. Implement minimal fix. Avoid unrelated formatting/refactors and arbitrary business-rule changes.
5. Run affected tests and full regression baseline; verify embed/routing/accessibility where applicable.
6. Inspect diff for accidental changes, secrets, new dependencies and changed permissions.
7. Report exact files, test results, residual risks, rollback steps and whether deployed.
8. Do not publish without explicit authorization.
