import pulsar
import _pulsar
from pulsar.schema import *
import logging
import traceback

from src.modulos.planos.infraestructura.schema.v1.comandos import   \
    ComandoActualizarPlano
from src.seedwork.infraestructura import utils
from src.seedwork.aplicacion.evento_handler import ejecutar_evento
from src.modulos.planos.aplicacion.event_handler.actualizar_plano_comando import ActualizarPlanoComando


def suscribirse_a_actualizar_plano_comando(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('actualizar-plano', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='aeroalpes-sub-comandos', schema=AvroSchema(ComandoActualizarPlano))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            comando = ActualizarPlanoComando(
                comando_payload=mensaje.value().data)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
