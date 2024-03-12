from __future__ import annotations
from dataclasses import dataclass
from src.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class PlanoCreado(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None
    zone: int = None
    floors: int = None
    status: str = None


@dataclass
class PlanoEliminado(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None


@dataclass
class PlanoCreadoFallido(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None
