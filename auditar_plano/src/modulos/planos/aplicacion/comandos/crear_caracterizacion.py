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
from src.modulos.planos.aplicacion.handlers import HandlerEventosComandos
from src.seedwork.dominio.eventos import EventoDominio


@dataclass
class CrearCaract(Comando):
    evento: EventoDominio


class CrearCaractHandler(ComandoAppBaseHandler):

    def handle(self, comando: CrearCaract):
        print('CREAR CARCTERIZACION HANDLER')
        HandlerEventosComandos.handle_crear_caracterizacion(comando.evento)


@comando.register(CrearCaract)
def ejecutar_comando_crear_caract(comando):
    handler = CrearCaractHandler()
    handler.handle(comando)
