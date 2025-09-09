# Backend Tesis
API backend desarrollada con FastAPI para el proyecto de tesis.

## Cómo correrlo

1. Crear un entorno virtual e instalar dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows

   pip install -r requirements.txt

2. Levantar el servidor:

uvicorn app.main:app --reload