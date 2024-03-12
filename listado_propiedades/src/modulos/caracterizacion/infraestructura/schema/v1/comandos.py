from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoCrearCaractPayload(ComandoIntegracion):
    propiedad_id = String()
    correlacion_id = String()
    zone = Integer()
    floors = Integer()
    status = String()


class ComandoCrearCaract(ComandoIntegracion):
    data = ComandoCrearCaractPayload()


class ComandoEliminarCaractPayload(ComandoIntegracion):
    propiedad_id = String()
    correlacion_id = String()


class ComandoEliminarCaract(ComandoIntegracion):
    data = ComandoEliminarCaractPayload()
