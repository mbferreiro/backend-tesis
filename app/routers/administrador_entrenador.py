from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal

router = APIRouter(
    prefix="/administradores_entrenador",
    tags=["AdministradoresEntrenador"]
)

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📍 GET /administradores_entrenador -> listar todos
@router.get("/", response_model=list[schemas.AdministradorEntrenador])
def listar_administradores(db: Session = Depends(get_db)):
    return db.query(models.AdministradorEntrenador).all()

# 📍 GET /administradores_entrenador/{id} -> obtener uno
@router.get("/{admin_id}", response_model=schemas.AdministradorEntrenador)
def obtener_administrador(admin_id: int, db: Session = Depends(get_db)):
    admin = db.query(models.AdministradorEntrenador).filter(models.AdministradorEntrenador.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador/Entrenador no encontrado")
    return admin

# 📍 POST /administradores_entrenador -> crear
@router.post("/", response_model=schemas.AdministradorEntrenador)
def crear_administrador(admin: schemas.AdministradorEntrenadorCreate, db: Session = Depends(get_db)):
    nuevo = models.AdministradorEntrenador(**admin.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# 📍 PUT /administradores_entrenador/{id} -> actualizar
@router.put("/{admin_id}", response_model=schemas.AdministradorEntrenador)
def actualizar_administrador(admin_id: int, datos: schemas.AdministradorEntrenadorCreate, db: Session = Depends(get_db)):
    admin = db.query(models.AdministradorEntrenador).filter(models.AdministradorEntrenador.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador/Entrenador no encontrado")

    for campo, valor in datos.model_dump().items():
        setattr(admin, campo, valor)

    db.commit()
    db.refresh(admin)
    return admin

# 📍 DELETE /administradores_entrenador/{id} -> eliminar
@router.delete("/{admin_id}")
def eliminar_administrador(admin_id: int, db: Session = Depends(get_db)):
    admin = db.query(models.AdministradorEntrenador).filter(models.AdministradorEntrenador.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador/Entrenador no encontrado")

    db.delete(admin)
    db.commit()
    return {"detail": "Administrador/Entrenador eliminado correctamente"}
