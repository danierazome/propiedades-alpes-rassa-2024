import pulsar
from pulsar.schema import *

from src.modulos.audit.infraestructura.schema.v1.eventos import AuditoriaCreadaPayload, \
    EventoAuditoriaCreada, AuditoriaCreadaFallidaPayload, EventoAuditoriaCreadaFallida, \
    AuditoriaEliminadaPayload, EventoAuditoriaEliminada
from src.seedwork.infraestructura import utils


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(
            topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento_auditoria_creada(self, evento, topico):
        payload = AuditoriaCreadaPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id,
            area_construida=evento.area_construida,
            area_total=evento.area_total,
            zone=evento.zone,
            floors=evento.floors,
            status=evento.status
        )
        evento_integracion = EventoAuditoriaCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoAuditoriaCreada))

    def publicar_evento_auditoria_eliminada(self, evento, topico):
        payload = AuditoriaEliminadaPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id
        )
        evento_integracion = EventoAuditoriaEliminada(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoAuditoriaEliminada))

    def publicar_evento_auditoria_creada_fallida(self, evento, topico):
        payload = AuditoriaCreadaFallidaPayload(
            propiedad_id=evento.propiedad_id,
            correlacion_id=evento.correlacion_id
        )
        evento_integracion = EventoAuditoriaCreadaFallida(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoAuditoriaCreadaFallida))
