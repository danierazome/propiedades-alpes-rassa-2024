import strawberry
import typing

from strawberry.types import Info
from ...utils import *
from ...dispatchers import Despachador

from .schemes import *

APC_HOST = os.getenv("APC_HOST", default="localhost")


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def auditar_plano(self, propiedad_id: str, floors: int, zone: int, area_total: str, area_construida: str, info: Info) -> PlanosRespuesta:
        payload = dict(
            propiedad_id=propiedad_id,
            floors=floors,
            zone=zone,
            area_total=area_total,
            area_construida=area_construida
        )
        comando = dict(
            id=str(uuid.uuid4()),
            time=time_millis(),
            specversion="v1",
            type="ComandoPlanos",
            ingestion=time_millis(),
            datacontenttype="AVRO",
            service_name="BFF",
            data=payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(
            despachador.publicar_mensaje, comando, "caract-creado-v1", "public/default/caract-creado-v1")
        response = requests.post(f'http://{APC_HOST}/auditar-planos/',
                                 data=json.dumps(payload), headers=obtener_headers())

        return PlanosRespuesta(mensaje="Procesando", codigo=response.status_code)
