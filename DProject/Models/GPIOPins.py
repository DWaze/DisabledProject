from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base


class GPIOPins(Base):
    __tablename__ = "gpioPins"
    id = Column(Integer, primary_key=True)
    nodePin = Column(String(250))
    gpioPin = Column(String(250))

    # Object

    object_id = Column(Integer, ForeignKey('object.id'))
    object = relationship("Object", back_populates="pins")

    def addObject(self, object):
        if self not in object.pins:
            if self.object is not None:
                object.removeObject(self)
            self.object = object


    # Agent

    agent_id = Column(Integer, ForeignKey('agent.id'))



