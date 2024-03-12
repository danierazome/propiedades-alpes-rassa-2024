from dataclasses import dataclass, field
from src.seedwork.dominio.fabricas import Fabrica
from src.seedwork.dominio.repositorios import Repositorio
from .repositorios import RepositorioPlanoPostgres


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        return RepositorioPlanoPostgres()
