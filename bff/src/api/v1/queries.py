import strawberry
from .schemes import *

@strawberry.type
class Query:
    planos: typing.List[Caracterizacion] = strawberry.field(resolver=obtener_caracterizacion)