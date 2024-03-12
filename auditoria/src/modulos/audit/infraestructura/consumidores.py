import pulsar
import _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.modulos.audit.infraestructura.schema.v1.comandos import ComandoCrearAuditoria, \
    ComandoCrearAuditoriaPayload, ComandoEliminarAuditoria, ComandoEliminarAuditoriaPayload
from src.seedwork.infraestructura import utils
from src.seedwork.aplicacion.evento_handler import ejecutar_evento
from src.modulos.audit.aplicacion.event_handler.crear_auditoria import CrearAuditoria
from src.modulos.audit.aplicacion.event_handler.eliminar_auditoria import EliminarAuditoria


def suscribirse_a_comando_crear_auditoria(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando-crear-auditoria-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(ComandoCrearAuditoria))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            crear_auditoria_evento = CrearAuditoria(
                evento_payload=mensaje.value().data)

            ejecutar_evento(crear_auditoria_evento, app=app)

        cliente.close()
    except:
        logging.error(
            'ERROR: Suscribiendose al tópico de comando crear auditoria!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comando_eliminar_auditoria(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando-eliminar-auditoria-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(ComandoEliminarAuditoria))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            eliminar_auditoria_evento = EliminarAuditoria(
                evento_payload=mensaje.value().data)

            ejecutar_evento(eliminar_auditoria_evento, app=app)

        cliente.close()
    except:
        logging.error(
            'ERROR: Suscribiendose al tópico de comando eliminar auditoria!')
        traceback.print_exc()
        if cliente:
            cliente.close()
