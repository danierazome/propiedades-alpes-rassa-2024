from src.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

Base = db.declarative_base()


class Plano(db.Model):
    __tablename__ = 'plano'
    id = db.Column(db.String, primary_key=True)
    propiedad_id = db.Column(db.String)
    fecha_creacion = db.Column(db.DateTime, nullable=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=True)
    area_total = db.Column(db.String)
    area_construida = db.Column(db.String)
    floors = db.Column(db.Integer, nullable=True)
    zone = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String)
