# main.py
import os
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return {"error": "API key no configurada en .env"}

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": request.message}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": response.status_code, "details": response.text}

    data = response.json()
    try:
        reply = data["choices"][0]["message"]["content"]
    except KeyError:
        reply = data
    return {"reply": reply}
