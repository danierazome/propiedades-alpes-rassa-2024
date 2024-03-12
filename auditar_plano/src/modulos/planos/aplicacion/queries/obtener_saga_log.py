from src.seedwork.aplicacion.queries import Query, QueryResultado
from src.seedwork.aplicacion.queries import ejecutar_query as query
from src.modulos.planos.infraestructura.repositorios import RepositorioSagaLog
from dataclasses import dataclass
from .base import SagaLogQueryBaseHandler
from src.modulos.planos.aplicacion.mapeadores import MapeadorSagaLog


@dataclass
class ObtenerSagaLog(Query):
    ...


class ObtenerSagaLogHandler(SagaLogQueryBaseHandler):

    def handle(self, query: ObtenerSagaLog) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioSagaLog.__class__)

        saga_logs = self.fabrica_plano.crear_objeto(
            repositorio.obtener_todos(), MapeadorSagaLog())
        return QueryResultado(resultado=saga_logs)


@query.register(ObtenerSagaLog)
def ejecutar_query_obtener_saga_log(query: ObtenerSagaLog):
    handler = ObtenerSagaLogHandler()
    return handler.handle(query)
