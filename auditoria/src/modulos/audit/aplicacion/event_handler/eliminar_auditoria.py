from src.seedwork.aplicacion.evento_handler import Evento
from src.seedwork.aplicacion.evento_handler import ejecutar_evento as evento
from src.modulos.audit.infraestructura.repositorios import RepositorioAuditoria
from dataclasses import dataclass
from .base import AuditoriaBaseHandler
from src.modulos.audit.aplicacion.mapeadores import MapeadorAuditoria
from src.modulos.audit.dominio.entidades import Auditoria
from src.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.modulos.audit.infraestructura.schema.v1.comandos import ComandoEliminarAuditoriaPayload
from src.modulos.audit.dominio.eventos import AuditoriaEliminada
from pydispatch import dispatcher
from src.modulos.audit.aplicacion.handlers import HandlerAuditoriaIntegracion
import random


@dataclass
class EliminarAuditoria(Evento):
    evento_payload: ComandoEliminarAuditoriaPayload
    ...


class EliminarAuditoriaHandler(AuditoriaBaseHandler):

    def handle(self, event: EliminarAuditoria):
        from src.config.db import db

        print('-------------------------ENTER ELIMINATE AUDITORIA HANDLER')

        print(event.evento_payload.__dict__)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioAuditoria.__class__)
        repositorio.eliminar(event.evento_payload.propiedad_id)

        auditoria_eliminada_evento = AuditoriaEliminada(
            propiedad_id=event.evento_payload.propiedad_id,
            correlacion_id=event.evento_payload.correlacion_id
        )

        db.session.commit()
        HandlerAuditoriaIntegracion.handle_auditoria_eliminada(
            evento=auditoria_eliminada_evento)


@evento.register(EliminarAuditoria)
def ejecutar_evento_elilminar_auditoria(evento: EliminarAuditoria, app=None):
    with app.app_context():
        handler = EliminarAuditoriaHandler()
        handler.handle(evento)
