# Dependency and supply-chain assessment

1. Identify package manager and authoritative lockfile (npm, pnpm, yarn, Bun, etc.). Never assume `npm audit` works with another lockfile.
2. Record dependency graph, installed version, advisory ID, affected/fixed range, direct/transitive path, package purpose, build/runtime location.
3. De-duplicate advisories while preserving affected paths.
4. Check reachable vulnerable API with code references and conditions; classify CONFIRMED, INFERRED NOT REACHABLE, or NOT TESTED. Static reachability is not an exploit proof.
5. Consider CI/build exposure, untrusted build inputs, scripts, compromised registries, package provenance and release age.
6. Propose minimal compatible upgrade, lockfile changes, breaking changes and rollback.
7. Re-run install/build/unit/browser tests and scan the resulting lockfile. Document unresolved risks.

Never blindly override transitive versions without verifying compatibility. Do not treat build-only vulnerabilities as universally harmless.
