from src.seedwork.aplicacion.comandos import Comando
from src.modulos.caracterizacion.aplicacion.dto import CaracterizacionDTO
from .base import CrearCaracterizacionBaseHandler
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando

from src.modulos.caracterizacion.dominio.entidades import Caracterizacion
from src.modulos.caracterizacion.aplicacion.dto import CaracterizacionDTO
from src.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.modulos.caracterizacion.aplicacion.mapeadores import MapeadorCaracterizacion
from src.modulos.caracterizacion.infraestructura.repositorios import RepositorioCaracterizacion


@dataclass
class CrearCaracterizacion(Comando):
    caracterizacionDTO: CaracterizacionDTO


class CrearCaracterizacionHandler(CrearCaracterizacionBaseHandler):

    def handle(self, comando: CrearCaracterizacion):

        caracterizacion: Caracterizacion = self.fabrica_caracterizacion.crear_objeto(
            comando.caracterizacionDTO, MapeadorCaracterizacion())

        caracterizacion.crear_caracterizacion(caracterizacion)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioCaracterizacion.__class__)

        UnidadTrabajoPuerto.registrar_batch(
            repositorio.agregar, caracterizacion)

        UnidadTrabajoPuerto.commit()


@comando.register(CrearCaracterizacion)
def ejecutar_comando_crear_caracterizacion(comando: Caracterizacion):
    handler = CrearCaracterizacionHandler()
    handler.handle(comando)
