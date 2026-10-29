from openai import OpenAI
import re

client = OpenAI()

with open("changedFiles.txt") as f:
    changes = f.read()

prompt = f"""
Review Salesforce deployment risk.

Files:
{changes}

Return only a number between 1 and 10.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role":"user","content":prompt}]
)

risk = response.choices[0].message.content.strip()

match = re.search(r"\d+", risk)

score = match.group(0) if match else "5"

with open("risk_score.txt","w") as f:
    f.write(score)

print(score)