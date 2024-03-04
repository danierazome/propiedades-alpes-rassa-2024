from src.seedwork.aplicacion.queries import Query, QueryResultado
from src.seedwork.aplicacion.queries import ejecutar_query as query
from src.modulos.planos.infraestructura.repositorios import RepositorioPlano
from dataclasses import dataclass
from .base import PlanoQueryBaseHandler
from src.modulos.planos.aplicacion.mapeadores import MapeadorPlano


@dataclass
class ObtenerPlanos(Query):
    ...


class ObtenerPlanosHandler(PlanoQueryBaseHandler):

    def handle(self, query: ObtenerPlanos) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPlano.__class__)

        planos = self.fabrica_plano.crear_objeto(
            repositorio.obtener_todos(), MapeadorPlano())
        return QueryResultado(resultado=planos)


@query.register(ObtenerPlanos)
def ejecutar_query_obtener_planos(query: ObtenerPlanos):
    handler = ObtenerPlanosHandler()
    return handler.handle(query)
