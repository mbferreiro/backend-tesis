from pydantic import BaseModel
from typing import Optional


class EquipoBase(BaseModel):
    nombre: str
    id_club: Optional[int] = None
    nro_telefono: Optional[str] = None
    correo_electronico: Optional[str] = None
    direccion_cancha: Optional[str] = None
    direccion_practicas: Optional[str] = None
    mercado_pago: Optional[str] = None
    cuenta_sistarbanc: Optional[str] = None


class EquipoCreate(EquipoBase):
    pass


class Equipo(EquipoBase):
    id_equipo: int

    class Config:
        orm_mode = True
