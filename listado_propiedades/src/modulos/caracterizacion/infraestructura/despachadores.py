import pulsar
from pulsar.schema import *

from src.modulos.caracterizacion.infraestructura.schema.v1.eventos import CaractCreadoPayload, \
    EventoCaractCreada, CaractCreadaFallidaPayload, EventoCaractCreadaFallida, \
    CaractEliminadoPayload, EventoCaractEliminado
from src.seedwork.infraestructura import utils


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(
            topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_caract_creada(self, evento, topico):
        payload = CaractCreadoPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id,
        )
        evento_integracion = EventoCaractCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoCaractCreada))

    def publicar_evento_caract_eliminada(self, evento, topico):
        payload = CaractEliminadoPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id
        )
        evento_integracion = EventoCaractEliminado(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoCaractEliminado))

    def publicar_evento_caract_creada_fallida(self, evento, topico):
        payload = CaractCreadaFallidaPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id
        )
        evento_integracion = EventoCaractCreadaFallida(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoCaractCreadaFallida))
