from dataclasses import dataclass, field
from src.seedwork.aplicacion.dto import DTO
from datetime import datetime


@dataclass(frozen=True)
class PlanoDTO(DTO):
    propiedad_id: str = field(default_factory=str)
    fecha_creacion: datetime = None
    fecha_actualizacion: datetime = None
    area_total: str = field(default_factory=str)
    area_construida: str = field(default_factory=str)
    floors: int = field(default_factory=int)
    zone: int = field(default_factory=int)


@dataclass(frozen=True)
class ResponsePlanoDTO(DTO):
    id: str = field(default_factory=str)
    propiedad_id: str = field(default_factory=str)
    fecha_creacion: datetime = None
    fecha_actualizacion: datetime = None
    area_total: str = field(default_factory=str)
    area_construida: str = field(default_factory=str)
    floors: int = field(default_factory=int)
    zone: int = field(default_factory=int)
    status: str = field(default_factory=str)
