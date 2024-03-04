import pulsar
from pulsar.schema import *

from src.modulos.audit.infraestructura.schema.v1.comandos import ComandoActualizarCaract, \
    ComandoActualizarPlano, ComandoActualizarCaractPayload, ComandoActualizarPlanoPayload
from src.seedwork.infraestructura import utils


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(
            topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando_actualizar_plano(self, comando, topico):
        payload = ComandoActualizarPlanoPayload(
            propiedad_id=comando.propiedad_id,
            status=comando.status
        )
        comando_integracion = ComandoActualizarPlano(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoActualizarPlano))

    def publicar_comando_actualizar_caracterizacion(self, comando, topico):
        payload = ComandoActualizarCaractPayload(
            propiedad_id=comando.propiedad_id,
            status=comando.status,
            zone=comando.zone,
            floors=comando.floors)

        comando_integracion = ComandoActualizarCaract(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoActualizarCaract))
