from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Tesis Backend API")

# Permitir que el frontend (localhost:5173) acceda
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend Tesis funcionando 🚀"}
