from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


print("usuario.py cargado")

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    correo = Column(String(150), nullable=False)  # podés agregar unique=True más adelante
    id_keycloak = Column(String(255), nullable=False, unique=True)
    id_equipo = Column(Integer, ForeignKey("equipos.id_equipo"))

    equipo = relationship("Equipo", back_populates="usuarios")
    administrador_entrenador = relationship("AdministradorEntrenador", back_populates="usuario")
    jugador = relationship("Jugador", back_populates="usuario")
