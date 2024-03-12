from __future__ import annotations
from dataclasses import dataclass
from src.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class CaracterizacionCreada(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None


@dataclass
class CaracterizacionEliminado(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None


@dataclass
class CaracterizacionCreadaFallido(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None
