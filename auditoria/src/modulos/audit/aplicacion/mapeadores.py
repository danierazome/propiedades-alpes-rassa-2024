from src.seedwork.dominio.repositorios import Mapeador
from .dto import ResponseAuditoriaDTO
from src.modulos.audit.dominio.entidades import Auditoria
from src.seedwork.aplicacion.dto import Mapeador as AppMap
import uuid


class MapeadorAuditoria(Mapeador):

    def obtener_tipo(self) -> type:
        return Auditoria.__class__

    def dto_a_entidad(self, dto: any) -> Auditoria:
        return Auditoria()

    def dto_list_a_entidad_list(self, dtos: list[any]) -> list[Auditoria]:
        dtos_entidades = list()
        for d in dtos:
            dtos_entidades.append(self.dto_a_entidad(dto=d))
        return dtos_entidades

    def entidad_a_dto(self, entidad: Auditoria) -> ResponseAuditoriaDTO:
        return ResponseAuditoriaDTO(
            propiedad_id=entidad.propiedad_id,
            id=entidad.id,
            fecha_creacion=entidad.fecha_creacion,
            fecha_actualizacion=entidad.fecha_actualizacion,
            assessment=entidad.assessment,
            client=entidad.client,
            status=entidad.status)

    def entidad_list_a_dto_list(self, entidades: list[Auditoria]) -> list[ResponseAuditoriaDTO]:
        entidades_dto = list()
        for e in entidades:
            entidades_dto.append(self.entidad_a_dto(entidad=e))
        return entidades_dto


class MapeadorAuditoriaDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> ResponseAuditoriaDTO:
        return ResponseAuditoriaDTO()

    def dto_a_externo(self, dto: ResponseAuditoriaDTO) -> dict:
        return dto.__dict__

    def dto_list_a_externo(self, dtos: list[ResponseAuditoriaDTO]) -> list:
        externo = list()
        for d in dtos:
            externo.append(self.dto_a_externo(d))
        return externo
