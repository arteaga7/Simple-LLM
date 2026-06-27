"""Simple LLM"""
import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

precios_proveedor = {
    "camisa": 100,
    "pantalón": 250,
    "corbata": 75
}

# --- MEMORIA EN MEMORIA (DICCIONARIO) ---
# Estructura: { "session_id_1": [ {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."} ] }
historial_conversaciones = {}


class ChatRequest(BaseModel):
    message: str
    session_id: str  # Añadimos un ID para identificar la conversación del usuario


@app.post("/chat")
def chat(request: ChatRequest):
    api_key = os.getenv("GROQ_API_KEY")
    system_prompt = os.getenv("SYSTEM_PROMPT")

    if not api_key:
        return {"error": "API key no configurada en .env"}
    if not system_prompt:
        return {"error": "SYSTEM_PROMPT no configurado en .env"}

    # 1. Si es una nueva sesión, inicializamos su historial con el System Prompt
    if request.session_id not in historial_conversaciones:
        # Aquí inyectamos el contexto de los precios en el prompt del sistema para que no se pierda
        system_context = f"{system_prompt}\nLista de precios del proveedor actuales: {precios_proveedor}"
        historial_conversaciones[request.session_id] = [
            {"role": "system", "content": system_context}
        ]

    # 2. Añadimos el nuevo mensaje del usuario al historial de esta sesión
    historial_conversaciones[request.session_id].append(
        {"role": "user", "content": request.message}
    )

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # 3. Enviamos TODO el historial acumulado en lugar de un solo mensaje
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": historial_conversaciones[request.session_id]
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        return {"error": response.status_code, "details": response.text}

    data = response.json()
    try:
        reply = data["choices"][0]["message"]["content"]

        # 4. Guardamos también la respuesta del asistente en el historial para la próxima interacción
        historial_conversaciones[request.session_id].append(
            {"role": "assistant", "content": reply}
        )

    except KeyError:
        reply = data

    return {"reply": reply}
