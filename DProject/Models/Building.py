from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base
import json

class Building(Base):
    __tablename__ = "building"
    id = Column(Integer, primary_key=True)
    address = Column(String(100))
    floor = Column(Integer)
    typeBuilding = Column(String(250))
    country = Column(String(250))
    city = Column(String(250))
    longitude = Column(Float)
    latitude = Column(Float)

    def __init__(self, address="", floor=0, typeBuilding="", country="", city="", longitude=0.0, latitude=0.0):
        self.address = address
        self.floor = floor
        self.typeBuilding = typeBuilding
        self.country = country
        self.city = city
        self.longitude = longitude
        self.latitude = latitude



    # Agents

    agents = relationship("Agent", back_populates="building")
    agentSup = relationship("Agent", uselist=False, back_populates="building")

    def removeAgent(self, agent):
        self.agents.remove(agent)

    def addAgent(self, agent):
        if agent not in self.agents:
            if agent.building is not None:
                agent.building.removeAgent(agent)

            self.agents.append(agent)

    def addAgentSup(self, agentSup):
        if agentSup.building is not None:
            agentSup.building = None

        if self.agentSup is not None:
            self.agentSup.building = None

        self.agentSup = agentSup
        agentSup.building = self

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

