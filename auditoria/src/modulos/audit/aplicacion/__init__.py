from pydispatch import dispatcher
from .handlers import HandlerAuditoriaIntegracion
from src.modulos.audit.dominio.eventos import ActualizarPlano, ActualizarCaracterizacion

dispatcher.connect(HandlerAuditoriaIntegracion.handle_actualizar_caracterizacion,
                   signal=f'{ActualizarCaracterizacion.__name__}Integracion')

dispatcher.connect(HandlerAuditoriaIntegracion.handle_actualizar_plano,
                   signal=f'{ActualizarPlano.__name__}Integracion')
