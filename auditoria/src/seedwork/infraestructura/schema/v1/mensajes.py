import uuid

from pulsar.schema import *
from src.seedwork.infraestructura.utils import time_millis


class Mensaje(Record):
    id = String(default=str(uuid.uuid4()))
    ingestion = Long(default=time_millis())
    version = String()
    client = String()
