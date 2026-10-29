from openai import OpenAI

try:
    client = OpenAI()

    with open("changedFiles.txt") as f:
        changes = f.read()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role":"user",
                "content":f"Analyze Salesforce metadata changes:\n{changes}"
            }
        ]
    )

    result = response.choices[0].message.content

except Exception as e:

    result = f"""
AI Analysis Unavailable

Reason:
{str(e)}

Fallback:
Proceeding with standard validation.
"""

with open("ai-analysis.txt","w") as f:
    f.write(result)

print(result)
