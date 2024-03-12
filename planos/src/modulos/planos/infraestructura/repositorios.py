from src.config.db import db
from src.modulos.planos.dominio.entidades import Plano
from src.modulos.planos.dominio.repositorios import RepositorioPlano
from .mapeadores import MapeadorPlano
from src.modulos.planos.dominio.fabricas import FabricaPlanoInfra
from .dto import Plano as PlanoDTO


class RepositorioPlanoPostgres(RepositorioPlano):

    def __init__(self):
        self._fabrica_plano: FabricaPlanoInfra = FabricaPlanoInfra()

    @property
    def fabrica_plano(self):
        return self._fabrica_plano

    def obtener_por_propiedad_id(self, id: str) -> any:
        return db.session.query(
            PlanoDTO).filter_by(propiedad_id=id).first()

    def obtener_por_id(self, id: str) -> Plano:
        plano_dto = db.session.query(
            PlanoDTO).filter_by(propiedad_id=id).first()
        return self.fabrica_plano.crear_objeto(plano_dto, MapeadorPlano())

    def obtener_todos(self) -> list[Plano]:
        planos_dto = db.session.query(PlanoDTO).all()
        return self.fabrica_plano.crear_objeto(planos_dto, MapeadorPlano())

    def agregar(self, plano: Plano):
        plano_dto = self.fabrica_plano.crear_objeto(
            plano, MapeadorPlano())
        db.session.add(plano_dto)

    def agregar_dto(self, dto):
        db.session.add(dto)

    def actualizar(self, plano: Plano):
        plano_dto = self.fabrica_plano.crear_objeto(
            plano, MapeadorPlano())

    def eliminar(self, id: str):
        plano = db.session.query(
            PlanoDTO).filter_by(propiedad_id=id).first()
        if plano is not None:
            db.session.delete(plano)
