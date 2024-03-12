from src.seedwork.aplicacion.evento_handler import EventHandler
from src.modulos.audit.infraestructura.fabricas import FabricaRepositorio
from src.modulos.audit.dominio.fabricas import FabricaAuditoria


class AuditoriaBaseHandler(EventHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditoria: FabricaAuditoria = FabricaAuditoria()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_auditoria(self):
        return self._fabrica_auditoria
