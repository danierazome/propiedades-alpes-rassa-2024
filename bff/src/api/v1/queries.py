import strawberry
from .schemes import *

@strawberry.type
class Query:
    reservas: typing.List[Caracterizacion] = strawberry.field(resolver=obtener_caracterizacion)