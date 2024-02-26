import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


def registrar_handlers():
    import src.modulos.disponibilidad.aplicacion
    import src.modulos.caracterizacion.aplicacion


def importar_modelos_alchemy():
    import src.modulos.disponibilidad.infraestructura.dto
    import src.modulos.caracterizacion.infraestructura.dto


def comenzar_consumidor():
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    import threading
    import src.modulos.disponibilidad.infraestructura.consumidores as cliente
    import src.modulos.caracterizacion.infraestructura.consumidores as vuelos

    # # Suscripción a eventos
    # threading.Thread(target=cliente.suscribirse_a_eventos).start()
    # threading.Thread(target=vuelos.suscribirse_a_eventos).start()

    # # Suscripción a comandos
    # threading.Thread(target=cliente.suscribirse_a_comandos).start()
    # threading.Thread(target=vuelos.suscribirse_a_comandos).start()


def create_app(configuracion={}):

    from src.seedwork.infraestructura.utils import database_url

    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url()

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

    # Inicializa la DB
    from src.config.db import init_db
    init_db(app)

    from src.config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor()

     # Importa Blueprints
    from . import caracterizacion
    from . import disponibilidad

    # Registro de Blueprints
    app.register_blueprint(caracterizacion.bp)
    app.register_blueprint(disponibilidad.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
