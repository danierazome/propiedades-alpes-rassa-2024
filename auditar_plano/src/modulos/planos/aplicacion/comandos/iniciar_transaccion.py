from src.seedwork.aplicacion.comandos import Comando
from src.modulos.planos.aplicacion.dto import AuditoriaDTO
from .base import ComandoAppBaseHandler
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando

from src.modulos.planos.dominio.entidades import Plano
from src.modulos.planos.aplicacion.dto import AuditoriaDTO
from src.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.modulos.planos.aplicacion.mapeadores import MapeadorAuditoriaPlano
from src.modulos.planos.infraestructura.repositorios import RepositorioSagaLog
from src.seedwork.dominio.excepciones import ExcepcionPlano
from src.seedwork.dominio.eventos import EventoDominio
from src.modulos.planos.aplicacion.dto import AuditoriaDTO
from src.seedwork.aplicacion.evento_handler import ejecutar_evento
from src.modulos.planos.aplicacion.saga.saga_operacion_handler import SagaOperacionEvento
from src.modulos.planos.dominio.eventos import TransacionIniciada
import uuid
from src.modulos.planos.aplicacion.handlers import HandlerEventosComandos


@dataclass
class IniciarTransaccion(Comando):
    transaccion: AuditoriaDTO


class IniciarTransaccionHandler(ComandoAppBaseHandler):

    def handle(self, comando: IniciarTransaccion):
        print('-------------------------ENTER INICIAR TRANSACION HANDLER')
        print(comando.transaccion.__dict__)
        evento_dominio = TransacionIniciada(
            id=str(uuid.uuid4()),
            propiedad_id=comando.transaccion.propiedad_id,
            correlacion_id=str(uuid.uuid4()),
            area_construida=comando.transaccion.area_construida,
            area_total=comando.transaccion.area_total,
            floors=comando.transaccion.floors,
            zone=comando.transaccion.zone
        )
        HandlerEventosComandos.handle_transacion_inicializada(evento_dominio)


@comando.register(IniciarTransaccion)
def ejecutar_comando_crear_plano(comando):
    handler = IniciarTransaccionHandler()
    handler.handle(comando)
