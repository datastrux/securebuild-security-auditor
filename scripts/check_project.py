#!/usr/bin/env python3
"""Offline, non-destructive JavaScript security heuristics; not a vulnerability scanner."""
import argparse, json, pathlib, re, sys
SKIP={'.git','node_modules','dist','build','.next','.venv','coverage','.turbo'}
PATTERNS={
 'HTML_SINK':r'\b(?:innerHTML|outerHTML|insertAdjacentHTML|dangerouslySetInnerHTML)\b',
 'DYNAMIC_EXECUTION':r'\b(?:eval|new\s+Function)\s*\(',
 'POSTMESSAGE':r'\bpostMessage\s*\(',
 'STORAGE':r'\b(?:localStorage|sessionStorage)\b',
 'URL_INPUT':r'\b(?:URLSearchParams|location\.search|location\.hash)\b',
 'NETWORK':r'\b(?:fetch|XMLHttpRequest|sendBeacon)\s*\(',
}
def main():
 p=argparse.ArgumentParser();p.add_argument('project');p.add_argument('--output');a=p.parse_args()
 root=pathlib.Path(a.project).resolve()
 if not root.is_dir(): p.error('project must be a directory')
 out={'scope':str(root),'method':'offline heuristic, NOT security verification','package_files':[],'findings':[],'files_scanned':0}
 for f in root.rglob('*'):
  if not f.is_file() or any(part in SKIP for part in f.relative_to(root).parts): continue
  rel=str(f.relative_to(root))
  if f.name in {'package.json','bun.lock','bun.lockb','package-lock.json','pnpm-lock.yaml','yarn.lock'}:out['package_files'].append(rel)
  if f.suffix not in {'.js','.jsx','.ts','.tsx','.mjs','.cjs'} or f.stat().st_size>1024*1024:continue
  try: lines=f.read_text(encoding='utf-8').splitlines()
  except (UnicodeError,OSError):continue
  out['files_scanned']+=1
  for n,line in enumerate(lines,1):
   for name,regex in PATTERNS.items():
    if re.search(regex,line):out['findings'].append({'kind':name,'file':rel,'line':n,'status':'POTENTIAL — REVIEW REQUIRED'})
 payload=json.dumps(out,indent=2)
 if a.output:pathlib.Path(a.output).write_text(payload+'\n',encoding='utf-8')
 else:print(payload)
 return 0
if __name__=='__main__':sys.exit(main())
