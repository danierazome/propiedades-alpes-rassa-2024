from src.seedwork.aplicacion.evento_handler import Evento
from src.seedwork.aplicacion.evento_handler import ejecutar_evento as evento
from src.modulos.planos.infraestructura.repositorios import RepositorioSagaLog
from dataclasses import dataclass
from .base import ActualizarPlanoBaseHandler
from src.modulos.planos.aplicacion.mapeadores import MapeadorAuditoriaPlano
from src.modulos.planos.infraestructura.schema.v1.comandos import ComandoCrearPlanoPayload
from src.modulos.planos.dominio.entidades import Plano
from src.seedwork.infraestructura.uow import UnidadTrabajoPuerto


@dataclass
class ActualizarPlanoComando(Evento):
    comando_payload: ComandoCrearPlanoPayload
    ...


class ActualizarPlanoHandler(ActualizarPlanoBaseHandler):

    def handle(self, event: ActualizarPlanoComando):
        from src.config.db import db

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioSagaLog.__class__)

        plano = repositorio.obtener_por_propiedad_id(
            event.comando_payload.propiedad_id)

        if plano is not None:
            plano.status = event.comando_payload.status
            db.session.commit()


@evento.register(ActualizarPlanoComando)
def ejecutar_conando_actualizar_plano(evento: ActualizarPlanoComando, app):
    with app.app_context():
        handler = ActualizarPlanoHandler()
        handler.handle(evento)
