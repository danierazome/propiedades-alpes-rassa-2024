from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoCrearAuditoriaPayload(ComandoIntegracion):
    propiedad_id = String()
    correlacion_id = String()
    area_construida = String()
    area_total = String()
    zone = Integer()
    floors = Integer()
    client = String()


class ComandoCrearAuditoria(ComandoIntegracion):
    data = ComandoCrearAuditoriaPayload()


class ComandoEliminarAuditoriaPayload(ComandoIntegracion):
    propiedad_id = String()
    correlacion_id = String()


class ComandoEliminarAuditoria(ComandoIntegracion):
    data = ComandoEliminarAuditoriaPayload()
