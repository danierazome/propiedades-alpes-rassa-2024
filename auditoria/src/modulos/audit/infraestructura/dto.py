from src.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

Base = db.declarative_base()


class Auditoria(db.Model):
    __tablename__ = 'auditoria'
    id = db.Column(db.String, primary_key=True)
    propiedad_id = db.Column(db.String)
    fecha_creacion = db.Column(db.DateTime, nullable=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=True)
    assessment = db.Column(db.String)
    client = db.Column(db.String)
    status = db.Column(db.String)
