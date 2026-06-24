import ollama

def generate_jd(resume_text):

    prompt = f"""
Create a SHORT Job Description.

Resume:
{resume_text[:1000]}

Return ONLY:

1. Job Title
2. Skills
3. Experience
4. Responsibilities

Keep response under 250 words.
"""

    response = ollama.chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]