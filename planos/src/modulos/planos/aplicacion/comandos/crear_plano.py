from src.seedwork.aplicacion.comandos import Comando
from src.modulos.planos.aplicacion.dto import PlanoDTO
from .base import CrearPlanoBaseHandler
from dataclasses import dataclass
from src.seedwork.aplicacion.comandos import ejecutar_commando as comando

from src.modulos.planos.dominio.entidades import Plano
from src.modulos.planos.aplicacion.dto import PlanoDTO
from src.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.modulos.planos.aplicacion.mapeadores import MapeadorPlano
from src.modulos.planos.infraestructura.repositorios import RepositorioPlano
from src.seedwork.dominio.excepciones import ExcepcionPlano


@dataclass
class CrearPlano(Comando):
    planoDTO: PlanoDTO


class CrearPlanoHandler(CrearPlanoBaseHandler):

    def handle(self, comando: CrearPlano):

        plano: Plano = self.fabrica_plano.crear_objeto(
            comando.planoDTO, MapeadorPlano())

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPlano.__class__)

        plano_db = repositorio.obtener_por_propiedad_id(plano.propiedad_id)
        if plano_db is not None:
            raise ExcepcionPlano('PROPIEDAD YA EXISTE')

        plano.crear_plano(plano=plano)

        UnidadTrabajoPuerto.registrar_batch(
            repositorio.agregar, plano)

        UnidadTrabajoPuerto.commit()


@comando.register(CrearPlano)
def ejecutar_comando_crear_plano(comando: Plano):
    handler = CrearPlanoHandler()
    handler.handle(comando)
