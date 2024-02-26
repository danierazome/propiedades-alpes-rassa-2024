from src.seedwork.aplicacion.queries import Query, QueryResultado
from src.seedwork.aplicacion.queries import ejecutar_query as query
from src.modulos.caracterizacion.infraestructura.repositorios import RepositorioCaracterizacion
from dataclasses import dataclass
from .base import CaracterizacionQueryBaseHandler
from src.modulos.caracterizacion.aplicacion.mapeadores import MapeadorCaracterizacion


@dataclass
class ObtenerCaracterizaciones(Query):
    ...


class ObtenerCaracterizacionesHandler(CaracterizacionQueryBaseHandler):

    def handle(self, query: ObtenerCaracterizaciones) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioCaracterizacion.__class__)

        caracterizaciones = self.fabrica_caracterizacion.crear_objeto(
            repositorio.obtener_todos(), MapeadorCaracterizacion())
        return QueryResultado(resultado=caracterizaciones)


@query.register(ObtenerCaracterizaciones)
def ejecutar_query_obtener_caracterizacion(query: ObtenerCaracterizaciones):
    handler = ObtenerCaracterizacionesHandler()
    return handler.handle(query)
