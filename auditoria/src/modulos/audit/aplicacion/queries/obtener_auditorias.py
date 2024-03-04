from src.seedwork.aplicacion.queries import Query, QueryResultado
from src.seedwork.aplicacion.queries import ejecutar_query as query
from src.modulos.audit.infraestructura.repositorios import RepositorioAuditoria
from dataclasses import dataclass
from .base import AuditoriaQueryBaseHandler
from src.modulos.audit.aplicacion.mapeadores import MapeadorAuditoria


@dataclass
class ObtenerAuditorias(Query):
    ...


class ObtenerAuditoriasHandler(AuditoriaQueryBaseHandler):

    def handle(self, query: ObtenerAuditorias) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioAuditoria.__class__)

        auditorias = self.fabrica_auditoria.crear_objeto(
            repositorio.obtener_todos(), MapeadorAuditoria())

        return QueryResultado(resultado=auditorias)


@query.register(ObtenerAuditorias)
def ejecutar_query_obtener_auditorias(query: ObtenerAuditorias):
    handler = ObtenerAuditoriasHandler()
    return handler.handle(query)
