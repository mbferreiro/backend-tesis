from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ClubAdministrador(Base):
    __tablename__ = "club_administrador"

    id_club = Column(Integer, ForeignKey("clubes.id_club"), primary_key=True)
    id_admin = Column(Integer, ForeignKey("administrador_entrenador.id"), primary_key=True)

    club = relationship("Club", back_populates="administradores")
    administrador = relationship("AdministradorEntrenador", back_populates="club_administradores")
