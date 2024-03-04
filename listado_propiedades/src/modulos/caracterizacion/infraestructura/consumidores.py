import pulsar
import _pulsar
from pulsar.schema import *
import logging
import traceback

from src.modulos.caracterizacion.infraestructura.schema.v1.comandos import   \
    ComandoActualizarCaract
from src.seedwork.infraestructura import utils
from src.seedwork.aplicacion.evento_handler import ejecutar_evento
from src.modulos.caracterizacion.aplicacion.event_handler.actualizar_caract_comando import ActualizarCaractComando


def suscribirse_a_actualizar_caract_comando(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('actualizar-caracterizacion', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='aeroalpes-sub-comandos', schema=AvroSchema(ComandoActualizarCaract))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            comando = ActualizarCaractComando(
                comando_payload=mensaje.value().data)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
