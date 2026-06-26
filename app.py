import os
import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


def send_message(message: str):
    url = "http://127.0.0.1:8000/chat"
    payload = {"message": message}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "reply" in data:
            reply = data["reply"]
            # Guardamos en historial
            st.session_state["chat_history"].append(("Usuario", message))
            st.session_state["chat_history"].append(("Chatbot", reply))
        else:
            st.error("⚠️ Error en servidor")
    else:
        st.error(f"⚠️ Error HTTP {response.status_code}")


# Inicializar historial si no existe
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.set_page_config(
    page_title="Chatbot Pedidos",
    page_icon="🛒",
    layout="centered"
)
st.title("💬 Chatbot de pedidos")
st.subheader("Haga sus pedidos")

# Input primero
user_input = st.chat_input("Escribe tu pedido:")
if user_input:
    send_message(user_input)

# Mostrar historial después de procesar input
for sender, text in st.session_state["chat_history"]:
    if sender == "Usuario":
        with st.chat_message("user", avatar="🧑"):
            st.markdown(text)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(text)
