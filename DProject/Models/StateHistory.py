from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base
import datetime

class StateHistory(Base):
    __tablename__ = "statehistory"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    state = Column(String(250))

    def __init__(self,date,state):
        self.date= date
        self.state =state

    # Object

    object_id = Column(Integer, ForeignKey('object.id'))
