from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Equipo(Base):
    __tablename__ = "equipos"

    id_equipo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    id_club = Column(Integer, ForeignKey("clubes.id_club"))
    nro_telefono = Column(String(30))
    correo_electronico = Column(String(150))
    direccion_cancha = Column(String(255))
    direccion_practicas = Column(String(255))
    mercado_pago = Column(String(150))
    cuenta_sistarbanc = Column(String(100))

    club = relationship("Club", back_populates="equipos")
    usuarios = relationship("Usuario", back_populates="equipo")
    administradores_entrenador = relationship("AdministradorEntrenador", back_populates="equipo")
    jugadores = relationship("Jugador", back_populates="equipo")
