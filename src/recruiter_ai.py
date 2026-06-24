import ollama

def ask_recruiter(question):

    response = ollama.chat(
        model="qwen2.5-coder:14b",
        messages=[
            {
                "role": "system",
                "content": """
You are an expert technical recruiter.

Analyze candidates.
Explain ranking decisions.
Identify strengths and weaknesses.
Provide concise hiring recommendations.
"""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]