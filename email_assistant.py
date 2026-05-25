#!/usr/bin/env python3
"""MiMo Email Assistant - Draft and reply to emails with AI."""
import os, argparse
from openai import OpenAI

client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url="https://api.xiaomimimo.com/v1")

def draft(description, tone="professional"):
    resp = client.chat.completions.create(model="mimo-v2.5-pro", messages=[
        {"role": "system", "content": f"Email writer. Tone: {tone}. Include subject."},
        {"role": "user", "content": f"Draft: {description}"}])
    return resp.choices[0].message.content

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--draft"); p.add_argument("--tone", default="professional")
    a = p.parse_args()
    if a.draft: print(draft(a.draft, a.tone))
