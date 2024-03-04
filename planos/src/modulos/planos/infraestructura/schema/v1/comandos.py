from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoActualizarPlanoPayload(ComandoIntegracion):
    propiedad_id = String()
    status = String()


class ComandoActualizarPlano(ComandoIntegracion):
    data = ComandoActualizarPlanoPayload()
