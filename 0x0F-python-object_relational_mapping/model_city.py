#!/usr/bin/python3
'''Module contain class definition of a City'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, ForeignKey
from model_state import Base


class City(Base):
    '''Class City that inhierites from Base and define cities table'''
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, autoincrement='auto')
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'))
