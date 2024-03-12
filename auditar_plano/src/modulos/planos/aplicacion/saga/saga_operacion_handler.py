from src.seedwork.aplicacion.evento_handler import Evento
from src.seedwork.aplicacion.evento_handler import ejecutar_evento as evento
from src.modulos.planos.infraestructura.repositorios import RepositorioSagaLog
from dataclasses import dataclass
from src.modulos.planos.aplicacion.mapeadores import MapeadorAuditoriaPlano
from src.modulos.planos.infraestructura.schema.v1.comandos import ComandoCrearPlanoPayload
from src.modulos.planos.dominio.entidades import Plano
from src.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.seedwork.dominio.eventos import EventoDominio
from src.seedwork.aplicacion.evento_handler import EventHandler
from src.modulos.planos.aplicacion.saga.saga_auditar_planos import CoordinadorAuditoriaPlanos


@dataclass
class SagaOperacionEvento(Evento):
    evento_dominio: EventoDominio


class SagaOperacionHandler(EventHandler):

    def handle(self, event: SagaOperacionEvento):
        from src.config.db import db
        print('-----------SAGA OPERACION HANDLERR')
        print(type(event.evento_dominio))
        print(event.evento_dominio.__dict__)

        coordinador = CoordinadorAuditoriaPlanos()
        coordinador.inicializar_pasos(db=db)
        coordinador.procesar_evento(evento=event.evento_dominio)


@evento.register(SagaOperacionEvento)
def ejecutar_conando_actualizar_plano(evento: SagaOperacionEvento, app):
    with app.app_context():
        handler = SagaOperacionHandler()
        handler.handle(evento)
