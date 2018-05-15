from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base


class Object(Base):
    __tablename__ = "object"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    longitude = Column(Float)
    latitude = Column(Float)
    state = Column(String(250))
    weight = Column(Float)
    size = Column(String)


    def __init__(self, name, longitude, latitude, state, weight, size):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.state = state
        self.weight = weight
        self.size = size


    # Area ID

    area_id = Column(Integer, ForeignKey('area.id'))

    def removeIoTNode(self, iotNode):
        self.ioT_Nodes.remove(iotNode)

    def addIoTNode(self, iotNode):
        if iotNode not in self.ioT_Nodes:
            if iotNode.object is not None:
                iotNode.object.removeIoTNode(iotNode)

            self.ioT_Nodes.append(iotNode)

    # GPIO Pins

    pins = relationship("GPIOPins", back_populates="object")

    def addPin(self, pin):
        if pin not in self.pins:
            if pin.object is not None:
                pin.object.removePin(pin)

            self.pins.append(pin)

    def removePin(self, pin):
        self.pins.remove(pin)


    # StateHistory

    sHistories = relationship("StateHistory")

    def addStateHistory(self,sHistory):
        if sHistory not in self.sHistories :
            self.sHistories.append(sHistory)


    # Action

    actions = relationship("Action", back_populates="object")

    def removeAction(self, action):
        self.actions.remove(action)

    def addAction(self, action):
        if action not in self.actions:
            if action.object is not None:
                action.object.removeAction(action)

            self.actions.append(action)