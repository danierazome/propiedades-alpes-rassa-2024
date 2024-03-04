from __future__ import annotations
from dataclasses import dataclass
from src.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class PlanoAuditado(EventoDominio):
    id: str = None
    propiedad_id: str = None
    status: str = None


@dataclass
class PlanoCreado(EventoDominio):
    id: str = None
    propiedad_id: str = None
    area_construida: str = None
    area_total: str = None
    zone: int = None
    floors: int = None
    client: str = None


@dataclass
class ActualizarPlano(EventoDominio):
    id: str = None
    propiedad_id: str = None
    status: str = None


@dataclass
class ActualizarCaracterizacion(EventoDominio):
    id: str = None
    propiedad_id: str = None
    zone: int = None
    floors: int = None
    status: str = None
