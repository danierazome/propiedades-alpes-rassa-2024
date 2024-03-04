import pulsar
import _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.modulos.audit.infraestructura.schema.v1.eventos import EventoPlanoCreado
from src.seedwork.infraestructura import utils
from src.seedwork.aplicacion.evento_handler import ejecutar_evento
from src.modulos.audit.aplicacion.event_handler.plano_creado_event import PlanoCreadoEvento


def suscribirse_a_eventos(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('evento-plano-creado', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(EventoPlanoCreado))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            plano_creado_evento = PlanoCreadoEvento(
                plano_creado_payload=mensaje.value().data)

            ejecutar_evento(plano_creado_evento, app=app)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


# def suscribirse_a_comandos():
#     cliente = None
#     try:
#         cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
#         consumidor = cliente.subscribe('comandos-reserva', consumer_type=_pulsar.ConsumerType.Shared,
#                                        subscription_name='aeroalpes-sub-comandos', schema=AvroSchema(ComandoCrearReserva))

#         while True:
#             mensaje = consumidor.receive()
#             print(f'Comando recibido: {mensaje.value().data}')

#             consumidor.acknowledge(mensaje)

#         cliente.close()
#     except:
#         logging.error('ERROR: Suscribiendose al tópico de comandos!')
#         traceback.print_exc()
#         if cliente:
#             cliente.close()
