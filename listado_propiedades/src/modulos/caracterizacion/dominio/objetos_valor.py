from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class Floors():
    floors: int


@dataclass(frozen=True)
class Zone():
    zone: int


class Status(str, Enum):
    POR_AUDITAR = "POR_AUDITAR"
    AUDITADO = "AUDITADO"
    RECHAZADO = "RECHAZADO"


class PropiedadType(str, Enum):
    INDUSTRIAL = "INDUSTRIAL"
    OFICINA = "OFICINA"
    MINORISTA = "MINORISTA"
