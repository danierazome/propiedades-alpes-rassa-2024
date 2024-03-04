import src.seedwork.presentacion.api as api

from flask import redirect, render_template, request, session, url_for
from src.modulos.audit.aplicacion.mapeadores import MapeadorAuditoriaDTOJson
from src.modulos.audit.aplicacion.queries.obtener_auditorias import ObtenerAuditorias
from src.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('auditorias', '/auditorias')


@bp.route('/', methods=('GET',))
def dar_auditorias():
    if id:
        query_resultado = ejecutar_query(ObtenerAuditorias())
        map_auditorias = MapeadorAuditoriaDTOJson()

        return map_auditorias.dto_list_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
