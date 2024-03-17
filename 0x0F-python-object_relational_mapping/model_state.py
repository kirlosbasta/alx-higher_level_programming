#!/usr/bin/python3
'''Module contain class definition of a State'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer


Base = declarative_base()
class State(Base):
    '''Class state that inhierites from Base and define states table'''
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, autoincrement='auto')
    name = Column('name', String(128), nullable=False)
