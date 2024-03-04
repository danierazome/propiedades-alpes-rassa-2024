from pydispatch import dispatcher
from .handlers import HandlerPlanoIntegracion
from src.modulos.planos.dominio.eventos import PlanoCreado

dispatcher.connect(HandlerPlanoIntegracion.handle_reserva_creada,
                   signal=f'{PlanoCreado.__name__}Integracion')
