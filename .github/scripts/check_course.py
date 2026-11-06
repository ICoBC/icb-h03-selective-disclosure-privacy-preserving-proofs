#!/usr/bin/env python3
"""ICoBC Course Workshop · checks a LiaScript course (README.md). Errors fail the check; warnings do not."""
import re, sys, pathlib
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "README.md"); t = p.read_text(encoding="utf-8")
E, W = [], []
head = re.match(r"\s*<!--(.*?)-->", t, re.S)
if not head: E.append("LiaScript header comment <!-- ... --> is missing at the top of the file.")
else:
    for k in ("author", "version", "language", "logo"):
        if not re.search(rf"^\s*{k}\s*:", head.group(1), re.M): E.append(f'header field "{k}" is missing.')
    if not re.search(r"^\s*language\s*:\s*en", head.group(1), re.M): E.append('header field "language" must be "en".')
lines = t.split("\n"); i = 0
while i < len(lines):
    if re.match(r"\s*- \[\((X| )\)\]", lines[i]):
        j = i; n = 0
        while j < len(lines) and re.match(r"\s*- \[\((X| )\)\]", lines[j]): n += "[(X)]" in lines[j]; j += 1
        if n != 1: E.append(f"line {i + 1}: single-choice quiz needs exactly one [(X)] (found {n}).")
        i = j
    else: i += 1
for m in re.finditer(r"!\[([^\]]*)\]\(([^)\s]+)", t):
    if not m.group(1).strip(): E.append(f"image {m.group(2)}: alt text is missing.")
    if not re.match(r"https?://", m.group(2)) and not (p.parent / m.group(2)).exists(): E.append(f"image {m.group(2)}: file not found.")
AM = {"color": "colour", "center": "centre", "behavior": "behaviour", "organization": "organisation", "recognize": "recognise",
      "analyze": "analyse", "catalog": "catalogue", "enroll": "enrol", "percent": "per cent", "favorite": "favourite", "program": "programme"}
body = re.sub(r"<!--.*?-->", "", t, flags=re.S)
for w, b in AM.items():
    for m in re.finditer(rf"\b{w}(s|d|ed|ing)?\b", body, re.I): W.append(f'"{m.group(0)}": British English is "{b}".')
for e in E: print("::error::" + e)
for w in sorted(set(W)): print("::warning::" + w)
print(f"{len(E)} errors, {len(set(W))} warnings"); sys.exit(1 if E else 0)
