from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    POR_AUDITAR = "POR_AUDITAR"
    AUDITADO = "AUDITADO"
    RECHAZADO = "RECHAZADO"
