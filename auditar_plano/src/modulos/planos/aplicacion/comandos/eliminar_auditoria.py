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
from src.modulos.planos.aplicacion.handlers import HandlerEventosComandos
from src.seedwork.dominio.eventos import EventoDominio


@dataclass
class EliminarAuditoria(Comando):
    evento: EventoDominio


class EliminarAuditoriaHandler(ComandoAppBaseHandler):

    def handle(self, comando: EliminarAuditoria):
        print('ELIMINAR AUDITORIA HANDLER')
        HandlerEventosComandos.handle_eliminar_auditoria(comando.evento)


@comando.register(EliminarAuditoria)
def ejecutar_comando_eliminar_auditoria(comando):
    handler = EliminarAuditoriaHandler()
    handler.handle(comando)
