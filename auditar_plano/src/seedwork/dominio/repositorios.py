""" Interfaces para los repositorios reusables parte del seedwork del proyecto

En este archivo usted encontrará las diferentes interfaces para repositorios
reusables parte del seedwork del proyecto

"""

from abc import ABC, abstractmethod
from uuid import UUID
from .entidades import Entidad


class Repositorio(ABC):

    @abstractmethod
    def obtener_todos(self) -> list[Entidad]:
        ...

    @abstractmethod
    def agregar(self, entity: any):
        ...


class Mapeador(ABC):
    @abstractmethod
    def obtener_tipo(self) -> type:
        ...

    @abstractmethod
    def entidad_a_dto(self, entidad: Entidad) -> any:
        ...

    @abstractmethod
    def dto_a_entidad(self, dto: any) -> Entidad:
        ...

    @abstractmethod
    def dto_list_a_entidad_list(self, dtos: any) -> any:
        ...

    @abstractmethod
    def entidad_list_a_dto_list(self, entidades: any) -> any:
        ...
