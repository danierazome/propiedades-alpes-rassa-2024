import src.seedwork.presentacion.api as api

from flask import redirect, render_template, request, session, url_for
from src.modulos.disponibilidad.aplicacion.mapeadores import MapeadorDisponibilidadDTOJson
from src.modulos.disponibilidad.aplicacion.queries.obtener_disponibilidades import ObtenerDisponibilidades
from src.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('disponibilidad', '/disponibilidad')


@bp.route('/', methods=('GET',))
def dar_caracterizacion():
    if id:
        query_resultado = ejecutar_query(ObtenerDisponibilidades())
        map_caracterizacion = MapeadorDisponibilidadDTOJson()

        return map_caracterizacion.dto_list_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
