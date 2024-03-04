from src.seedwork.aplicacion.evento_handler import Evento
from src.seedwork.aplicacion.evento_handler import ejecutar_evento as evento
from src.modulos.caracterizacion.infraestructura.repositorios import RepositorioCaracterizacion
from dataclasses import dataclass
from .base import ActualizarCaractBaseHandler
from src.modulos.caracterizacion.infraestructura.schema.v1.comandos import ComandoActualizarCaractPayload
from src.modulos.caracterizacion.dominio.entidades import Caracterizacion
import uuid
from src.modulos.caracterizacion.dominio.objetos_valor import Status, PropiedadType


@dataclass
class ActualizarCaractComando(Evento):
    comando_payload: ComandoActualizarCaractPayload
    ...


class ActualizarCaractHandler(ActualizarCaractBaseHandler):

    def handle(self, event: ActualizarCaractComando):
        from src.config.db import db

        print('llllllllllllllllllllllllllllll')
        print(event.comando_payload)
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioCaracterizacion.__class__)

        caracterizacion = repositorio.obtener_por_id(
            event.comando_payload.propiedad_id)

        if caracterizacion is not None:
            caracterizacion.status = event.comando_payload.status
            caracterizacion.floors = event.comando_payload.floors
            caracterizacion.zone = event.comando_payload.zone
        else:
            status = None

            if event.comando_payload.status == 'AUDITADO':
                status = Status.AUDITADO
            else:
                status = Status.RECHAZADO

            entidad = Caracterizacion(
                id=str(uuid.uuid4()),
                propiedad_id=event.comando_payload.propiedad_id,
                status=status,
                floors=event.comando_payload.floors,
                zone=event.comando_payload.zone,
                type=PropiedadType.POR_DEFINIR
            )

            repositorio.agregar(entidad)

        db.session.commit()


@evento.register(ActualizarCaractComando)
def ejecutar_conando_actualizar_caract(evento: ActualizarCaractComando, app):
    with app.app_context():
        handler = ActualizarCaractHandler()
        handler.handle(evento)
