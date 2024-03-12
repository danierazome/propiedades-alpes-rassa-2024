from src.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

Base = db.declarative_base()


class SagaLog(db.Model):
    __tablename__ = 'saga_log'
    id = db.Column(db.String, primary_key=True)
    correlation_id = db.Column(db.String)
    fecha = db.Column(db.DateTime, nullable=True)
    index = db.Column(db.Integer, nullable=True)
    type = db.Column(db.String, nullable=True)
