from pydantic import BaseModel
from typing import Optional
from datetime import date


class JugadorBase(BaseModel):
    nombre: str
    id_equipo: Optional[int] = None
    fecha_nacimiento: Optional[date] = None
    posicion: Optional[str] = None
    estado: Optional[str] = None
    altura: Optional[float] = None
    peso: Optional[float] = None
    correo: Optional[str] = None
    celular: Optional[str] = None
    id_usuario: Optional[int] = None


class JugadorCreate(JugadorBase):
    pass


class Jugador(JugadorBase):
    id: int

    class Config:
        orm_mode = True
