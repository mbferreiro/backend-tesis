from pydantic import BaseModel


class ClubBase(BaseModel):
    nombre: str
    id_admin_creador: int


class ClubCreate(ClubBase):
    pass


class Club(ClubBase):
    id_club: int

    class Config:
        orm_mode = True
