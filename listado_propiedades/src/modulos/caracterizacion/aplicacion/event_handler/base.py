from src.seedwork.aplicacion.evento_handler import EventHandler
from src.modulos.caracterizacion.infraestructura.fabricas import FabricaRepositorio


class ActualizarCaractBaseHandler(EventHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
