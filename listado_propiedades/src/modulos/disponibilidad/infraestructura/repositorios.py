from src.config.db import db
from src.modulos.disponibilidad.dominio.entidades import Disponibilidad
from src.modulos.disponibilidad.dominio.repositorios import RepositorioDisponibilidad
from .mapeadores import MapeadorDisponibilidad
from src.modulos.disponibilidad.dominio.fabricas import FabricaDisponibilidad
from .dto import Disponibilidad as DisponibilidadDTO


class RepositorioDisponibilidadPostgres(RepositorioDisponibilidad):

    def __init__(self):
        self._fabrica_disponibilidad: FabricaDisponibilidad = FabricaDisponibilidad()

    @property
    def fabrica_disponibilidad(self):
        return self._fabrica_disponibilidad

    def obtener_por_id(self, id: str) -> Disponibilidad:
        disponibilidad_dto = db.session.query(
            DisponibilidadDTO).filter_by(id=id).one()
        return self.fabrica_disponibilidad.crear_objeto(disponibilidad_dto, MapeadorDisponibilidad())

    def obtener_todos(self) -> list[Disponibilidad]:
        caracterizaciones_dto = db.session.query(DisponibilidadDTO).all()
        return self.fabrica_disponibilidad.crear_objeto(caracterizaciones_dto, MapeadorDisponibilidad())

    def agregar(self, disponibilidad: Disponibilidad):
        disponibilidad_dto = self.fabrica_disponibilidad.crear_objeto(
            disponibilidad, MapeadorDisponibilidad())
        db.session.add(disponibilidad_dto)

    def actualizar(self, disponibilidad: Disponibilidad):
        # TODO
        raise NotImplementedError

    def eliminar(self, id: str):
        # TODO
        raise NotImplementedError
