import src.seedwork.presentacion.api as api

from flask import redirect, render_template, request, session, url_for
from src.modulos.planos.aplicacion.mapeadores import MapeadorAuditoriaDTOJson
from src.modulos.planos.aplicacion.queries.obtener_saga_log import ObtenerSagaLog
from src.modulos.planos.aplicacion.comandos.iniciar_transaccion import IniciarTransaccion
from src.seedwork.aplicacion.queries import ejecutar_query
from src.seedwork.aplicacion.comandos import ejecutar_commando
from flask import Response
from src.seedwork.dominio.excepciones import ExcepcionDominio
import json

bp = api.crear_blueprint('auditar', '/auditar-planos')


@bp.route('/saga-log', methods=('GET',))
def dar_saga_logs():
    if id:
        query_resultado = ejecutar_query(ObtenerSagaLog())
        map_caracterizacion = MapeadorAuditoriaDTOJson()

        return map_caracterizacion.dto_list_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]


@bp.route('/', methods=('POST',))
def auditar_plano_api():
    try:
        dict = request.json

        mapeador = MapeadorAuditoriaDTOJson()

        auditoria = mapeador.externo_a_dto(dict)
        comando = IniciarTransaccion(transaccion=auditoria)

        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
