from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal

print("club_administrador.py cargado")
router = APIRouter(
    prefix="/club_administradores",
    tags=["ClubAdministradores"]
)

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 📍 GET /club_administradores -> listar todos
@router.get("/", response_model=list[schemas.ClubAdministrador])
def listar_club_administradores(db: Session = Depends(get_db)):
    return db.query(models.ClubAdministrador).all()


# 📍 GET /club_administradores/{id_club}/{id_admin} -> obtener uno
@router.get("/{id_club}/{id_admin}", response_model=schemas.ClubAdministrador)
def obtener_club_administrador(id_club: int, id_admin: int, db: Session = Depends(get_db)):
    ca = db.query(models.ClubAdministrador).filter(
        models.ClubAdministrador.id_club == id_club,
        models.ClubAdministrador.id_admin == id_admin
    ).first()
    if not ca:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    return ca


# 📍 POST /club_administradores -> crear
@router.post("/", response_model=schemas.ClubAdministrador)
def crear_club_administrador(datos: schemas.ClubAdministradorCreate, db: Session = Depends(get_db)):
    nuevo = models.ClubAdministrador(**datos.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


# 📍 DELETE /club_administradores/{id_club}/{id_admin} -> eliminar
@router.delete("/{id_club}/{id_admin}")
def eliminar_club_administrador(id_club: int, id_admin: int, db: Session = Depends(get_db)):
    ca = db.query(models.ClubAdministrador).filter(
        models.ClubAdministrador.id_club == id_club,
        models.ClubAdministrador.id_admin == id_admin
    ).first()
    if not ca:
        raise HTTPException(status_code=404, detail="Relación no encontrada")

    db.delete(ca)
    db.commit()
    return {"detail": "Relación eliminada correctamente"}
