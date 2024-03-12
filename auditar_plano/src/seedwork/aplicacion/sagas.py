from abc import ABC, abstractmethod
from src.seedwork.aplicacion.comandos import Comando
from src.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass
from .comandos import ejecutar_commando
import uuid
import datetime


class CoordinadorSaga(ABC):
    id_correlacion: uuid.UUID
    db: any

    @abstractmethod
    def persistir_en_saga_log(self, mensaje):
        ...

    @abstractmethod
    def construir_comando(self, evento: EventoDominio) -> Comando:
        ...

    def publicar_comando(self, evento: EventoDominio):
        comando = self.construir_comando(evento)
        ejecutar_commando(comando)

    @abstractmethod
    def inicializar_pasos(self, db):
        ...

    @abstractmethod
    def procesar_evento(self, evento: EventoDominio):
        ...

    @abstractmethod
    def obtener_paso_dado_un_evento(self, evento: EventoDominio):
        ...

    @abstractmethod
    def es_ultima_transaccion(self, index):
        ...


class Paso():
    id_correlacion: uuid.UUID
    fecha_evento: datetime.datetime
    index: int


@dataclass
class Inicio(Paso):
    index: int = 0
    evento: EventoDominio = None


@dataclass
class Fin(Paso):
    ...


@dataclass
class Transaccion(Paso):
    index: int
    comando: Comando
    evento: EventoDominio


@dataclass
class TransaccionCompensacion(Paso):
    index: int
    comando: Comando
    evento: EventoDominio
    evento_error: EventoDominio


class CoordinadorOrquestacion(CoordinadorSaga, ABC):
    pasos: list[Paso]
    index: int
    transaccion_type: str

    def obtener_paso_dado_un_evento(self, evento: EventoDominio):
        for i, paso in enumerate(self.pasos):

            if isinstance(evento, paso.evento):
                return i
        raise Exception("Evento no hace parte de la transacción")

    def es_ultima_transaccion(self, index):
        return (len(self.pasos) - 1) == index

    def procesar_evento(self, evento: EventoDominio):
        index = self.obtener_paso_dado_un_evento(evento)
        self.index = index
        self.persistir_en_saga_log(evento)
        if self.es_ultima_transaccion(index) == False:
            self.index = index + 1
            self.publicar_comando(evento)


class CoordinadorCompensacion(CoordinadorSaga, ABC):
    pasos: list[Paso]
    index: int
    transaccion_type: str

    def obtener_paso_dado_un_evento(self, evento: EventoDominio):
        for i, paso in enumerate(self.pasos):

            if isinstance(evento, paso.evento):
                return i
            if isinstance(evento, paso.evento_error):
                return i
        raise Exception("Evento no hace parte de la transacción")

    def es_ultima_transaccion(self, index):
        return (len(self.pasos) - 1) == index

    def procesar_evento(self, evento: EventoDominio):
        index = self.obtener_paso_dado_un_evento(evento)
        self.index = index
        self.persistir_en_saga_log(evento)
        if self.es_ultima_transaccion(index) == False:
            self.index = index + 1
            self.publicar_comando(evento)
