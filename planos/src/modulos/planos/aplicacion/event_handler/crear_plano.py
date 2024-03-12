import uuid
from src.seedwork.aplicacion.evento_handler import Evento
from src.seedwork.aplicacion.evento_handler import ejecutar_evento as evento
from src.modulos.planos.infraestructura.repositorios import RepositorioPlano
from dataclasses import dataclass
from .base import EventHandlerPlanoBaseHandler
from src.modulos.planos.aplicacion.mapeadores import MapeadorPlano
from src.modulos.planos.infraestructura.schema.v1.comandos import ComandoCrearPlanoPayload
from src.modulos.planos.dominio.entidades import Plano
from src.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.modulos.planos.infraestructura.dto import Plano as PlanoDTO
from datetime import datetime
from src.modulos.planos.aplicacion.handlers import HandlerPlanoIntegracion
from src.modulos.planos.dominio.eventos import PlanoCreado, PlanoCreadoFallido


@dataclass
class CrearPlanoEvent(Evento):
    event_payload: ComandoCrearPlanoPayload
    ...


class CrearPlanoHandler(EventHandlerPlanoBaseHandler):

    def handle(self, event: CrearPlanoEvent):
        from src.config.db import db

        print('-------------------------ENTER CREATE PLANO HANDLER')
        print(event.event_payload)

        if event.event_payload.zone == 200:
            print('-------------------------ENTER CREAR PLANO FALLO')
            evento_plano = PlanoCreadoFallido(
                propiedad_id=event.event_payload.propiedad_id,
                correlacion_id=event.event_payload.correlacion_id
            )
            HandlerPlanoIntegracion.handle_plano_creado_fallida(evento_plano)
        else:
            repositorio = self.fabrica_repositorio.crear_objeto(
                RepositorioPlano.__class__)

            plano = repositorio.obtener_por_propiedad_id(
                event.event_payload.propiedad_id)

            if plano is not None:
                plano.status = event.event_payload.status
                plano.area_total = event.event_payload.area_total
                plano.area_construida = event.event_payload.area_construida
                plano.floors = event.event_payload.floors
                plano.zone = event.event_payload.zone
                plano.fecha_actualizacion = datetime.now()
            else:
                plano = PlanoDTO(
                    id=uuid.uuid4(),
                    propiedad_id=event.event_payload.propiedad_id,
                    fecha_creacion=datetime.now(),
                    fecha_actualizacion=datetime.now(),
                    area_total=event.event_payload.area_total,
                    area_construida=event.event_payload.area_construida,
                    floors=event.event_payload.floors,
                    zone=event.event_payload.zone,
                    status=event.event_payload.status,
                )
                repositorio.agregar_dto(plano)

            db.session.commit()

            evento_plano = PlanoCreado(
                propiedad_id=event.event_payload.propiedad_id,
                correlacion_id=event.event_payload.correlacion_id,
                zone=event.event_payload.zone,
                floors=event.event_payload.floors,
                status=event.event_payload.status

            )
            HandlerPlanoIntegracion.handle_plano_creada(evento_plano)


@evento.register(CrearPlanoEvent)
def ejecutar_conando_crear_plano(evento: CrearPlanoEvent, app):
    with app.app_context():
        handler = CrearPlanoHandler()
        handler.handle(evento)
