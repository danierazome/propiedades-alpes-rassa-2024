from src.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, \
    CoordinadorCompensacion, TransaccionCompensacion
from src.seedwork.aplicacion.comandos import Comando
from src.seedwork.dominio.eventos import EventoDominio

from src.modulos.planos.aplicacion.comandos.crear_auditoria import CrearAuditoria
from src.modulos.planos.aplicacion.comandos.eliminar_auditoria import EliminarAuditoria
from src.modulos.planos.aplicacion.comandos.crear_plano import CrearPlano
from src.modulos.planos.aplicacion.comandos.eliminar_plano import EliminarPlano
from src.modulos.planos.aplicacion.comandos.crear_caracterizacion import CrearCaract
from src.modulos.planos.aplicacion.comandos.eliminar_caract import EliminarCaract
from src.modulos.planos.dominio.eventos import AuditoriaCreada, AuditoriaCreadaFallida, \
    PlanoCreado, PlanoCreadoFallido, CaracterizacionCreada, CaracterizacionCreadaFallido, \
    AuditoriaEliminada, PlanoEliminado, CaracterizacionEliminado
from src.modulos.planos.infraestructura.fabricas import FabricaRepositorio
from src.modulos.planos.infraestructura.repositorios import RepositorioSagaLog
from src.modulos.planos.infraestructura.dto import SagaLog
from src.modulos.planos.dominio.eventos import TransacionIniciada

from datetime import datetime
import uuid


class CoordinadorAuditoriaPlanos(CoordinadorOrquestacion):

    transaccion_type: str = 'OPERACION'

    def inicializar_pasos(self, db):
        self.pasos = [
            Inicio(index=0, evento=TransacionIniciada),
            Transaccion(index=1, comando=CrearAuditoria,
                        evento=AuditoriaCreada),
            Transaccion(index=2, comando=CrearPlano, evento=PlanoCreado),
            Transaccion(index=3, comando=CrearCaract,
                        evento=CaracterizacionCreada)
        ]
        self.db = db

    def persistir_en_saga_log(self, mensaje):
        fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(
            RepositorioSagaLog.__class__)
        saga_log = SagaLog(
            id=str(uuid.uuid4()),
            correlation_id=mensaje.correlacion_id,
            fecha=datetime.now(),
            index=self.index,
            type=self.transaccion_type
        )
        repositorio.agregar(saga_log)
        self.db.session.commit()

    def construir_comando(self, evento: EventoDominio):
        print('---------------CONSTRUIR COMANDO')
        print(self.index)

        if self.index == 1:
            print('----------------1')
            return CrearAuditoria(evento=evento)
        elif self.index == 2:
            print('----------------2')
            return CrearPlano(evento=evento)

        elif self.index == 3:
            print('----------------3')
            return CrearCaract(evento=evento)


# COMPENSACION

class CoordinadorCompensacionAuditoriaPlanos(CoordinadorCompensacion):

    transaccion_type: str = 'COMPENSACION'

    def inicializar_pasos(self, db):
        self.pasos = [
            TransaccionCompensacion(index=1, comando=EliminarCaract,
                                    evento=CaracterizacionEliminado, evento_error=CaracterizacionCreadaFallido),
            TransaccionCompensacion(index=2, comando=EliminarPlano,
                                    evento=PlanoEliminado, evento_error=PlanoCreadoFallido),
            TransaccionCompensacion(index=3, comando=EliminarAuditoria,
                                    evento=AuditoriaEliminada, evento_error=AuditoriaCreadaFallida)
        ]
        self.db = db

    def persistir_en_saga_log(self, mensaje):
        fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(
            RepositorioSagaLog.__class__)
        saga_log = SagaLog(
            id=str(uuid.uuid4()),
            correlation_id=mensaje.correlacion_id,
            fecha=datetime.now(),
            index=self.index,
            type=self.transaccion_type
        )
        repositorio.agregar(saga_log)
        self.db.session.commit()

    def construir_comando(self, evento: EventoDominio):
        if self.index == 0:
            return EliminarAuditoria(evento=evento)
        elif self.index == 1:
            return EliminarPlano(evento=evento)
        elif self.index == 2:
            return EliminarCaract(evento=evento)
