from src.seedwork.aplicacion.comandos import Comando
from src.modulos.planos.aplicacion.dto import AuditoriaDTO
from .base import ComandoAppBaseHandler
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando

from src.seedwork.dominio.eventos import EventoDominio
from src.modulos.planos.aplicacion.handlers import HandlerEventosComandos
from src.seedwork.dominio.eventos import EventoDominio


@dataclass
class CrearAuditoria(Comando):
    evento: EventoDominio


class CrearAuditoriaHandler(ComandoAppBaseHandler):

    def handle(self, comando: CrearAuditoria):
        print('CREAR AUDITORIA HANDLER')
        HandlerEventosComandos.handle_crear_auditoria(comando.evento)


@comando.register(CrearAuditoria)
def ejecutar_comando_crear_auditoria(comando):
    handler = CrearAuditoriaHandler()
    handler.handle(comando)
