import pulsar
import _pulsar
from pulsar.schema import *
import logging
import traceback

from src.modulos.planos.infraestructura.schema.v1.comandos import   \
    ComandoCrearPlano, ComandoEliminarPlano
from src.seedwork.infraestructura import utils
from src.seedwork.aplicacion.evento_handler import ejecutar_evento
from src.modulos.planos.aplicacion.event_handler.crear_plano import CrearPlanoEvent
from src.modulos.planos.aplicacion.event_handler.eliminar_plano import EliminarPlanoEvent


def suscribirse_a_comando_crear_plano(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando-crear-plano-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(ComandoCrearPlano))

        while True:

            mensaje = consumidor.receive()
            print('--------------COMANDO CREAR PLANO')
            print(mensaje.value().data)
            consumidor.acknowledge(mensaje)
            crear_auditoria_evento = CrearPlanoEvent(
                event_payload=mensaje.value().data)

            ejecutar_evento(crear_auditoria_evento, app=app)

        cliente.close()
    except:
        logging.error(
            'ERROR: Suscribiendose al tópico de comando crear plano!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comando_eliminar_plano(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando-eliminar-plano-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(ComandoEliminarPlano))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            eliminar_auditoria_evento = EliminarPlanoEvent(
                event_payload=mensaje.value().data)

            ejecutar_evento(eliminar_auditoria_evento, app=app)

        cliente.close()
    except:
        logging.error(
            'ERROR: Suscribiendose al tópico de comando eliminar plano!')
        traceback.print_exc()
        if cliente:
            cliente.close()
