from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoActualizarCaractPayload(ComandoIntegracion):
    propiedad_id = String()
    status = String()
    floors = Integer()
    zone = Integer()


class ComandoActualizarCaract(ComandoIntegracion):
    data = ComandoActualizarCaractPayload()
