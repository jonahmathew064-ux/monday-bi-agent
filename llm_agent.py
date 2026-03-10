from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_insight(question, context):

    prompt = f"""
You are a business intelligence assistant for company founders.

Business Data:
{context}

Founder Question:
{question}

Provide:
1. Key numbers
2. Insights
3. Risks if data is incomplete
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
