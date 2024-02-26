from dataclasses import dataclass, field
from src.seedwork.aplicacion.dto import DTO
from datetime import datetime


@dataclass(frozen=True)
class CaracterizacionDTO(DTO):
    propiedad_id: str = field(default_factory=str)
    floors: int = field(default_factory=int)
    zone: int = field(default_factory=int)
    type: str = field(default_factory=str)


@dataclass(frozen=True)
class ResponseCaracterizacionDTO(DTO):
    id: str = field(default_factory=str)
    propiedad_id: str = field(default_factory=str)
    floors: int = field(default_factory=int)
    zone: int = field(default_factory=int)
    type: str = field(default_factory=str)
    fecha_creacion: datetime = None
    fecha_actualizacion: datetime = None
    status: str = field(default_factory=str)
