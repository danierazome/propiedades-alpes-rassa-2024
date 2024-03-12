from __future__ import annotations
from dataclasses import dataclass, field

from src.seedwork.dominio.entidades import AgregacionRaiz
import uuid
from datetime import datetime
from . import objetos_valor as ov


@dataclass
class SagaLog(AgregacionRaiz):
    id: str = field(default=str(uuid.uuid4()))
    correlation_id: str = field(default=str)
    fecha: datetime = field(default=datetime)
    index: int = field(default=int)
    type: str = field(default=str)


@dataclass
class Plano(AgregacionRaiz):
    id: str = field(default=str(uuid.uuid4()))
    propiedad_id: str = field(default=str)
    area_total: str = field(default=str)
    area_construida: str = field(default=str)
    floors: int = field(default=1)
    zone: int = field(default=1)
    status: ov.PropiedadStatus = field(
        default=ov.Status.POR_AUDITAR)
