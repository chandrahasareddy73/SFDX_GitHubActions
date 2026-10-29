from openai import OpenAI

client = OpenAI()

with open("changedFiles.txt") as f:
    changes = f.read()

prompt=f"""
Generate Salesforce release notes.

Changes:

{changes}

Format:

Features
Bug Fixes
Technical Changes
Deployment Notes
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role":"user","content":prompt}]
)

notes=response.choices[0].message.content

with open("release_notes.md","w") as f:
    f.write(notes)

print(notes)