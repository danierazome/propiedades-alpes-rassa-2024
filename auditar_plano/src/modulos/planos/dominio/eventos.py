from __future__ import annotations
from dataclasses import dataclass
from src.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class TransacionIniciada(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None
    area_construida: str = None
    area_total: str = None
    zone: int = None
    floors: int = None


@dataclass
class AuditoriaCreada(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None
    area_construida: str = None
    area_total: str = None
    zone: int = None
    floors: int = None
    status: str = None


@dataclass
class PlanoCreado(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None
    zone: int = None
    floors: int = None
    status: str = None


@dataclass
class CaracterizacionCreada(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None

# DELETED EVENTS


@dataclass
class AuditoriaEliminada(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None


@dataclass
class PlanoEliminado(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None


@dataclass
class CaracterizacionEliminado(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None

# ERROR EVENTS


@dataclass
class AuditoriaCreadaFallida(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None


@dataclass
class PlanoCreadoFallido(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None


@dataclass
class CaracterizacionCreadaFallido(EventoDominio):
    id: str = None
    propiedad_id: str = None
    correlacion_id: str = None
