from sqlalchemy import Column, Integer, String, Text, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base   

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    correo = Column(String(150), nullable=False)  # podés agregar unique=True más adelante
    contrasenia = Column(Text, nullable=False)    # guarda hash, no texto plano
    id_equipo = Column(Integer, ForeignKey("equipos.id_equipo"))

    equipo = relationship("Equipo", back_populates="usuarios")
    administrador_entrenador = relationship("AdministradorEntrenador", back_populates="usuario")
    jugador = relationship("Jugador", back_populates="usuario")


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


class Club(Base):
    __tablename__ = "clubes"

    id_club = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    id_admin_creador = Column(Integer, ForeignKey("administrador_entrenador.id"), nullable=False)

    admin_creador = relationship("AdministradorEntrenador", back_populates="clubes")
    equipos = relationship("Equipo", back_populates="club")
    administradores = relationship("ClubAdministrador", back_populates="club")


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


class ClubAdministrador(Base):
    __tablename__ = "club_administrador"

    id_club = Column(Integer, ForeignKey("clubes.id_club"), primary_key=True)
    id_admin = Column(Integer, ForeignKey("administrador_entrenador.id"), primary_key=True)

    club = relationship("Club", back_populates="administradores")
    administrador = relationship("AdministradorEntrenador", back_populates="club_administradores")


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
