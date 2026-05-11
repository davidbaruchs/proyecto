from sqlalchemy import Column, Integer, String, Float

from core.database import Base


class Calificacion(Base):

    __tablename__ = "calificaciones"

    id = Column(Integer, primary_key=True, index=True)

    alumno = Column(String(100))

    materia = Column(String(100))

    calificacion1 = Column(Float)

    calificacion2 = Column(Float)

    calificacion3 = Column(Float)