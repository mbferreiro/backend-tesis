from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal

print("equipo.py cargado")
router = APIRouter(
    prefix="/equipos",
    tags=["Equipos"]
)

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📍 GET /equipos -> listar todos
@router.get("/", response_model=list[schemas.Equipo])
def listar_equipos(db: Session = Depends(get_db)):
    return db.query(models.Equipo).all()

# 📍 GET /equipos/{id} -> obtener uno
@router.get("/{equipo_id}", response_model=schemas.Equipo)
def obtener_equipo(equipo_id: int, db: Session = Depends(get_db)):
    equipo = db.query(models.Equipo).filter(models.Equipo.id_equipo == equipo_id).first()
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo

# 📍 POST /equipos -> crear
@router.post("/", response_model=schemas.Equipo)
def crear_equipo(equipo: schemas.EquipoCreate, db: Session = Depends(get_db)):
    nuevo = models.Equipo(**equipo.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# 📍 PUT /equipos/{id} -> actualizar
@router.put("/{equipo_id}", response_model=schemas.Equipo)
def actualizar_equipo(equipo_id: int, datos: schemas.EquipoCreate, db: Session = Depends(get_db)):
    equipo = db.query(models.Equipo).filter(models.Equipo.id_equipo == equipo_id).first()
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")

    for campo, valor in datos.model_dump().items():
        setattr(equipo, campo, valor)

    db.commit()
    db.refresh(equipo)
    return equipo

# 📍 DELETE /equipos/{id} -> eliminar
@router.delete("/{equipo_id}")
def eliminar_equipo(equipo_id: int, db: Session = Depends(get_db)):
    equipo = db.query(models.Equipo).filter(models.Equipo.id_equipo == equipo_id).first()
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")

    db.delete(equipo)
    db.commit()
    return {"detail": "Equipo eliminado correctamente"}
