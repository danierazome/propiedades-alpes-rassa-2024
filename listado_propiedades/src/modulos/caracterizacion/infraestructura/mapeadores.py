from src.seedwork.dominio.repositorios import Mapeador
from src.modulos.caracterizacion.dominio.entidades import Caracterizacion
from .dto import Caracterizacion as CaracterizacionDTO


class MapeadorCaracterizacion(Mapeador):

    def obtener_tipo(self) -> type:
        return Caracterizacion.__class__

    def entidad_a_dto(self, entidad: Caracterizacion) -> CaracterizacionDTO:

        caracterizacion_dto = CaracterizacionDTO()
        caracterizacion_dto.propiedad_id = entidad.propiedad_id
        caracterizacion_dto.id = entidad.id
        caracterizacion_dto.floors = entidad.floors
        caracterizacion_dto.zone = entidad.zone
        caracterizacion_dto.type = entidad.type
        caracterizacion_dto.status = entidad.status
        caracterizacion_dto.fecha_creacion = entidad.fecha_creacion
        caracterizacion_dto.fecha_actualizacion = entidad.fecha_actualizacion

        return caracterizacion_dto

    def entidad_list_a_dto_list(self, entidades: list[Caracterizacion]) -> list[CaracterizacionDTO]:
        entidades_dto = list()
        for e in entidades:
            entidades_dto.append(self.entidad_a_dto(entidad=e))
        return entidades_dto

    def dto_a_entidad(self, dto: CaracterizacionDTO) -> Caracterizacion:
        caracterizacion = Caracterizacion(
            id=dto.id,
            propiedad_id=dto.propiedad_id,
            zone=dto.zone,
            floors=dto.floors,
            type=dto.type,
            status=dto.status,
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion
        )

        return caracterizacion

    def dto_list_a_entidad_list(self, dtos: list[CaracterizacionDTO]) -> list[Caracterizacion]:
        dtos_entidades = list()
        for d in dtos:
            dtos_entidades.append(self.dto_a_entidad(dto=d))
        return dtos_entidades
