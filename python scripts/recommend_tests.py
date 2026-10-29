from openai import OpenAI

client = OpenAI()

with open("changedFiles.txt") as f:
    changes = f.read()

prompt = f"""
Salesforce metadata changed:

{changes}

Provide only comma separated Apex test classes.
No explanation.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role":"user","content":prompt}]
)

tests = response.choices[0].message.content.strip()

print(tests)

with open("ai_tests.txt","w") as f:
    f.write(tests)