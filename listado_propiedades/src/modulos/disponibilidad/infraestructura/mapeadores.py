from src.seedwork.dominio.repositorios import Mapeador
from src.modulos.disponibilidad.dominio.entidades import Disponibilidad
from .dto import Disponibilidad as DisponibilidadDTO


class MapeadorDisponibilidad(Mapeador):

    def obtener_tipo(self) -> type:
        return Disponibilidad.__class__

    def entidad_a_dto(self, entidad: Disponibilidad) -> DisponibilidadDTO:

        disponibilidad_dto = DisponibilidadDTO()
        disponibilidad_dto.propiedad_id = entidad.propiedad_id
        disponibilidad_dto.id = entidad.id
        disponibilidad_dto.fecha_creacion = entidad.fecha_creacion
        disponibilidad_dto.fecha_actualizacion = entidad.fecha_actualizacion
        disponibilidad_dto.propiedad_status = entidad.propiedad_status

        return disponibilidad_dto

    def entidad_list_a_dto_list(self, entidades: list[Disponibilidad]) -> list[DisponibilidadDTO]:
        entidades_dto = list()
        for e in entidades:
            entidades_dto.append(self.entidad_a_dto(entidad=e))
        return entidades_dto

    def dto_a_entidad(self, dto: DisponibilidadDTO) -> Disponibilidad:
        disponibilidad = Disponibilidad(
            id=dto.id,
            propiedad_id=dto.propiedad_id,
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion,
            propiedad_status=dto.propiedad_status
        )

        return disponibilidad

    def dto_list_a_entidad_list(self, dtos: list[DisponibilidadDTO]) -> list[Disponibilidad]:
        dtos_entidades = list()
        for d in dtos:
            dtos_entidades.append(self.dto_a_entidad(dto=d))
        return dtos_entidades
