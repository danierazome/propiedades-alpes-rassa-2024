from pulsar.schema import *
from src.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


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
