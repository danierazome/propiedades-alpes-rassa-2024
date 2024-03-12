import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


PDA_HOST = os.getenv("PDA_HOST", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


def obtener_caracterizacion(root) -> typing.List["Caracterizacion"]:
    caracterizaciones_json = requests.get(
        f'http://{PDA_HOST}/caracterizacion/').json()
    caracterizaciones = []

    for caracterizacion in caracterizaciones_json:
        caracterizaciones.append(
            Caracterizacion(
                id=caracterizacion.get('id'),
                propiedad_id=caracterizacion.get('id'),
                fecha_creacion=caracterizacion.get('fecha_creacion'),
                fecha_actualizacion=caracterizacion.get('fecha_actualizacion'),
                floors=caracterizacion.get('floors'),
                zone=caracterizacion.get('zone'),
                type=caracterizacion.get('type'),
                status=caracterizacion.get('status')
            )
        )

    return caracterizaciones


@strawberry.type
class PlanosRespuesta:
    mensaje: str
    codigo: int


@strawberry.type
class Caracterizacion:
    id: str
    propiedad_id: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    floors: int
    zone: int
    type: str
    status: str
