import pulsar
from pulsar.schema import *

from .schema.v1.eventos import EventoPlanoCreado, PlanoCreadoPayload, \
    PlanoEliminadoPayload, EventoPlanoEliminado, EventoPlanoCreadaFallida, PlanoCreadaFallidaPayload
from src.seedwork.infraestructura import utils

from datetime import datetime


def timestamp_now() -> float:
    return datetime.now().timestamp()


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(
            topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_plano_creada(self, evento, topico):
        payload = PlanoCreadoPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id,
            zone=evento.zone,
            floors=evento.floors,
            status=evento.status
        )
        evento_integracion = EventoPlanoCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoPlanoCreado))

    def publicar_evento_plano_eliminada(self, evento, topico):
        payload = PlanoEliminadoPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id
        )
        evento_integracion = EventoPlanoEliminado(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoPlanoEliminado))

    def publicar_evento_plano_creada_fallida(self, evento, topico):
        payload = PlanoCreadaFallidaPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id
        )
        evento_integracion = EventoPlanoCreadaFallida(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoPlanoCreadaFallida))
