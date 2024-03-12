from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class AuditoriaCreadaPayload(Record):
    propiedad_id = String()
    correlacion_id = String()
    area_construida = String()
    area_total = String()
    zone = Integer()
    floors = Integer()
    status = String()


class EventoAuditoriaCreada(EventoIntegracion):
    data = AuditoriaCreadaPayload()
#####


class AuditoriaCreadaFallidaPayload(Record):
    propiedad_id = String()
    correlacion_id = String()


class EventoAuditoriaCreadaFallida(EventoIntegracion):
    data = AuditoriaCreadaFallidaPayload()
#####


class AuditoriaEliminadaPayload(Record):
    propiedad_id = String()
    correlacion_id = String()


class EventoAuditoriaEliminada(EventoIntegracion):
    data = AuditoriaEliminadaPayload()
