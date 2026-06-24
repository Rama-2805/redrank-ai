import ollama

def generate_jd(resume_text):

    prompt = f"""
Create a professional Job Description
based on this resume.

Resume:
{resume_text}

Return:

1. Job Title
2. Required Skills
3. Experience
4. Responsibilities
5. Preferred Qualifications

Professional HR format.
"""

    response = ollama.chat(
        model="qwen2.5-coder:14b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]