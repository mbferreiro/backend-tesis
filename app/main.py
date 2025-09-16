from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, database


from app.routers import (
    usuario,
    jugador,
    equipo,
    club,
    club_administrador,
    administrador_entrenador
)




# Crea las tablas si no existen
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Tesis Backend API")

# Permitir que el frontend (localhost:5173) acceda
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener sesión de BD
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🏠 Rutas base
# --------------
@app.get("/")
def root():
    return {"message": "Backend Tesis funcionando 🚀"}

# Registrar routers
app.include_router(usuario.router)
app.include_router(jugador.router)
app.include_router(equipo.router)
app.include_router(club.router)
app.include_router(club_administrador.router)
app.include_router(administrador_entrenador.router)

