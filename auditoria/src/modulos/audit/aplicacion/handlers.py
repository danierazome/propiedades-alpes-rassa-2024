from src.seedwork.aplicacion.handlers import Handler
from src.modulos.audit.infraestructura.despachadores import Despachador


class HandlerAuditoriaIntegracion(Handler):

    @staticmethod
    def handle_auditoria_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento_auditoria_creada(
            evento, 'auditoria-creado-v1')

    @staticmethod
    def handle_auditoria_eliminada(evento):
        despachador = Despachador()
        despachador.publicar_evento_auditoria_eliminada(
            evento, 'auditoria-eliminada-v1')

    @staticmethod
    def handle_auditoria_creada_fallida(evento):
        despachador = Despachador()
        despachador.publicar_evento_auditoria_creada_fallida(
            evento, 'auditoria-creada-fallida-v1')
