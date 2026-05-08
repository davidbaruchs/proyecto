from pydantic import Basemodel

class calificacionCreate(Basemodel):
    alumno: str
    materia: str
    calificacion: float


class calificacionResponse(calificacionCreate):
     id: int


     class config:
          orm_mode =  True
          