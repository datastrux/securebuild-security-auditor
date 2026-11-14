# VERIFY — post-change validation

1. Identify exact version/build and approved remediation IDs.
2. Reproduce original issue to verify it is no longer observable.
3. Re-run relevant static/dependency/secret scans, negative inputs and browser tests.
4. Verify baseline tests and new regression tests.
5. Inspect actual deployed response headers if a deployed target is authorized and accessible.
6. Validate authorized iframe embeddings and cross-origin messaging.
7. Record PASS/FAIL/NOT RUN per test with evidence, confidence and outstanding limitations.
8. A missing scanner alert alone does not prove remediation.
