from src.config.db import db
from src.modulos.audit.dominio.entidades import Auditoria
from src.modulos.audit.dominio.repositorios import RepositorioAuditoria
from .mapeadores import MapeadorAuditoria
from src.modulos.audit.dominio.fabricas import FabricaAuditoriaInfra
from .dto import Auditoria as AuditoriaDTO


class RepositorioAuditoriaPostgres(RepositorioAuditoria):

    def __init__(self):
        self._fabrica_auditoria: FabricaAuditoriaInfra = FabricaAuditoriaInfra()

    @property
    def fabrica_auditoria(self):
        return self._fabrica_auditoria

    def obtener_por_id_dto(self, id: str) -> any:
        return db.session.query(
            AuditoriaDTO).filter_by(propiedad_id=id).first()

    def obtener_por_id(self, id: str) -> Auditoria:
        auditoria_dto = db.session.query(
            AuditoriaDTO).filter_by(id=id).one()
        return self.fabrica_auditoria.crear_objeto(auditoria_dto, MapeadorAuditoria())

    def obtener_todos(self) -> list[Auditoria]:
        auditorias_dto = db.session.query(AuditoriaDTO).all()
        return self.fabrica_auditoria.crear_objeto(auditorias_dto, MapeadorAuditoria())

    def agregar(self, auditoria: Auditoria):
        auditoria_dto = self.fabrica_auditoria.crear_objeto(
            auditoria, MapeadorAuditoria())
        db.session.add(auditoria_dto)

    def actualizar(self, auditoria: Auditoria):
        # TODO
        raise NotImplementedError

    def eliminar(self, id: str):
        auditoria = db.session.query(
            AuditoriaDTO).filter_by(propiedad_id=id).first()
        if auditoria is not None:
            db.session.delete(auditoria)

    def commit(self):
        db.session.commit()
