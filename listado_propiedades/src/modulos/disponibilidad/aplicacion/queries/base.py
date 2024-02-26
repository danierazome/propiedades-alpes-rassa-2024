from src.seedwork.aplicacion.queries import QueryHandler
from src.modulos.disponibilidad.infraestructura.fabricas import FabricaRepositorio
from src.modulos.disponibilidad.dominio.fabricas import FabricaDisponibilidad


class DisponibilidadQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_disponibilidad: FabricaDisponibilidad = FabricaDisponibilidad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_disponibilidad(self):
        return self._fabrica_disponibilidad
