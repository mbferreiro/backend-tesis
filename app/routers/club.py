from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal

print("club.py cargado")
router = APIRouter(
    prefix="/clubes",
    tags=["Clubes"]
)

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📍 GET /clubes -> listar todos
@router.get("/", response_model=list[schemas.Club])
def listar_clubes(db: Session = Depends(get_db)):
    return db.query(models.Club).all()

# 📍 GET /clubes/{id} -> obtener uno
@router.get("/{club_id}", response_model=schemas.Club)
def obtener_club(club_id: int, db: Session = Depends(get_db)):
    club = db.query(models.Club).filter(models.Club.id_club == club_id).first()
    if not club:
        raise HTTPException(status_code=404, detail="Club no encontrado")
    return club

# 📍 POST /clubes -> crear
@router.post("/", response_model=schemas.Club)
def crear_club(club: schemas.ClubCreate, db: Session = Depends(get_db)):
    nuevo = models.Club(**club.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# 📍 PUT /clubes/{id} -> actualizar
@router.put("/{club_id}", response_model=schemas.Club)
def actualizar_club(club_id: int, datos: schemas.ClubCreate, db: Session = Depends(get_db)):
    club = db.query(models.Club).filter(models.Club.id_club == club_id).first()
    if not club:
        raise HTTPException(status_code=404, detail="Club no encontrado")

    for campo, valor in datos.model_dump().items():
        setattr(club, campo, valor)

    db.commit()
    db.refresh(club)
    return club

# 📍 DELETE /clubes/{id} -> eliminar
@router.delete("/{club_id}")
def eliminar_club(club_id: int, db: Session = Depends(get_db)):
    club = db.query(models.Club).filter(models.Club.id_club == club_id).first()
    if not club:
        raise HTTPException(status_code=404, detail="Club no encontrado")

    db.delete(club)
    db.commit()
    return {"detail": "Club eliminado correctamente"}
