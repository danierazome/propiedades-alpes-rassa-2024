from src.seedwork.aplicacion.handlers import Handler
from src.modulos.audit.infraestructura.despachadores import Despachador


class HandlerAuditoriaIntegracion(Handler):

    @staticmethod
    def handle_actualizar_plano(evento):
        despachador = Despachador()
        despachador.publicar_comando_actualizar_plano(
            evento, 'actualizar-plano')

    @staticmethod
    def handle_actualizar_caracterizacion(evento):
        despachador = Despachador()
        despachador.publicar_comando_actualizar_caracterizacion(
            evento, 'actualizar-caracterizacion')
