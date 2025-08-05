import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}
MODEL = "llama3-8b-8192" 

def simplify_text(text: str) -> str:
    prompt = f"Explain the following legal clause in simple, clear language:\n\n{text}"

    body = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }

    response = requests.post(API_URL, headers=HEADERS, json=body)
    result = response.json()

    print("🪵 Groq response:", result)

    if "choices" not in result:
        return f"❌ LLM Error: {result.get('error', 'Unknown error')}"

    return result["choices"][0]["message"]["content"].strip()


def answer_question(question: str, context: str = "") -> str:
    if context:
        prompt = f"Given the following legal clause:\n\n{context}\n\nAnswer this question simply:\n{question}"
    else:
        prompt = f"Answer this legal question clearly and simply:\n\n{question}"

    body = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }

    response = requests.post(API_URL, headers=HEADERS, json=body)
    result = response.json()

    return result["choices"][0]["message"]["content"].strip()
