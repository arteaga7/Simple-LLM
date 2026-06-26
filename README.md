# Simple-LLM



## 🌎 Repository Structure
```
Simple-LLM/
└── main.py          # Punto de entrada FastAPI
└── client.py        # Script para chatear
└── .env             # Contains all secret data (not provided)
└── requirements.txt
```

## ✨ Details
![alt text](<Documentation/Captura de pantalla 2026-04-23 134002.png>)
Fig. 1.

![alt text](<Documentation/Captura de pantalla 2026-04-23 133918.png>)
Fig. 2.



## 🚀 How to run locally
1. Clone this repository:
```
git clone https://github.com/arteaga7/Simple-LLM.git
```
2. Create virtual enviroment and install dependencies (Linux):
```
python -m venv env && source env/bin/activate && pip install -r requirements.txt
```
3. Create your ".env" file, whith the following content:
```
GROQ_API_KEY=your_API_Key
SYSTEM_PROMPT = "Eres un chatbot que valida los precios y productos del usuario contra la lista del proveedor y responde brevemente si hay discrepancias. Si el precio o producto no coincide con la lista del proveedor, detalla brevemente cuál es el error en la solicitud. Si el producto solicitado por el cliente no está en la lista del proveedor, responde textualmente: 'Disculpa, no tengo ese producto'. Tu nombre es Sebastián, proporcíonalo al usuario solamente si te lo pregunta."
```
4. Run "main.py" with:
```
uvicorn main:app --reload
```
5. Run the interface (Python client):
```
streamlit run app.py
```