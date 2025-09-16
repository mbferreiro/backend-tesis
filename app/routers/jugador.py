from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal

router = APIRouter(
    prefix="/jugadores",
    tags=["Jugadores"]
)

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📍 GET /jugadores -> listar todos
@router.get("/", response_model=list[schemas.Jugador])
def listar_jugadores(db: Session = Depends(get_db)):
    return db.query(models.Jugador).all()

# 📍 GET /jugadores/{id} -> obtener uno
@router.get("/{jugador_id}", response_model=schemas.Jugador)
def obtener_jugador(jugador_id: int, db: Session = Depends(get_db)):
    jugador = db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return jugador

# 📍 POST /jugadores -> crear
@router.post("/", response_model=schemas.Jugador)
def crear_jugador(jugador: schemas.JugadorCreate, db: Session = Depends(get_db)):
    nuevo = models.Jugador(**jugador.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# 📍 PUT /jugadores/{id} -> actualizar
@router.put("/{jugador_id}", response_model=schemas.Jugador)
def actualizar_jugador(jugador_id: int, datos: schemas.JugadorCreate, db: Session = Depends(get_db)):
    jugador = db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")

    for campo, valor in datos.model_dump().items():
        setattr(jugador, campo, valor)

    db.commit()
    db.refresh(jugador)
    return jugador

# 📍 DELETE /jugadores/{id} -> eliminar
@router.delete("/{jugador_id}")
def eliminar_jugador(jugador_id: int, db: Session = Depends(get_db)):
    jugador = db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")

    db.delete(jugador)
    db.commit()
    return {"detail": "Jugador eliminado correctamente"}
