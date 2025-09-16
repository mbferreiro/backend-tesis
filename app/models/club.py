from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Club(Base):
    __tablename__ = "clubes"

    id_club = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    id_admin_creador = Column(Integer, ForeignKey("administrador_entrenador.id"), nullable=False)

    admin_creador = relationship("AdministradorEntrenador", back_populates="clubes")
    equipos = relationship("Equipo", back_populates="club")
    administradores = relationship("ClubAdministrador", back_populates="club")
