from src.seedwork.aplicacion.evento_handler import Evento
from src.seedwork.aplicacion.evento_handler import ejecutar_evento as evento
from src.modulos.audit.infraestructura.repositorios import RepositorioAuditoria
from dataclasses import dataclass
from .base import AuditoriaBaseHandler
from src.modulos.audit.dominio.entidades import Auditoria
from src.modulos.audit.infraestructura.schema.v1.comandos import ComandoCrearAuditoriaPayload
from src.modulos.audit.dominio.eventos import AuditoriaCreada, AuditoriaCreadaFallida
from src.modulos.audit.aplicacion.handlers import HandlerAuditoriaIntegracion


@dataclass
class CrearAuditoria(Evento):
    evento_payload: ComandoCrearAuditoriaPayload
    ...


class CrearAuditoriaHandler(AuditoriaBaseHandler):

    def handle(self, event: CrearAuditoria):
        from src.config.db import db
        print('-------------------------ENTER CREATE AUDITORIA HANDLER')
        print(event.evento_payload.__dict__)

        if event.evento_payload.zone == 100:
            auditoria_creada_evento_fallido = AuditoriaCreadaFallida(
                propiedad_id=event.evento_payload.propiedad_id,
                correlacion_id=event.evento_payload.correlacion_id,
            )
            HandlerAuditoriaIntegracion.handle_auditoria_creada_fallida(
                evento=auditoria_creada_evento_fallido)
        else:
            status_auditoria = None
            repositorio = self.fabrica_repositorio.crear_objeto(
                RepositorioAuditoria.__class__)

            auditoria = repositorio.obtener_por_id_dto(
                event.evento_payload.propiedad_id)

            if auditoria is not None:
                if event.evento_payload.zone > 10 and auditoria.assessment == 'RECHAZADO':
                    auditoria.assessment = 'AUDITADO'
                status_auditoria = auditoria.status
            else:
                auditoria: Auditoria = Auditoria(
                    propiedad_id=event.evento_payload.propiedad_id,
                    client='PLANOS'
                )

                if event.evento_payload.zone > 10:
                    auditoria.auditoria_aprobada()
                else:
                    auditoria.auditoria_rechazada()

                repositorio.agregar(auditoria)
                status_auditoria = auditoria.status.value

            auditoria_creada_evento = AuditoriaCreada(
                propiedad_id=event.evento_payload.propiedad_id,
                correlacion_id=event.evento_payload.correlacion_id,
                area_construida=event.evento_payload.area_construida,
                area_total=event.evento_payload.area_total,
                zone=event.evento_payload.zone,
                floors=event.evento_payload.floors,
                status=status_auditoria
            )

            db.session.commit()
            HandlerAuditoriaIntegracion.handle_auditoria_creada(
                evento=auditoria_creada_evento)


@evento.register(CrearAuditoria)
def ejecutar_evento_crear_auditoria(evento: CrearAuditoria, app=None):
    with app.app_context():
        handler = CrearAuditoriaHandler()
        handler.handle(evento)
