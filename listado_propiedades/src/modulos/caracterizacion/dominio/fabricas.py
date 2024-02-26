""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Caracterizacion
from src.modulos.caracterizacion.infraestructura.dto import Caracterizacion as CaracterizacionDTO
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from src.seedwork.dominio.repositorios import Mapeador, Repositorio
from src.seedwork.dominio.fabricas import Fabrica
from src.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass


# @dataclass
# class _FabricaReserva(Fabrica):
#     def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
#         if isinstance(obj, Entidad):
#             return mapeador.entidad_a_dto(obj)
#         else:
#             reserva: Reserva = mapeador.dto_a_entidad(obj)

#             self.validar_regla(MinimoUnItinerario(reserva.itinerarios))
#             [self.validar_regla(RutaValida(
#                 ruta)) for itin in reserva.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]

#             return reserva


@dataclass
class _FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, list):
            return mapeador.entidad_list_a_dto_list(obj)
        elif isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            return mapeador.dto_a_entidad(obj)


@dataclass
class FabricaCaracterizacion(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        fabrica_propiedad = _FabricaPropiedad()
        return fabrica_propiedad.crear_objeto(obj, mapeador)


@dataclass
class _FabricaPropiedadInfra(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, list):
            return mapeador.dto_list_a_entidad_list(obj)
        elif isinstance(obj, Caracterizacion):
            return mapeador.entidad_a_dto(obj)
        else:
            return mapeador.dto_a_entidad(obj)


@dataclass
class FabricaCaracterizacionInfra(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        fabrica_propiedad = _FabricaPropiedadInfra()
        return fabrica_propiedad.crear_objeto(obj, mapeador)
