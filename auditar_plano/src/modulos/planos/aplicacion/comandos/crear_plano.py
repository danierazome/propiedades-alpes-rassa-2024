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
class CrearPlano(Comando):
    evento: EventoDominio


class CrearPlanoHandler(ComandoAppBaseHandler):

    def handle(self, comando: CrearPlano):
        print('---------------CREAR PLANO HANDLER')
        print(comando.evento)
        HandlerEventosComandos.handle_crear_plano(comando.evento)


@comando.register(CrearPlano)
def ejecutar_comando_crear_plano(comando):
    handler = CrearPlanoHandler()
    handler.handle(comando)
