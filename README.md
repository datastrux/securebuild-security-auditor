# SecureBuild Security Auditor

A portable, evidence-driven security review skill for web applications. **Not** a certification, penetration-test substitute, or automatic vulnerability scanner. Human approval is required for changes and release decisions.

## Install
- **Skill-file import**: import this folder/ZIP only if your AI platform supports a directory-based skill package. The entry point is `SKILL.md`; import compatibility varies by platform.
- **Lovable Personal Skills (manual)**: copy the name, description and content from `lovable-personal-skill.md`. Supplemental references may need to be attached separately or stored in project knowledge; manual content fields do **not** automatically install bundled files.
- **Repository-based agents**: point your agent at `SKILL.md` and permit it to read referenced files.

## Usage
“Use SecureBuild Security Auditor in AUDIT mode on this project. Begin read-only, disclose available tools, preserve regression baseline, and report evidence and limitations. Do not modify or deploy.”

Modes: AUDIT, PLAN, REMEDIATE, VERIFY, RELEASE GATE.

## Contents
- `references/`: security review guidance and domain-specific checks.
- `workflows/`: approval-gated operating procedures.
- `templates/`: threat model, findings, test matrix, and release report.
- `scripts/`: opt-in local checks (safe, dependency-free static heuristics), with explicit limitations.
- `.github/workflows/`: basic package integrity workflow.

## Scope and safety
No client-specific data, proprietary assessment, or secrets are included. Do not run active DAST without permission. Tool results are evidence only when executed against the relevant build. See `LICENSE` and `SECURITY.md`.
