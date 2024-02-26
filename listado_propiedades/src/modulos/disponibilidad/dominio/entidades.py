from __future__ import annotations
from dataclasses import dataclass, field

import src.modulos.disponibilidad.dominio.objetos_valor as ov
from src.seedwork.dominio.entidades import AgregacionRaiz
import uuid


@dataclass
class Disponibilidad(AgregacionRaiz):
    id: str = field(default=str(uuid.uuid4()))
    propiedad_id: str = field(default=str(uuid.uuid4()))
    propiedad_status: ov.PropiedadStatus = field(
        default=ov.PropiedadStatus.POR_DEFINIR)
