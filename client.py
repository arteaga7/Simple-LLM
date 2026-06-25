# client.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def send_message(message: str):
    url = "http://127.0.0.1:8000/chat"
    payload = {"message": message}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "reply" in data:
            print("Chatbot:", data["reply"])
        else:
            print("⚠️ Error en servidor:", data)
    else:
        print("Error HTTP:", response.status_code, response.text)


if __name__ == "__main__":
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("⚠️ No se encontró la variable GROQ_API_KEY en tu .env")
    else:
        print("✅ API Key cargada desde .env")

    print("Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            break
        send_message(user_input)
