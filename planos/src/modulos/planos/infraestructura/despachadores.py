import pulsar
from pulsar.schema import *

from .schema.v1.eventos import EventoPlanoCreado, PlanoCreadoPayload
from src.seedwork.infraestructura import utils

from datetime import datetime


def timestamp_now() -> float:
    return datetime.now().timestamp()


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(
            topico, schema=AvroSchema(EventoPlanoCreado))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = PlanoCreadoPayload(
            propiedad_id=evento.propiedad_id,
            area_total=evento.area_total,
            area_construida=evento.area_construida,
            floors=evento.floors,
            zone=evento.zone,
            fecha_creacion=timestamp_now()
        )
        evento_integracion = EventoPlanoCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoPlanoCreado))
