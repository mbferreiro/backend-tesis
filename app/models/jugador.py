from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Jugador(Base):
    __tablename__ = "jugador"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    id_equipo = Column(Integer, ForeignKey("equipos.id_equipo"))
    fecha_nacimiento = Column(Date)
    posicion = Column(String(60))
    estado = Column(String(15))
    altura = Column(Numeric(5, 2))
    peso = Column(Numeric(5, 2))
    correo = Column(String(150))
    celular = Column(String(30))
    id_usuario = Column(Integer, ForeignKey("usuario.id"))

    equipo = relationship("Equipo", back_populates="jugadores")
    usuario = relationship("Usuario", back_populates="jugador")
