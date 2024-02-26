from src.seedwork.aplicacion.queries import QueryHandler
from src.modulos.caracterizacion.infraestructura.fabricas import FabricaRepositorio
from src.modulos.caracterizacion.dominio.fabricas import FabricaCaracterizacion


class CaracterizacionQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_caracterizacion: FabricaCaracterizacion = FabricaCaracterizacion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_caracterizacion(self):
        return self._fabrica_caracterizacion
