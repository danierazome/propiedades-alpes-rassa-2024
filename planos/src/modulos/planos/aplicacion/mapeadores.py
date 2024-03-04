from src.seedwork.dominio.repositorios import Mapeador
from .dto import PlanoDTO, ResponsePlanoDTO
from src.modulos.planos.dominio.entidades import Plano
from src.seedwork.aplicacion.dto import Mapeador as AppMap
import uuid


class MapeadorPlano(Mapeador):

    def obtener_tipo(self) -> type:
        return Plano.__class__

    def dto_a_entidad(self, dto: PlanoDTO) -> Plano:
        plano = Plano(
            id=str(uuid.uuid4()),
            propiedad_id=dto.propiedad_id,
            area_construida=dto.area_construida,
            area_total=dto.area_total,
            floors=dto.floors,
            zone=dto.zone
        )

        return plano

    def dto_list_a_entidad_list(self, dtos: list[PlanoDTO]) -> list[Plano]:
        dtos_entidades = list()
        for d in dtos:
            dtos_entidades.append(self.dto_a_entidad(dto=d))
        return dtos_entidades

    def entidad_a_dto(self, entidad: Plano) -> ResponsePlanoDTO:
        return ResponsePlanoDTO(
            propiedad_id=entidad.propiedad_id,
            id=entidad.id,
            fecha_creacion=entidad.fecha_creacion,
            fecha_actualizacion=entidad.fecha_actualizacion,
            area_construida=entidad.area_construida,
            area_total=entidad.area_total,
            floors=entidad.floors,
            status=entidad.status,
            zone=entidad.zone)

    def entidad_list_a_dto_list(self, entidades: list[Plano]) -> list[ResponsePlanoDTO]:
        entidades_dto = list()
        for e in entidades:
            entidades_dto.append(self.entidad_a_dto(entidad=e))
        return entidades_dto


class MapeadorPlanoDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PlanoDTO:
        plano_dto = PlanoDTO(
            propiedad_id=externo.get('propiedad_id'),
            area_construida=externo.get('area_construida'),
            area_total=externo.get('area_total'),
            floors=externo.get('floors'),
            zone=externo.get('zone')
        )

        return plano_dto

    def dto_a_externo(self, dto: PlanoDTO) -> dict:
        return dto.__dict__

    def dto_list_a_externo(self, dtos: list[PlanoDTO]) -> list:
        externo = list()
        for d in dtos:
            externo.append(self.dto_a_externo(d))
        return externo
