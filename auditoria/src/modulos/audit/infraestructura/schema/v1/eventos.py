from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class PlanoCreadoPayload(Record):
    propiedad_id = String()
    area_total = String()
    area_construida = String()
    floors = Integer()
    zone = Integer()


class EventoPlanoCreado(EventoIntegracion):
    data = PlanoCreadoPayload
