"""Offline check for the org default files: YAML and JSON parse, each starter workflow has its properties file,
and every relative Markdown link points at a file that exists. Needs PyYAML. Exit 1 on any problem."""
import glob, json, os, re, sys

import yaml

bad = []
for f in glob.glob("ISSUE_TEMPLATE/*.yml") + glob.glob("workflow-templates/*.yml") + glob.glob(".github/workflows/*.yml"):
    try:
        yaml.safe_load(open(f, encoding="utf-8"))
    except Exception as e:
        bad.append(f"{f}: invalid YAML ({e})")
for f in glob.glob("workflow-templates/*.properties.json"):
    try:
        json.load(open(f, encoding="utf-8"))
    except Exception as e:
        bad.append(f"{f}: invalid JSON ({e})")
for f in glob.glob("workflow-templates/*.yml"):
    p = f[:-4] + ".properties.json"
    if not os.path.exists(p):
        bad.append(f"{f}: missing {p}")
for f in glob.glob("*.md") + glob.glob("profile/*.md"):
    text = open(f, encoding="utf-8").read()
    for m in re.findall(r'\]\(([^)\s]+)\)|src="([^"]+)"', text):
        url = m[0] or m[1]
        if url.startswith(("#", "mailto:", "http://", "https://")):
            continue
        if not os.path.exists(os.path.join(os.path.dirname(f), url.split("#")[0])):
            bad.append(f"{f}: {url} -> missing file")
for b in bad:
    print("FAIL", b)
print("verify: " + ("FAILED" if bad else "ok"))
sys.exit(1 if bad else 0)
