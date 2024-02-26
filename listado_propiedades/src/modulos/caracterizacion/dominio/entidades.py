from __future__ import annotations
from dataclasses import dataclass, field

import src.modulos.caracterizacion.dominio.objetos_valor as ov
from src.modulos.caracterizacion.dominio.eventos import CaracterizacionCreada
from src.seedwork.dominio.entidades import AgregacionRaiz
import uuid


@dataclass
class Caracterizacion(AgregacionRaiz):
    id: str = field(default=str(uuid.uuid4()))
    propiedad_id: str = field(default=str(uuid.uuid4()))
    floors: ov.Floors = field(default=0)
    zone: ov.Zone = field(default_factory=ov.Zone)
    status: ov.Status = field(default=ov.Status.POR_AUDITAR)
    type: ov.PropiedadType = field(default_factory=ov.PropiedadType)

    def crear_caracterizacion(self, caracterizacion: Caracterizacion):
        self.propiedad_id = caracterizacion.propiedad_id
        self.id = str(uuid.uuid4())
        self.floors = caracterizacion.floors
        self.type = caracterizacion.type
        self.zone = caracterizacion.zone

        self.agregar_evento(CaracterizacionCreada(
            propiedad_id=self.propiedad_id, id=self.id, status=self.status))
