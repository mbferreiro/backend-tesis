from pydantic import BaseModel
from typing import Optional


class AdministradorEntrenadorBase(BaseModel):
    nombre: str
    id_equipo: Optional[int] = None
    id_usuario: Optional[int] = None


class AdministradorEntrenadorCreate(AdministradorEntrenadorBase):
    pass


class AdministradorEntrenador(AdministradorEntrenadorBase):
    id: int

    class Config:
        orm_mode = True
