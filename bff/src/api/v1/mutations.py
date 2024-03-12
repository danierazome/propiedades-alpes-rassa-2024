import strawberry
import typing

from strawberry.types import Info
from ...utils import *
from ...dispatchers import Despachador

from .schemes import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear_reserva(self, propiedad_id: str, floors: int, zone: int, area_total: str, area_construida: str,info: Info) -> PlanosRespuesta:
        payload = dict(
            propiedad_id = propiedad_id,
            floors = floors,
            zone = zone,
            area_total = area_total,
            area_construida = area_construida
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=time_millis(),
            specversion = "v1",
            type = "ComandoPlanos",
            ingestion=time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "actualizar-plano", "public/default/actualizar-plano")
        
        return PlanosRespuesta(mensaje="Procesando Mensaje", codigo=203)