import pulsar
import _pulsar
from pulsar.schema import *
import logging
import traceback

from src.modulos.planos.infraestructura.schema.v1.eventos import EventoAuditoriaCreada, EventoPlanoCreado, \
    EventoCaractCreada, EventoAuditoriaEliminada, EventoPlanoEliminado, EventoCaractEliminado, \
    EventoAuditoriaCreadaFallida, EventoPlanoCreadaFallida, EventoCaractCreadaFallida, \
    EventoTransacionIniciada
from src.modulos.planos.dominio.eventos import AuditoriaCreada, PlanoCreado, CaracterizacionCreada, \
    AuditoriaCreadaFallida, PlanoCreadoFallido, CaracterizacionCreadaFallido, \
    AuditoriaEliminada, PlanoEliminado, CaracterizacionEliminado, TransacionIniciada
from src.seedwork.infraestructura import utils
from src.seedwork.aplicacion.evento_handler import ejecutar_evento
from src.modulos.planos.aplicacion.saga.saga_operacion_handler import SagaOperacionEvento
from src.modulos.planos.aplicacion.saga.saga_compensacion_handler import SagaCompensacionEvento


def suscribirse_a_auditoria_creada_evento(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('auditoria-creado-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(EventoAuditoriaCreada))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            evento_aplicacion = AuditoriaCreada(
                propiedad_id=mensaje.value().data.propiedad_id,
                correlacion_id=mensaje.value().data.correlacion_id,
                area_construida=mensaje.value().data.area_construida,
                area_total=mensaje.value().data.area_total,
                zone=mensaje.value().data.zone,
                floors=mensaje.value().data.floors,
                status=mensaje.value().data.status
            )
            comando = SagaOperacionEvento(
                evento_dominio=evento_aplicacion)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error('EÑOR: Suscribiendose al tópico de auditoria creada')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_plano_creada_evento(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('plano-creado-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(EventoPlanoCreado))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            evento_aplicacion = PlanoCreado(
                propiedad_id=mensaje.value().data.propiedad_id,
                correlacion_id=mensaje.value().data.correlacion_id,
                zone=mensaje.value().data.zone,
                floors=mensaje.value().data.floors,
                status=mensaje.value().data.status
            )
            comando = SagaOperacionEvento(
                evento_dominio=evento_aplicacion)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error('EÑOR: Suscribiendose al tópico de plano creada')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_caract_creada_evento(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('caract-creado-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(EventoCaractCreada))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            evento_aplicacion = CaracterizacionCreada(
                propiedad_id=mensaje.value().data.propiedad_id,
                correlacion_id=mensaje.value().data.correlacion_id
            )
            comando = SagaOperacionEvento(
                evento_dominio=evento_aplicacion)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error(
            'EÑOR: Suscribiendose al tópico de caracterizacion creada')
        traceback.print_exc()
        if cliente:
            cliente.close()


# COMSUMIDORES PARA COMPENSACIONS

def suscribirse_a_auditoria_eliminada_evento(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('auditoria-eliminada-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(EventoAuditoriaEliminada))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            evento_aplicacion = AuditoriaEliminada(
                propiedad_id=mensaje.value().data.propiedad_id,
                correlacion_id=mensaje.value().data.correlacion_id,
            )
            comando = SagaCompensacionEvento(
                evento_dominio=evento_aplicacion)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error('EÑOR: Suscribiendose al tópico de auditoria eliminada')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_plano_eliminada_evento(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('plano-eliminada-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(EventoPlanoEliminado))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            evento_aplicacion = PlanoEliminado(
                propiedad_id=mensaje.value().data.propiedad_id,
                correlacion_id=mensaje.value().data.correlacion_id,
            )
            comando = SagaCompensacionEvento(
                evento_dominio=evento_aplicacion)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error('EÑOR: Suscribiendose al tópico de plano eliminada')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_caract_eliminada_evento(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('caract-eliminada-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(EventoCaractEliminado))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            evento_aplicacion = CaracterizacionEliminado(
                propiedad_id=mensaje.value().data.propiedad_id,
                correlacion_id=mensaje.value().data.correlacion_id,
            )
            comando = SagaCompensacionEvento(
                evento_dominio=evento_aplicacion)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error('EÑOR: Suscribiendose al tópico de caract eliminada')
        traceback.print_exc()
        if cliente:
            cliente.close()


# COMSUMIDORES PARA EVENTOS DE ERROR

def suscribirse_a_auditoria_creada_fallida(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('auditoria-creada-fallida-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(EventoAuditoriaCreadaFallida))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            print('------------- AUDITORIA CREAR FALLLO')
            evento_aplicacion = AuditoriaCreadaFallida(
                propiedad_id=mensaje.value().data.propiedad_id,
                correlacion_id=mensaje.value().data.correlacion_id,
            )
            comando = SagaCompensacionEvento(
                evento_dominio=evento_aplicacion)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error(
            'EÑOR: Suscribiendose al tópico de auditoria creada fallida')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_plano_creada_fallida(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('plano-creada-fallida-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(EventoPlanoCreadaFallida))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            print('------------- PLANO CREAR FALLLO')
            evento_aplicacion = PlanoCreadoFallido(
                propiedad_id=mensaje.value().data.propiedad_id,
                correlacion_id=mensaje.value().data.correlacion_id,
            )
            comando = SagaCompensacionEvento(
                evento_dominio=evento_aplicacion)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error(
            'EÑOR: Suscribiendose al tópico de plano creada fallida')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_caract_creada_fallida(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('caract-creada-fallida-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(EventoCaractCreadaFallida))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            print('------------- CARARCT CREAR FALLLO')

            evento_aplicacion = CaracterizacionCreadaFallido(
                propiedad_id=mensaje.value().data.propiedad_id,
                correlacion_id=mensaje.value().data.correlacion_id,
            )
            comando = SagaCompensacionEvento(
                evento_dominio=evento_aplicacion)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error(
            'EÑOR: Suscribiendose al tópico de caract creada fallida')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_transacion_iniciallizada(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('transacion-inicializada-v1', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='propiedades-alples-miso', schema=AvroSchema(EventoTransacionIniciada))

        while True:
            mensaje = consumidor.receive()
            consumidor.acknowledge(mensaje)
            evento_aplicacion = TransacionIniciada(
                propiedad_id=mensaje.value().data.propiedad_id,
                correlacion_id=mensaje.value().data.correlacion_id,
                zone=mensaje.value().data.zone,
                floors=mensaje.value().data.floors,
                area_construida=mensaje.value().data.area_construida,
                area_total=mensaje.value().data.area_total,
            )
            comando = SagaOperacionEvento(
                evento_dominio=evento_aplicacion)
            ejecutar_evento(comando, app)

        cliente.close()
    except:
        logging.error(
            'EÑOR: Suscribiendose al tópico de transacion inicilizada')
        traceback.print_exc()
        if cliente:
            cliente.close()
