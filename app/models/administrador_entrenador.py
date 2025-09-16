from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class AdministradorEntrenador(Base):
    __tablename__ = "administrador_entrenador"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    id_equipo = Column(Integer, ForeignKey("equipos.id_equipo"))
    id_usuario = Column(Integer, ForeignKey("usuario.id"))

    usuario = relationship("Usuario", back_populates="administrador_entrenador")
    equipo = relationship("Equipo", back_populates="administradores_entrenador")
    clubes = relationship("Club", back_populates="admin_creador")
    club_administradores = relationship("ClubAdministrador", back_populates="administrador")
