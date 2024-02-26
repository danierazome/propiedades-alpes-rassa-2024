from src.seedwork.aplicacion.queries import Query, QueryResultado
from src.seedwork.aplicacion.queries import ejecutar_query as query
from src.modulos.disponibilidad.infraestructura.repositorios import RepositorioDisponibilidad
from dataclasses import dataclass
from .base import DisponibilidadQueryBaseHandler
from src.modulos.disponibilidad.aplicacion.mapeadores import MapeadorDisponibilidad


@dataclass
class ObtenerDisponibilidades(Query):
    ...


class ObtenerDisponibilidadesHandler(DisponibilidadQueryBaseHandler):

    def handle(self, query: ObtenerDisponibilidades) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioDisponibilidad.__class__)

        disponibilidades = self.fabrica_disponibilidad.crear_objeto(
            repositorio.obtener_todos(), MapeadorDisponibilidad())
        return QueryResultado(resultado=disponibilidades)


@query.register(ObtenerDisponibilidades)
def ejecutar_query_obtener_disponibilidades(query: ObtenerDisponibilidades):
    handler = ObtenerDisponibilidadesHandler()
    return handler.handle(query)
