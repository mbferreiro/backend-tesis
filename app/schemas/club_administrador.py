from pydantic import BaseModel


class ClubAdministradorBase(BaseModel):
    id_club: int
    id_admin: int


class ClubAdministradorCreate(ClubAdministradorBase):
    pass


class ClubAdministrador(ClubAdministradorBase):
    class Config:
        orm_mode = True
