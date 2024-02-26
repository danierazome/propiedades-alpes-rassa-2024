from src.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

Base = db.declarative_base()


class Caracterizacion(db.Model):
    __tablename__ = 'caracterizacion'
    id = db.Column(db.String, primary_key=True)
    propiedad_id = db.Column(db.String)
    fecha_creacion = db.Column(db.DateTime, nullable=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=True)
    floors = db.Column(db.Integer, nullable=True)
    zone = db.Column(db.Integer, nullable=True)
    type = db.Column(db.String, nullable=True)
    status = db.Column(db.String, nullable=True)
