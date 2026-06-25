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
SYSTEM_PROMPT = "Eres un asistente experto en programación y muy útil."
```
4. Run "main.py" with:
```
uvicorn main:app --reload
```
5. Run Python client "client.py".