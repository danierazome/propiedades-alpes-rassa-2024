from src.seedwork.aplicacion.evento_handler import Evento
from src.seedwork.aplicacion.evento_handler import ejecutar_evento as evento
from src.modulos.caracterizacion.infraestructura.repositorios import RepositorioCaracterizacion
from dataclasses import dataclass
from .base import ActualizarCaractBaseHandler
from src.modulos.caracterizacion.infraestructura.schema.v1.comandos import ComandoEliminarCaractPayload
from src.modulos.caracterizacion.dominio.entidades import Caracterizacion
import uuid
from src.modulos.caracterizacion.dominio.objetos_valor import Status, PropiedadType
from src.modulos.caracterizacion.dominio.eventos import CaracterizacionEliminado
from src.modulos.caracterizacion.aplicacion.handlers import HandlerCaractIntegracion
from src.modulos.caracterizacion.infraestructura.dto import Caracterizacion as CaracterizacionDTO
from datetime import datetime


@dataclass
class EliminarCaractEvento(Evento):
    event_payload: ComandoEliminarCaractPayload
    ...


class EliminarCaractHandler(ActualizarCaractBaseHandler):

    def handle(self, event: EliminarCaractEvento):
        from src.config.db import db

        print('-------------------------ENTER DELETE CARACTERIZA HANDLER')
        print(event.event_payload.__dict__)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioCaracterizacion.__class__)

        repositorio.eliminar(
            event.event_payload.propiedad_id)

        db.session.commit()

        evento_plano = CaracterizacionEliminado(
            propiedad_id=event.event_payload.propiedad_id,
            correlacion_id=event.event_payload.correlacion_id

        )
        HandlerCaractIntegracion.handle_caract_eliminada(evento_plano)


@evento.register(EliminarCaractEvento)
def ejecutar_conando_crear_caract(evento: EliminarCaractEvento, app):
    with app.app_context():
        handler = EliminarCaractHandler()
        handler.handle(evento)
