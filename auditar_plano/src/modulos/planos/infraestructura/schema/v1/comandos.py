from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)

# AUDITORIA


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

# PLANOS


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

# CARACTERIZACION


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
