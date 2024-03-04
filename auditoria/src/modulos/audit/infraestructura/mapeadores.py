from src.seedwork.dominio.repositorios import Mapeador
from src.modulos.audit.dominio.entidades import Auditoria
from .dto import Auditoria as AuditoriaDTO


class MapeadorAuditoria(Mapeador):

    def obtener_tipo(self) -> type:
        return Auditoria.__class__

    def entidad_a_dto(self, entidad: Auditoria) -> AuditoriaDTO:

        auditoria_dto = AuditoriaDTO()
        auditoria_dto.propiedad_id = entidad.propiedad_id
        auditoria_dto.id = entidad.id
        auditoria_dto.fecha_creacion = entidad.fecha_creacion
        auditoria_dto.fecha_actualizacion = entidad.fecha_actualizacion
        auditoria_dto.assessment = entidad.assessment
        auditoria_dto.client = entidad.client
        auditoria_dto.status = entidad.status.value

        return auditoria_dto

    def entidad_list_a_dto_list(self, entidades: list[Auditoria]) -> list[AuditoriaDTO]:
        entidades_dto = list()
        for e in entidades:
            entidades_dto.append(self.entidad_a_dto(entidad=e))
        return entidades_dto

    def dto_a_entidad(self, dto: AuditoriaDTO) -> Auditoria:
        auditoria = Auditoria(
            id=dto.id,
            propiedad_id=dto.propiedad_id,
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion,
            assessment=dto.assessment,
            client=dto.client,
            status=dto.status
        )

        return auditoria

    def dto_list_a_entidad_list(self, dtos: list[AuditoriaDTO]) -> list[Auditoria]:
        dtos_entidades = list()
        for d in dtos:
            dtos_entidades.append(self.dto_a_entidad(dto=d))
        return dtos_entidades
