# Embedded JavaScript and iframe security

## Distinguish deployment models
- Third-party JS injected into host origin: same-origin page privileges; wrapper conventions do not create a security boundary.
- Cross-origin iframe: browser origin isolation; evaluate sandbox, allow, CSP and postMessage.
- Browser extension: extension permissions, content-script isolation, message bridge and host permissions.

## Audit checklist
- Inventory host DOM reads/writes, form fields, cookies, local/session storage, global namespace, event listeners, MutationObservers and network endpoints.
- Validate postMessage event.origin, event.source, payload schema, action allowlist, targetOrigin (never '*' for sensitive messages), replay and size bounds.
- Check idempotent init, duplicate scripts, teardown, AbortController, observer/timer limits, layout interference and memory leaks.
- Inspect CSP `frame-ancestors` on the framed response; it controls **who may frame** the app. `frame-src` controls **what the app may frame**.
- Do not set `X-Frame-Options: DENY` or `SAMEORIGIN` if cross-origin embedding is intended.
- Request a documented allowlist for production, staging and preview; use exact origin syntax.
- Check cookie restrictions and storage behavior in third-party contexts.

## Evidence
Capture embedding origin, framed origin, browser, CSP/headers, messages, console errors, network destinations and observed behavior. Avoid storing personal information.
