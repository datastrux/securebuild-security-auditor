# Web application security review reference

Use OWASP ASVS and WSTG as reference frameworks, not as proof of compliance. Record applicability, test method and evidence for every control.

## Inventory
- Assets, sensitive data, entry points, roles, sessions, backend/API, browser storage, third parties, trust boundaries.
- Deployment surfaces: preview, staging, production; actual response headers may differ.

## Injection and unsafe execution
- Search for `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `dangerouslySetInnerHTML`, `eval`, `Function`, script injection, dynamic URL/attribute assembly and unsafe templating.
- Check DOM clobbering, prototype pollution, untrusted deserialization, CSV/formula injection where relevant.
- Trace sources to sinks; a suspicious sink is not necessarily exploitable.

## Access and identity
- Verify authentication, authorization, object-level access and tenant isolation **on the server**.
- Check CSRF relevance, CORS allowlists, session cookies (Secure, HttpOnly, SameSite), token lifecycle, rate limiting.

## Data and privacy
- Secrets in bundles, source maps, logs, environment exposure; PII in URLs/storage/telemetry; unexpected network destinations.
- Verify third-party script data access and consent behavior where applicable.

## Headers
- Check actual deployed CSP (including script-src/connect-src/frame-ancestors), X-Content-Type-Options, Referrer-Policy, Permissions-Policy, HSTS, cache policy, cookies.
- CSP report-only can help plan enforcement, but `frame-ancestors` is not enforced in report-only mode. Validate embeds explicitly.

## Evidence quality
- EXECUTED: include command/browser steps, target, build, timestamp, observed result.
- INFERRED: include file/line, reasoning and assumptions.
- NOT RUN: explain why and how to execute safely elsewhere.

## Risk
Assess impact, exploit prerequisites, exposure, mitigations and confidence. Do not convert scanner severity directly into business priority.
