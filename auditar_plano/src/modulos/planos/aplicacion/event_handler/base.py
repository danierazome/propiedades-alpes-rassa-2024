from src.seedwork.aplicacion.evento_handler import EventHandler
from src.modulos.planos.infraestructura.fabricas import FabricaRepositorio
from src.modulos.planos.dominio.fabricas import FabricaSagaLog


class ActualizarPlanoBaseHandler(EventHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_plano: FabricaSagaLog = FabricaSagaLog()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_plano(self):
        return self._fabrica_plano
