from src.seedwork.aplicacion.handlers import Handler
from src.modulos.planos.infraestructura.despachadores import Despachador
from src.seedwork.aplicacion.handlers import Handler


class HandlerEventosComandos(Handler):

    @staticmethod
    def handle_crear_auditoria(evento):
        despachador = Despachador()
        despachador.publicar_comando_crear_auditoria(
            evento, 'comando-crear-auditoria-v1')

    @staticmethod
    def handle_crear_plano(evento):
        despachador = Despachador()
        despachador.publicar_comando_crear_plano(
            evento, 'comando-crear-plano-v1')

    @staticmethod
    def handle_crear_caracterizacion(evento):
        despachador = Despachador()
        despachador.publicar_comando_crear_caract(
            evento, 'comando-crear-caract-v1')

    @staticmethod
    def handle_eliminar_auditoria(evento):
        despachador = Despachador()
        despachador.publicar_comando_eliminar_auditoria(
            evento, 'comando-eliminar-auditoria-v1')

    @staticmethod
    def handle_eliminar_plano(evento):
        despachador = Despachador()
        despachador.publicar_comando_eliminar_plano(
            evento, 'comando-eliminar-plano-v1')

    @staticmethod
    def handle_eliminar_caracterizacion(evento):
        despachador = Despachador()
        despachador.publicar_comando_eliminar_caract(
            evento, 'comando-eliminar-caract-v1')

    @staticmethod
    def handle_transacion_inicializada(evento):
        despachador = Despachador()
        despachador.publicar_evento_transacion_inicializada(
            evento, 'transacion-inicializada-v1')
