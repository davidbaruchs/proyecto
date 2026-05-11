from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from core.database import SessionLocal, engine, Base

from schemas.calificacion import (
    CalificacionCreate,
    CalificacionResponse
)

from crud.calificacion import crear_calificacion

import models.calificacion


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/")
def inicio():

    return {
        "mensaje": "FastAPI funcionando"
    }


@app.post(
    "/calificaciones/",
    response_model=CalificacionResponse
)
def guardar_calificacion(
    data: CalificacionCreate,
    db: Session = Depends(get_db)
):

    nueva = crear_calificacion(db, data)

    return nueva


@app.get("/calificaciones/")
def obtener_calificaciones(
    db: Session = Depends(get_db)
):

    return db.query(
        models.calificacion.Calificacion
    ).all()