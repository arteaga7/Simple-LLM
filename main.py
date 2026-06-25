# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Modelo para la petición del usuario
class ChatRequest(BaseModel):
    message: str

# Endpoint del chatbot
@app.post("/chat")
def chat(request: ChatRequest):
    # Aquí llamamos a la API de Groq
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer TU_API_KEY_DE_GROQ",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",  # Modelo de Groq
        "messages": [
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": request.message}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    # Extraemos la respuesta del modelo
    reply = data["choices"][0]["message"]["content"]
    return {"reply": reply}
