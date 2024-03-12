from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


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
