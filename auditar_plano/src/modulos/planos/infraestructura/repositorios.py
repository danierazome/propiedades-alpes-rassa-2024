from src.config.db import db
from src.modulos.planos.dominio.entidades import SagaLog
from src.modulos.planos.dominio.repositorios import RepositorioSagaLog
from .mapeadores import MapeadorSagaLog
from src.modulos.planos.dominio.fabricas import FabricaSagaLogInfra
from .dto import SagaLog as SagaLogDto


class RepositorioPlanoPostgres(RepositorioSagaLog):

    def __init__(self):
        self._fabrica_saga_log: FabricaSagaLogInfra = FabricaSagaLogInfra()

    @property
    def fabrica_plano(self):
        return self._fabrica_saga_log

    def obtener_todos(self) -> list[SagaLog]:
        planos_dto = db.session.query(SagaLogDto).all()
        return self.fabrica_plano.crear_objeto(planos_dto, MapeadorSagaLog())

    def agregar(self, saga_log: any):
        db.session.add(saga_log)
