from src.seedwork.aplicacion.evento_handler import Evento
from src.seedwork.aplicacion.evento_handler import ejecutar_evento as evento
from src.modulos.planos.infraestructura.repositorios import RepositorioPlano
from dataclasses import dataclass
from .base import EventHandlerPlanoBaseHandler
from src.modulos.planos.aplicacion.mapeadores import MapeadorPlano
from src.modulos.planos.infraestructura.schema.v1.comandos import ComandoEliminarPlanoPayload
from src.modulos.planos.dominio.entidades import Plano
from src.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.modulos.planos.infraestructura.dto import Plano as PlanoDTO
from datetime import datetime
from src.modulos.planos.dominio.eventos import PlanoEliminado
from src.modulos.planos.aplicacion.handlers import HandlerPlanoIntegracion


@dataclass
class EliminarPlanoEvent(Evento):
    event_payload: ComandoEliminarPlanoPayload
    ...


class EliminarPlanoHandler(EventHandlerPlanoBaseHandler):

    def handle(self, event: EliminarPlanoEvent):
        from src.config.db import db

        print('-------------------------ENTER ELIMINATE PLANO HANDLER')
        print(event.event_payload.__dict__)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPlano.__class__)

        repositorio.eliminar(event.event_payload.propiedad_id)

        db.session.commit()

        evento_plano = PlanoEliminado(
            propiedad_id=event.event_payload.propiedad_id,
            correlacion_id=event.event_payload.correlacion_id

        )
        HandlerPlanoIntegracion.handle_plano_eliminada(evento_plano)


@evento.register(EliminarPlanoEvent)
def ejecutar_conando_eliminar_plano(evento: EliminarPlanoEvent, app):
    with app.app_context():
        handler = EliminarPlanoHandler()
        handler.handle(evento)
