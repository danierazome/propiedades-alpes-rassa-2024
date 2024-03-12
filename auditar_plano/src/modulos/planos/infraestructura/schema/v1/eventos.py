from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class TransacionIniciadaPayload(Record):
    propiedad_id = String()
    correlacion_id = String()
    area_construida = String()
    area_total = String()
    zone = Integer()
    floors = Integer()


class EventoTransacionIniciada(EventoIntegracion):
    data = TransacionIniciadaPayload()


# AUDITORIA
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

# PLANOS


class PlanoCreadoPayload(Record):
    propiedad_id = String()
    correlacion_id = String()
    zone = Integer()
    floors = Integer()
    status = String()


class EventoPlanoCreado(EventoIntegracion):
    data = PlanoCreadoPayload()
#####


class PlanoCreadaFallidaPayload(Record):
    propiedad_id = String()
    correlacion_id = String()


class EventoPlanoCreadaFallida(EventoIntegracion):
    data = PlanoCreadaFallidaPayload()
#####


class PlanoEliminadoPayload(Record):
    propiedad_id = String()
    correlacion_id = String()


class EventoPlanoEliminado(EventoIntegracion):
    data = PlanoEliminadoPayload()

# CARACTERIZACION


class CaractCreadoPayload(Record):
    propiedad_id = String()
    correlacion_id = String()
    zone = Integer()
    floors = Integer()
    status = String()


class EventoCaractCreada(EventoIntegracion):
    data = CaractCreadoPayload()

#####


class CaractCreadaFallidaPayload(Record):
    propiedad_id = String()
    correlacion_id = String()


class EventoCaractCreadaFallida(EventoIntegracion):
    data = CaractCreadaFallidaPayload()
#####


class CaractEliminadoPayload(Record):
    propiedad_id = String()
    correlacion_id = String()


class EventoCaractEliminado(EventoIntegracion):
    data = CaractEliminadoPayload()
