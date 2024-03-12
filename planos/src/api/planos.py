import src.seedwork.presentacion.api as api

from flask import redirect, render_template, request, session, url_for
from src.modulos.planos.aplicacion.mapeadores import MapeadorPlanoDTOJson
from src.modulos.planos.aplicacion.queries.obtener_planos import ObtenerPlanos
from src.seedwork.aplicacion.queries import ejecutar_query
from src.seedwork.aplicacion.comandos import ejecutar_commando
from flask import Response
from src.seedwork.dominio.excepciones import ExcepcionDominio
import json


bp = api.crear_blueprint('plano', '/planos')


@bp.route('/', methods=('GET',))
def dar_planos():
    if id:
        query_resultado = ejecutar_query(ObtenerPlanos())
        map_caracterizacion = MapeadorPlanoDTOJson()

        return map_caracterizacion.dto_list_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
