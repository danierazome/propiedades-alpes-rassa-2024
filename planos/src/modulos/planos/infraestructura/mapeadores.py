from src.seedwork.dominio.repositorios import Mapeador
from src.modulos.planos.dominio.entidades import Plano
from .dto import Plano as PlanoDTO


class MapeadorPlano(Mapeador):

    def obtener_tipo(self) -> type:
        return Plano.__class__

    def entidad_a_dto(self, entidad: Plano) -> PlanoDTO:

        plano_dto = PlanoDTO()
        plano_dto.propiedad_id = entidad.propiedad_id
        plano_dto.id = entidad.id
        plano_dto.fecha_creacion = entidad.fecha_creacion
        plano_dto.fecha_actualizacion = entidad.fecha_actualizacion
        plano_dto.area_construida = entidad.area_construida
        plano_dto.area_total = entidad.area_total
        plano_dto.floors = entidad.floors
        plano_dto.status = entidad.status.value
        plano_dto.zone = entidad.zone

        return plano_dto

    def entidad_list_a_dto_list(self, entidades: list[Plano]) -> list[PlanoDTO]:
        entidades_dto = list()
        for e in entidades:
            entidades_dto.append(self.entidad_a_dto(entidad=e))
        return entidades_dto

    def dto_a_entidad(self, dto: PlanoDTO) -> Plano:
        plano = Plano(
            id=dto.id,
            propiedad_id=dto.propiedad_id,
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion,
            area_construida=dto.area_construida,
            area_total=dto.area_total,
            floors=dto.floors,
            status=dto.status,
            zone=dto.zone
        )

        return plano

    def dto_list_a_entidad_list(self, dtos: list[PlanoDTO]) -> list[Plano]:
        dtos_entidades = list()
        for d in dtos:
            dtos_entidades.append(self.dto_a_entidad(dto=d))
        return dtos_entidades
