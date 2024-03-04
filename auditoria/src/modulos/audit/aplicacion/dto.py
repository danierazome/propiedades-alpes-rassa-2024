from dataclasses import dataclass, field
from src.seedwork.aplicacion.dto import DTO
from datetime import datetime


@dataclass(frozen=True)
class ResponseAuditoriaDTO(DTO):
    id: str = field(default_factory=str)
    propiedad_id: str = field(default_factory=str)
    fecha_creacion: datetime = None
    fecha_actualizacion: datetime = None
    assessment: str = field(default_factory=str)
    client: str = field(default_factory=str)
    status: str = field(default_factory=str)
