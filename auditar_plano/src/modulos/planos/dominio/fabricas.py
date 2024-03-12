from .entidades import Plano
from src.seedwork.dominio.repositorios import Mapeador
from src.seedwork.dominio.fabricas import Fabrica
from src.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


@dataclass
class FabricaSagaLog(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, list):
            return mapeador.entidad_list_a_dto_list(obj)
        elif isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            return mapeador.dto_a_entidad(obj)


@dataclass
class FabricaSagaLogInfra(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, list):
            return mapeador.dto_list_a_entidad_list(obj)
        elif isinstance(obj, Plano):
            return mapeador.entidad_a_dto(obj)
        else:
            return mapeador.dto_a_entidad(obj)
