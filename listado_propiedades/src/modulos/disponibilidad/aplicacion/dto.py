from dataclasses import dataclass, field
from src.seedwork.aplicacion.dto import DTO
from datetime import datetime


@dataclass(frozen=True)
class DisponibilidadDTO(DTO):
    propiedad_id: str = field(default_factory=str)
    fecha_creacion: datetime = None
    fecha_actualizacion: datetime = None
    propiedad_status: str = field(default_factory=str)


@dataclass(frozen=True)
class ResponseDisponibilidadDTO(DTO):
    id: str = field(default_factory=str)
    propiedad_id: str = field(default_factory=str)
    fecha_creacion: datetime = None
    fecha_actualizacion: datetime = None
    propiedad_status: str = field(default_factory=str)
