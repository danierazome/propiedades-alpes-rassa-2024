from src.seedwork.aplicacion.dto import Mapeador as AppMap
from src.seedwork.dominio.repositorios import Mapeador as RepMap
from src.modulos.caracterizacion.dominio.entidades import Caracterizacion
from .dto import CaracterizacionDTO, ResponseCaracterizacionDTO


class MapeadorCaracterizacion(RepMap):
    def obtener_tipo(self) -> type:
        return Caracterizacion.__class__

    def dto_a_entidad(self, dto: CaracterizacionDTO) -> Caracterizacion:
        caracterizacion = Caracterizacion(
            propiedad_id=dto.propiedad_id,
            floors=dto.floors,
            zone=dto.zone,
            type=dto.type
        )

        return caracterizacion

    def dto_list_a_entidad_list(self, dtos: list[CaracterizacionDTO]) -> list[Caracterizacion]:
        dtos_entidades = list()
        for d in dtos:
            dtos_entidades.append(self.dto_a_entidad(dto=d))
        return dtos_entidades

    def entidad_a_dto(self, entidad: Caracterizacion) -> ResponseCaracterizacionDTO:
        return ResponseCaracterizacionDTO(
            propiedad_id=entidad.propiedad_id,
            id=entidad.id,
            status=entidad.status,
            zone=entidad.zone,
            floors=entidad.floors,
            fecha_creacion=entidad.fecha_creacion,
            fecha_actualizacion=entidad.fecha_actualizacion,
            type=entidad.type)

    def entidad_list_a_dto_list(self, entidades: list[Caracterizacion]) -> list[ResponseCaracterizacionDTO]:
        entidades_dto = list()
        for e in entidades:
            entidades_dto.append(self.entidad_a_dto(entidad=e))
        return entidades_dto


class MapeadorCaracterizacionDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> CaracterizacionDTO:
        caracterizacion_dto = CaracterizacionDTO(
            propiedad_id=externo.get('propiedad_id'),
            floors=externo.get('floors'),
            zone=externo.get('zone'),
            type=externo.get('type'))

        return caracterizacion_dto

    def dto_a_externo(self, dto: CaracterizacionDTO) -> dict:
        return dto.__dict__

    def dto_list_a_externo(self, dtos: list[CaracterizacionDTO]) -> list:
        externo = list()
        for d in dtos:
            externo.append(self.dto_a_externo(d))
        return externo
