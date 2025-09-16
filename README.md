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

## Correrlo con el DOCKER

1. Tener el docker desktop corriendo
2. docker compose -f docker-compose.dev.yml build
3. docker compose -f docker-compose.dev.yml up

2a. docker compose -f docker-compose.dev.yml down
Coorerlo solo cuando hay cambios en el .env o en los archivos docker.

## A partir de ahora — Flujo de trabajo

Cada vez que empieces una nueva funcionalidad:

git checkout develop
git pull origin develop
git checkout -b feat/nombre-funcionalidad



