from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoActualizarCaractPayload(ComandoIntegracion):
    propiedad_id = String()
    status = String()
    floors = Integer()
    zone = Integer()


class ComandoActualizarCaract(ComandoIntegracion):
    data = ComandoActualizarCaractPayload()


# PLANOS

class ComandoActualizarPlanoPayload(ComandoIntegracion):
    propiedad_id = String()
    status = String()


class ComandoActualizarPlano(ComandoIntegracion):
    data = ComandoActualizarPlanoPayload()
