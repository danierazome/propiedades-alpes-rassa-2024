from functools import singledispatch
from abc import ABC, abstractmethod


class Evento(ABC):
    ...


class EventoHandler(ABC):
    @abstractmethod
    def handle(self, event: Evento):
        raise NotImplementedError()


class EventHandler(ABC):
    @abstractmethod
    def handle(self, event: Evento):
        raise NotImplementedError()


@singledispatch
def ejecutar_evento(evento):
    raise NotImplementedError(
        f'No existe implementación para el evento de tipo {type(evento).__name__}')
