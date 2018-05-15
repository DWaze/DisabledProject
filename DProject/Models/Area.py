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

    # Agent

    agentID = Column(Integer, ForeignKey('agent.id'))
    agent = relationship("Agent", back_populates="areas")

    def addAgent(self, agent):
        if self not in agent.areas:
            if self.agent is not None:
                agent.removeArea(self)
            self.agent = agent

    # Objects

    objects = relationship("Object")

    def addObject(self,object):
        if object not in self.objects :
            self.objects.append(object)