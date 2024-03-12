from src.seedwork.aplicacion.evento_handler import Evento
from src.seedwork.aplicacion.evento_handler import ejecutar_evento as evento
from src.modulos.caracterizacion.infraestructura.repositorios import RepositorioCaracterizacion
from dataclasses import dataclass
from .base import ActualizarCaractBaseHandler
from src.modulos.caracterizacion.infraestructura.schema.v1.comandos import ComandoCrearCaractPayload
from src.modulos.caracterizacion.dominio.entidades import Caracterizacion
import uuid
from src.modulos.caracterizacion.dominio.objetos_valor import Status, PropiedadType
from src.modulos.caracterizacion.dominio.eventos import CaracterizacionCreada, CaracterizacionCreadaFallido
from src.modulos.caracterizacion.aplicacion.handlers import HandlerCaractIntegracion
from src.modulos.caracterizacion.infraestructura.dto import Caracterizacion as CaracterizacionDTO
from datetime import datetime


@dataclass
class CrearCaractEvento(Evento):
    event_payload: ComandoCrearCaractPayload
    ...


class CrearCaractHandler(ActualizarCaractBaseHandler):

    def handle(self, event: CrearCaractEvento):
        from src.config.db import db

        print('-------------------------ENTER CREATE CARACTERIZA HANDLER')
        print(event.event_payload.__dict__)

        if event.event_payload.zone == 300:
            evento_plano = CaracterizacionCreadaFallido(
                propiedad_id=event.event_payload.propiedad_id,
                correlacion_id=event.event_payload.correlacion_id
            )
            HandlerCaractIntegracion.handle_caract_creada_fallida(evento_plano)
        else:
            repositorio = self.fabrica_repositorio.crear_objeto(
                RepositorioCaracterizacion.__class__)

            caracterizacion = repositorio.obtener_por_id(
                event.event_payload.propiedad_id)

            if caracterizacion is not None:
                caracterizacion.status = event.event_payload.status
                caracterizacion.floors = event.event_payload.floors
                caracterizacion.zone = event.event_payload.zone
                caracterizacion.fecha_actualizacion = datetime.now()
            else:
                caracterizacion = CaracterizacionDTO(
                    id=str(uuid.uuid4()),
                    propiedad_id=event.event_payload.propiedad_id,
                    fecha_creacion=datetime.now(),
                    fecha_actualizacion=datetime.now(),
                    floors=event.event_payload.floors,
                    zone=event.event_payload.zone,
                    status=event.event_payload.status,
                )
                repositorio.agregar_dto(caracterizacion)

            db.session.commit()

            evento_plano = CaracterizacionCreada(
                propiedad_id=event.event_payload.propiedad_id,
                correlacion_id=event.event_payload.correlacion_id

            )
            HandlerCaractIntegracion.handle_caract_creada(evento_plano)


@evento.register(CrearCaractEvento)
def ejecutar_conando_crear_caract(evento: CrearCaractEvento, app):
    with app.app_context():
        handler = CrearCaractHandler()
        handler.handle(evento)
