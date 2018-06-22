from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base


class Area(Base):
    __tablename__ = "area"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    surface = Column(Float)
    areaType = Column(String(250))
    floorNBR = Column(Integer)

    def __init__(self, name, surface, areaType, floorNBR):
        self.name = name
        self.surface = surface
        self.areaType = areaType
        self.floorNBR = floorNBR

    # Agent

    agentID = Column(Integer, ForeignKey('agent.id'))
    agent = relationship("Agent", back_populates="areas")

    def addAgent(self, agent):
        if self not in agent.areas:
            if self.agent is not None:
                agent.removeArea(self)
            self.agent = agent

    # Objects

    objects = relationship("Object", back_populates="area")

    def removeObject(self, object):
        self.objects.remove(object)

    def addObject(self, object):
        if object not in self.objects:
            if object.area is not None:
                object.area.removeObject(object)

            self.objects.append(object)