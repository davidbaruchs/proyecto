from pydantic import BaseModel


class CalificacionCreate(BaseModel):
    alumno: str
    materia: str
    calificacion1: float
    calificacion2: float
    calificacion3: float


class CalificacionResponse(CalificacionCreate):
    id: int

    class Config:
        from_attributes = True
        from_attributes = True
        from_attributes = True
        from_attributes = True