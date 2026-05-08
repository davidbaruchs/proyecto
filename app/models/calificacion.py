from sqlalchemy import column, integer, string, float
from database import base

class calificacion(base):
    __tablename__ = "calificacion"

    id = column(integer, primary_key=True, index=True )
    alumno = column(string, index=True)
    materia = column(string)
    calificacion = column(float)