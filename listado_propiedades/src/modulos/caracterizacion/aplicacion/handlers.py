from src.seedwork.aplicacion.handlers import Handler
from src.modulos.caracterizacion.infraestructura.despachadores import Despachador


class HandlerCaractIntegracion(Handler):

    @staticmethod
    def handle_caract_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento_caract_creada(
            evento, 'caract-creado-v1')

    @staticmethod
    def handle_caract_eliminada(evento):
        despachador = Despachador()
        despachador.publicar_evento_caract_eliminada(
            evento, 'caract-eliminada-v1')

    @staticmethod
    def handle_caract_creada_fallida(evento):
        despachador = Despachador()
        despachador.publicar_evento_caract_creada_fallida(
            evento, 'caract-creada-fallida-v1')
