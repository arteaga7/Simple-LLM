# Simple-LLM



## 🌎 Repository Structure
```
LLM-FastAPI-SQLModel-PostgreSQL/
└── app/
   └── main.py          # Punto de entrada FastAPI
   └── models.py        # Modelos SQLAlchemy
   └── database.py      # Conexión a PostgreSQL
   └── schemas.py       # Pydantic schemas
   └── crud.py          # Operaciones DB
   └── routes.py        # Endpoints
   └── .env             # Contains all secret data (not provided)
└── requirements.txt
└── Dockerfile
└── docker-compose.yml
└── Documentation
```

## ✨ Details
![alt text](<Documentation/Captura de pantalla 2026-04-23 134002.png>)
Fig. 1.

![alt text](<Documentation/Captura de pantalla 2026-04-23 133918.png>)
Fig. 2.



## 🚀 How to run locally
1. Clone this repository:
```
git clone https://github.com/arteaga7/.git
```
2. 
```
python -m venv env && source env/bin/activate && pip install -r requirements.txt
```

```
uvicorn main:app --reload

```

3. Create your ".env" file, which has the following form:
```
DB_SERVER=10.0.00.00,5000
DB_NAME=My_DataBase
DB_USER=caarteaga
DB_PASSWORD=pa$$word
```
4. Access to the API at "http://localhost:8000".