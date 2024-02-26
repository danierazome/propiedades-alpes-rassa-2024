from src.config.db import db
from src.modulos.caracterizacion.dominio.entidades import Caracterizacion
from src.modulos.caracterizacion.dominio.fabricas import FabricaCaracterizacion, FabricaCaracterizacionInfra
from src.modulos.caracterizacion.dominio.repositorios import RepositorioCaracterizacion
from .dto import Caracterizacion as CaracterizacionDTO

from .mapeadores import MapeadorCaracterizacion
from uuid import UUID


class RepositorioCaracterizacionPostgres(RepositorioCaracterizacion):

    def __init__(self):
        self._fabrica_caracterizacion: FabricaCaracterizacionInfra = FabricaCaracterizacionInfra()

    @property
    def fabrica_caracterizacion(self):
        return self._fabrica_caracterizacion

    def obtener_por_id(self, id: str) -> Caracterizacion:
        caracterizacion_dto = db.session.query(
            CaracterizacionDTO).filter_by(id=id).one()
        return self.fabrica_caracterizacion.crear_objeto(caracterizacion_dto, MapeadorCaracterizacion())

    def obtener_todos(self) -> list[Caracterizacion]:
        caracterizaciones_dto = db.session.query(CaracterizacionDTO).all()
        return self.fabrica_caracterizacion.crear_objeto(caracterizaciones_dto, MapeadorCaracterizacion())

    def agregar(self, caracterizacion: Caracterizacion):

        caracterizacion_dto = self._fabrica_caracterizacion.crear_objeto(
            caracterizacion, MapeadorCaracterizacion())
        db.session.add(caracterizacion_dto)

    def actualizar(self, caracterizacion: Caracterizacion):
        # TODO
        raise NotImplementedError

    def eliminar(self, id: str):
        # TODO
        raise NotImplementedError
