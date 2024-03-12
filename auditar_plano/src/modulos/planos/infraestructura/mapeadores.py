from src.seedwork.dominio.repositorios import Mapeador
from src.modulos.planos.dominio.entidades import SagaLog
from .dto import SagaLog as SagaLogDto


class MapeadorSagaLog(Mapeador):

    def obtener_tipo(self) -> type:
        return SagaLog.__class__

    def entidad_a_dto(self, entidad: SagaLog) -> SagaLogDto:

        saga_log_dto = SagaLogDto()
        saga_log_dto.correlation_id = entidad.correlation_id
        saga_log_dto.fecha = entidad.fecha
        saga_log_dto.index = entidad.index
        saga_log_dto.type = entidad.type

        return saga_log_dto

    def entidad_list_a_dto_list(self, entidades: list[SagaLog]) -> list[SagaLogDto]:
        entidades_dto = list()
        for e in entidades:
            entidades_dto.append(self.entidad_a_dto(entidad=e))
        return entidades_dto

    def dto_a_entidad(self, dto: SagaLogDto) -> SagaLog:
        saga_log = SagaLog(
            id=dto.id,
            fecha=dto.fecha,
            correlation_id=dto.correlation_id,
            index=dto.index,
            type=dto.type
        )

        return saga_log

    def dto_list_a_entidad_list(self, dtos: list[SagaLogDto]) -> list[SagaLog]:
        dtos_entidades = list()
        for d in dtos:
            dtos_entidades.append(self.dto_a_entidad(dto=d))
        return dtos_entidades
