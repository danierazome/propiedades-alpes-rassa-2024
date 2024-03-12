from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoCrearPlanoPayload(ComandoIntegracion):
    propiedad_id = String()
    correlacion_id = String()
    area_construida = String()
    area_total = String()
    zone = Integer()
    floors = Integer()
    status = String()


class ComandoCrearPlano(ComandoIntegracion):
    data = ComandoCrearPlanoPayload()


class ComandoEliminarPlanoPayload(ComandoIntegracion):
    propiedad_id = String()
    correlacion_id = String()


class ComandoEliminarPlano(ComandoIntegracion):
    data = ComandoEliminarPlanoPayload()
