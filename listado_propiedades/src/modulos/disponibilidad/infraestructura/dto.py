from src.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

Base = db.declarative_base()


class Disponibilidad(db.Model):
    __tablename__ = 'disponibilidad'
    id = db.Column(db.String, primary_key=True)
    propiedad_id = db.Column(db.String)
    fecha_creacion = db.Column(db.DateTime, nullable=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=True)
    propiedad_status = db.Column(db.String, nullable=True)
