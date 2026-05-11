from models.calificacion import Calificacion


def crear_calificacion(db, data):

    nueva = Calificacion(
        alumno=data.alumno,
        materia=data.materia,
        calificacion1=data.calificacion1,
        calificacion2=data.calificacion2,
        calificacion3=data.calificacion3
    )

    db.add(nueva)

    db.commit()

    db.refresh(nueva)

    return nueva