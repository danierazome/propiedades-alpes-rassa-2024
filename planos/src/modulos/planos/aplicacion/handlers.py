from src.seedwork.aplicacion.handlers import Handler
from src.modulos.planos.infraestructura.despachadores import Despachador
from src.seedwork.aplicacion.handlers import Handler


class HandlerPlanoIntegracion(Handler):

    @staticmethod
    def handle_plano_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento_plano_creada(
            evento, 'plano-creado-v1')

    @staticmethod
    def handle_plano_eliminada(evento):
        despachador = Despachador()
        despachador.publicar_evento_plano_eliminada(
            evento, 'plano-eliminada-v1')

    @staticmethod
    def handle_plano_creado_fallida(evento):
        despachador = Despachador()
        despachador.publicar_evento_plano_creada_fallida(
            evento, 'plano-creada-fallida-v1')
