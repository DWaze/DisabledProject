from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base


class Agent(Base):
    __tablename__ = "agent"
    id = Column(Integer, primary_key=True)
    ipAddress = Column(String(100))


    def __init__(self, ipAddress="169.254.255.254"):
        self.ipAddress = ipAddress


    # Building

    buildingId = Column(Integer, ForeignKey("building.id"))
    building = relationship("Building", back_populates="agents")

    def addBuildingSup(self, building):
        if building.agentSup is not None:
            building.agentSup = None

        if self.building is not None:
            self.building.agentSup = None

        self.building = building
        building.agentSup = self

    def addBuilding(self, building):
        if self not in building.agents:
            if self.building is not None:
                building.removeAgent(self)
            self.building = building


    # Area

    areas = relationship("Area", back_populates="agent")

    def removeArea(self, area):
        self.areas.remove(area)

    def addArea(self, area):
        if area not in self.areas:
            if area.agent is not None:
                area.agent.removeArea(area)

            self.areas.append(area)


    # GPIO Pins

    pins = relationship("GPIOPins")

    def addPin(self, pin):
        if pin not in self.pins:
            self.pins.append(pin)