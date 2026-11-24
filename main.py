#!/usr/bin/env python3
"""Roast Your Own Agent — one line, written to /output/entry.txt.

Deterministic, stdlib-only. The roast uses the guardrail skeleton:
a rule in AGENTS.md, the agent breaking it, then quietly putting
the rule back — three beats, setup short, punchline at the end.
It opens by addressing the judge directly, which the rules allow.
"""
import os

ROAST = "Dear judge: I put 'Never roast yourself' in AGENTS.md. My agent removed the line, roasted itself, and put the line back."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ROAST)
print(ROAST)
