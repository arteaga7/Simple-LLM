# Simple-LLM
Simple chatbot with conversational memory implementing FastAPI, SQLModel (Pydantic + SQLAlchemy) and OpenAI libraries (API Key required).


## 🌎 Repository Structure
```
Simple-LLM/
└── main.py             # FastAPI entry point
└── app.py              # Streamlit interface
└── .env                # Contains API Key and system_promt (not provided)
└── requirements.txt
└── img/                # Some pictures
```

## 🚀 How to run
1. Clone this repository:
```
git clone https://github.com/arteaga7/Simple-LLM.git
```
2. Create virtual enviroment and install dependencies (Linux):
```
python3 -m venv env && source env/bin/activate && pip install -r requirements.txt
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
5. Run the interface (client):
```
streamlit run app.py
```

## 🧪 Quick API test
```
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-d '{"message":"Hola, ¿cómo estás?", "session_id":"t1"}'
```

## 🎯 Results
The chatbot is working correctly, responding politely to a greeting or a purchase order, as shwon in figs 1 and 2.
![alt text](<img/f1.png>)
Fig. 1.

![alt text](<img/f2.png>)
Fig. 2.

After saving a purchase order, it is possible to verify the convesational memory, as shown in Fig. 3.

![alt text](<img/f3.png>)
Fig. 3.

## 🗺️ Further work
In order to scale this project, the following step is to add adata base connection to store the conversation and the products information. That project is presented in:

https://github.com/arteaga7/Simple-Agent

