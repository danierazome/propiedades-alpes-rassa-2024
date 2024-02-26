from __future__ import annotations
from dataclasses import dataclass
from src.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class CaracterizacionCreada(EventoDominio):
    id: str = None
    propiedad_id: str = None
    status: str = None
