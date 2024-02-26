from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class PropiedadStatus(str, Enum):
    POR_DEFINIR = "POR_DEFINIR"
    EN_ARRIENDO = "EN_ARRIENDO"
    EN_VENTA = "EN_VENTA"
    NO_DISPONIBLE = "NO_DISPONIBLE"
