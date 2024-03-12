import uuid
from src.seedwork.infraestructura.utils import time_millis
from pulsar.schema import *


class Mensaje(Record):
    id = String(default=str(uuid.uuid4()))
    ingestion = Long(default=time_millis())
    version = String()
    client = String()
    fecha_creacion = Float()
