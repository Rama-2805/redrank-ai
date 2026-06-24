import ollama

response = ollama.chat(
    model="qwen2.5-coder:14b",
    messages=[
        {
            "role": "user",
            "content": "Write a Machine Learning Engineer job description"
        }
    ]
)

print(response["message"]["content"])
