from __future__ import annotations
from dataclasses import dataclass, field

import src.modulos.audit.dominio.objetos_valor as ov
from src.seedwork.dominio.entidades import AgregacionRaiz
import uuid
import random


@dataclass
class Auditoria(AgregacionRaiz):
    id: str = field(default=str(uuid.uuid4()))
    propiedad_id: str = field(default=str)
    assessment: str = field(default=str)
    client: str = field(default=str)
    status: ov.PropiedadStatus = field(
        default=ov.Status.POR_AUDITAR)

    def auditoria_rechazada(self):
        self.id = str(uuid.uuid4())
        self.status = ov.Status.RECHAZADO
        self.assessment = 'RECHZADO POR NORMA' + \
            str(random.randint(1, 30))

    def auditoria_aprobada(self):
        self.id = str(uuid.uuid4())
        self.status = ov.Status.AUDITADO
        self.assessment = 'PLANOS CUMPLEN CON NORMAS DE NEGOCIO'
