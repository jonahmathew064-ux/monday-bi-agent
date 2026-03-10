import ollama

print("LLM AGENT MODULE LOADED")

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
3. Risks if data is incomplete.
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]