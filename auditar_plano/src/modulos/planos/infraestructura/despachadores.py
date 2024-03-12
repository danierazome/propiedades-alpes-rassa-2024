import pulsar
from pulsar.schema import *

from .schema.v1.eventos import TransacionIniciadaPayload, EventoTransacionIniciada
from .schema.v1.comandos import ComandoCrearAuditoria, ComandoCrearAuditoriaPayload,  \
    ComandoCrearPlano, ComandoCrearPlanoPayload, \
    ComandoCrearCaract, ComandoCrearCaractPayload, \
    ComandoEliminarAuditoria, ComandoEliminarAuditoriaPayload, \
    ComandoEliminarPlano, ComandoEliminarPlanoPayload, \
    ComandoEliminarCaract, ComandoEliminarCaractPayload
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

    def publicar_comando_crear_auditoria(self, evento, topico):
        payload = ComandoCrearAuditoriaPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id,
            area_total=evento.area_total,
            area_construida=evento.area_construida,
            floors=evento.floors,
            zone=evento.zone
        )
        comando_integracion = ComandoCrearAuditoria(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoCrearAuditoria))

    def publicar_comando_crear_plano(self, evento, topico):
        payload = ComandoCrearPlanoPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id,
            area_total=evento.area_total,
            area_construida=evento.area_construida,
            floors=evento.floors,
            zone=evento.zone,
            status=evento.status
        )
        print('------------publicar crear planop')
        print(payload.__dict__)
        comando_integracion = ComandoCrearPlano(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoCrearPlano))

    def publicar_comando_crear_caract(self, evento, topico):
        payload = ComandoCrearCaractPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id,
            floors=evento.floors,
            zone=evento.zone,
            status=evento.status
        )
        comando_integracion = ComandoCrearCaract(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoCrearCaract))
# ELIMINAR

    def publicar_comando_eliminar_auditoria(self, evento, topico):
        payload = ComandoEliminarAuditoriaPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id
        )
        print('------------- ELIMINAR AUDITORIA')
        comando_integracion = ComandoEliminarAuditoria(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoEliminarAuditoria))

    def publicar_comando_eliminar_plano(self, evento, topico):
        payload = ComandoEliminarPlanoPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id
        )
        print('------------- ELIMINAR PLANO')

        comando_integracion = ComandoEliminarPlano(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoEliminarPlano))

    def publicar_comando_eliminar_caract(self, evento, topico):
        payload = ComandoEliminarCaractPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id
        )
        print('------------- ELIMINAR CARACT')

        comando_integracion = ComandoEliminarCaract(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoEliminarCaract))

    # TRANSACION INICIALIZADA
    def publicar_evento_transacion_inicializada(self, evento, topico):
        payload = TransacionIniciadaPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id,
            area_total=evento.area_total,
            area_construida=evento.area_construida,
            floors=evento.floors,
            zone=evento.zone
        )
        print('------------iniciador payload')
        print(payload.__dict__)
        comando_integracion = EventoTransacionIniciada(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(EventoTransacionIniciada))
