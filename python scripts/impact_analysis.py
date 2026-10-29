from openai import OpenAI

client = OpenAI()

with open("changedFiles.txt","r") as f:
    changes = f.read()

prompt = f"""
Analyze these Salesforce metadata changes.

Identify:
1. Impacted components
2. Potential dependencies
3. Risk score
4. Recommended test classes

Changes:
{changes}
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role":"user","content":prompt}]
)

print(response.choices[0].message.content)

with open("ai-analysis.txt","w") as out:
    out.write(response.choices[0].message.content)