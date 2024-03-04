from src.seedwork.aplicacion.evento_handler import Evento
from src.seedwork.aplicacion.evento_handler import ejecutar_evento as evento
from src.modulos.audit.infraestructura.repositorios import RepositorioAuditoria
from dataclasses import dataclass
from .base import PlanoCreadoBaseHandler
from src.modulos.audit.aplicacion.mapeadores import MapeadorAuditoria
from src.modulos.audit.infraestructura.schema.v1.eventos import PlanoCreadoPayload
from src.modulos.audit.dominio.entidades import Auditoria
from src.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.modulos.audit.infraestructura.schema.v1.eventos import PlanoCreadoPayload
from src.modulos.audit.dominio.eventos import ActualizarCaracterizacion, ActualizarPlano
from pydispatch import dispatcher
from src.modulos.audit.aplicacion.handlers import HandlerAuditoriaIntegracion
import random


@dataclass
class PlanoCreadoEvento(Evento):
    plano_creado_payload: PlanoCreadoPayload
    ...


class PlanoCreadoHandler(PlanoCreadoBaseHandler):

    def handle(self, event: PlanoCreadoEvento):
        from src.config.db import db

        auditoria: Auditoria = Auditoria(
            propiedad_id=event.plano_creado_payload.propiedad_id,
            client='PLANOS'
        )

        if event.plano_creado_payload.zone > 10:
            auditoria.auditoria_aprobada()

            actualizar_caract_comando = self.create_actualizar_caract_comando(
                auditoria, event.plano_creado_payload)
            HandlerAuditoriaIntegracion.handle_actualizar_caracterizacion(
                actualizar_caract_comando)

        else:
            auditoria.auditoria_rechazada()

        actualizar_plano_comando = self.create_actualizar_plano_comando(
            auditoria)
        HandlerAuditoriaIntegracion.handle_actualizar_plano(
            actualizar_plano_comando)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioAuditoria.__class__)

        repositorio.agregar(auditoria)

        db.session.commit()

    def create_actualizar_plano_comando(self, entidad: Auditoria) -> ActualizarPlano:
        return ActualizarPlano(
            propiedad_id=entidad.propiedad_id,
            status=entidad.status.value
        )

    def create_actualizar_caract_comando(self, entidad: Auditoria, evento: PlanoCreadoPayload) -> ActualizarCaracterizacion:
        return ActualizarCaracterizacion(
            propiedad_id=entidad.propiedad_id,
            status=entidad.status.value,
            floors=evento.floors,
            zone=evento.zone
        )


@evento.register(PlanoCreadoEvento)
def ejecutar_evento_plano_creado(evento: PlanoCreadoEvento, app=None):
    with app.app_context():
        handler = PlanoCreadoHandler()
        handler.handle(evento)
