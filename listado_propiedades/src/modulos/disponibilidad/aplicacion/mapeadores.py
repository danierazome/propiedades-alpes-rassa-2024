from src.seedwork.dominio.repositorios import Mapeador
from .dto import DisponibilidadDTO, ResponseDisponibilidadDTO
from src.modulos.disponibilidad.dominio.entidades import Disponibilidad
from src.modulos.caracterizacion.dominio.eventos import CaracterizacionCreada
from src.seedwork.aplicacion.dto import Mapeador as AppMap
import uuid


class MapeadorDisponibilidad(Mapeador):

    def obtener_tipo(self) -> type:
        return Disponibilidad.__class__

    def dto_a_entidad(self, dto: CaracterizacionCreada) -> Disponibilidad:
        disponibilidad = Disponibilidad(
            id=str(uuid.uuid4()),
            propiedad_id=dto.propiedad_id
        )

        return disponibilidad

    def dto_list_a_entidad_list(self, dtos: list[DisponibilidadDTO]) -> list[Disponibilidad]:
        dtos_entidades = list()
        for d in dtos:
            dtos_entidades.append(self.dto_a_entidad(dto=d))
        return dtos_entidades

    def entidad_a_dto(self, entidad: Disponibilidad) -> ResponseDisponibilidadDTO:
        return ResponseDisponibilidadDTO(
            propiedad_id=entidad.propiedad_id,
            id=entidad.id,
            fecha_creacion=entidad.fecha_creacion,
            fecha_actualizacion=entidad.fecha_actualizacion,
            propiedad_status=entidad.propiedad_status)

    def entidad_list_a_dto_list(self, entidades: list[Disponibilidad]) -> list[ResponseDisponibilidadDTO]:
        entidades_dto = list()
        for e in entidades:
            entidades_dto.append(self.entidad_a_dto(entidad=e))
        return entidades_dto


class MapeadorDisponibilidadDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> DisponibilidadDTO:
        disponibilidad_dto = DisponibilidadDTO(
            propiedad_id=externo.get('propiedad_id'))

        return disponibilidad_dto

    def dto_a_externo(self, dto: DisponibilidadDTO) -> dict:
        return dto.__dict__

    def dto_list_a_externo(self, dtos: list[DisponibilidadDTO]) -> list:
        externo = list()
        for d in dtos:
            externo.append(self.dto_a_externo(d))
        return externo
