import pulsar
import _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.modulos.caracterizacion.infraestructura.schema.v1.comandos import ComandoCrearCaract, \
    ComandoCrearCaractPayload, ComandoEliminarCaract, ComandoEliminarCaractPayload
from src.seedwork.infraestructura import utils
from src.seedwork.aplicacion.evento_handler import ejecutar_evento
from src.modulos.caracterizacion.aplicacion.event_handler.crear_caract import CrearCaractEvento
from src.modulos.caracterizacion.aplicacion.event_handler.eliminar_caract import EliminarCaractEvento


def suscribirse_a_comando_crear_caract(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando-crear-caract-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(ComandoCrearCaract))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            crear_auditoria_evento = CrearCaractEvento(
                event_payload=mensaje.value().data)

            ejecutar_evento(crear_auditoria_evento, app=app)

        cliente.close()
    except:
        logging.error(
            'ERROR: Suscribiendose al tópico de comando crear caract!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comando_eliminar_caract(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando-eliminar-caract-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(ComandoEliminarCaract))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            eliminar_auditoria_evento = EliminarCaractEvento(
                plano_creado_payload=mensaje.value().data)

            ejecutar_evento(eliminar_auditoria_evento, app=app)

        cliente.close()
    except:
        logging.error(
            'ERROR: Suscribiendose al tópico de comando eliminar caract!')
        traceback.print_exc()
        if cliente:
            cliente.close()
