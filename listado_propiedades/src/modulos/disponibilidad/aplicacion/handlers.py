
from src.seedwork.aplicacion.handlers import Handler
from src.modulos.caracterizacion.dominio.eventos import CaracterizacionCreada
from src.modulos.disponibilidad.dominio.entidades import Disponibilidad

from src.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.modulos.disponibilidad.infraestructura.repositorios import RepositorioDisponibilidad
from src.modulos.disponibilidad.dominio.fabricas import FabricaDisponibilidad
from src.modulos.disponibilidad.infraestructura.fabricas import FabricaRepositorio
from src.modulos.disponibilidad.aplicacion.mapeadores import MapeadorDisponibilidad


class HandlerReservaDominio(Handler):

    @staticmethod
    def handle_reserva_creada(evento: CaracterizacionCreada):
        fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        fabrica_disponibilidad: FabricaDisponibilidad = FabricaDisponibilidad()

        disponibilidad: Disponibilidad = fabrica_disponibilidad.crear_objeto(
            evento, MapeadorDisponibilidad())

        repositorio = fabrica_repositorio.crear_objeto(
            RepositorioDisponibilidad.__class__)

        UnidadTrabajoPuerto.registrar_batch(
            repositorio.agregar, disponibilidad)
        UnidadTrabajoPuerto.commit()
