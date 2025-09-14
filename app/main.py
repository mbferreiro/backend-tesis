from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, database   # 👈 Import relativo

app = FastAPI(title="Tesis Backend API")

# Permitir que el frontend (localhost:5173) acceda
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crea las tablas si no existen
models.Base.metadata.create_all(bind=database.engine)

# Dependencia para obtener sesión de BD
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Backend Tesis funcionando 🚀"}

# Ejemplo: listar todos los usuarios
@app.get("/usuarios/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()


