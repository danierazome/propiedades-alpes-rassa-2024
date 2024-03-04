from __future__ import annotations
from dataclasses import dataclass, field

import src.modulos.planos.dominio.objetos_valor as ov
from .eventos import PlanoCreado
from src.seedwork.dominio.entidades import AgregacionRaiz
import uuid


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

    def crear_plano(self, plano: Plano):
        self.id = str(uuid.uuid4())
        self.status = ov.Status.POR_AUDITAR

        evento = PlanoCreado(
            propiedad_id=plano.propiedad_id,
            area_construida=plano.area_construida,
            area_total=plano.area_total,
            zone=plano.zone,
            floors=plano.floors,
            client='PLANOS'
        )

        self.agregar_evento(evento)

    def set_status_rechazado(self):
        self.status = ov.Status.RECHAZADO

    def set_status_auditado(self):
        self.status = ov.Status.AUDITADO
