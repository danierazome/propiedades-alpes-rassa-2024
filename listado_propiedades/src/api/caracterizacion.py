import src.seedwork.presentacion.api as api
import json
from src.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.modulos.caracterizacion.aplicacion.mapeadores import MapeadorCaracterizacionDTOJson
from src.modulos.caracterizacion.aplicacion.comandos.crear_caracterizacion import CrearCaracterizacion
from src.modulos.caracterizacion.aplicacion.queries.obtener_caracterizaciones import ObtenerCaracterizaciones
from src.seedwork.aplicacion.comandos import ejecutar_commando
from src.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('caracterizacion', '/caracterizacion')


@bp.route('/', methods=('GET',))
def dar_caracterizacion():
    if id:
        query_resultado = ejecutar_query(ObtenerCaracterizaciones())
        map_caracterizacion = MapeadorCaracterizacionDTOJson()

        return map_caracterizacion.dto_list_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]


@bp.route('/', methods=('POST',))
def crear_caracterizacion_api():
    try:
        reserva_dict = request.json

        map_caracterizacion = MapeadorCaracterizacionDTOJson()

        caracterizacion_dto = map_caracterizacion.externo_a_dto(reserva_dict)
        comando = CrearCaracterizacion(caracterizacionDTO=caracterizacion_dto)

        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
