import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_gpt(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "user", "content": prompt}
    ]
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
