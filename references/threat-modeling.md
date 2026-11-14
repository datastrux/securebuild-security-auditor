# Threat modeling guide

1. Define system and security objectives.
2. Inventory data (public, internal, confidential, regulated), actors and privileges.
3. Map data flows and boundaries: browser ↔ app server ↔ APIs ↔ third parties; iframe parent ↔ child.
4. Apply STRIDE: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege.
5. For each scenario record entry point, attacker control, affected asset, preconditions, mitigating control, detection, validation method and residual risk.
6. Prioritize by realistic exposure and impact; label assumptions.

Example: an untrusted URL parameter flows into an HTML sink. Validate actual encoding/sanitization and reachable route before classifying confirmed DOM XSS.

Avoid claiming 'no risk' when a path was not exercised. Use `templates/threat-model.md`.
