# Optional local checks

`python3 scripts/check_project.py /path/to/project --output ./securebuild-check.json`

The script performs **non-destructive heuristics only**: it inventories common JS package/lockfiles and flags suspicious textual patterns with file/line evidence. It does **not** execute the target project, crawl the web, detect secrets reliably, determine exploitability, or replace Semgrep/Gitleaks/OSV/ZAP. Treat all hits as POTENTIAL and verify manually.

It skips typical generated directories and limits scanned file size. It does not upload files or use the network. Inspect the output for sensitive paths before sharing.

For full security testing, use independently installed and authorized tools and record actual versions, commands, scope and evidence.
