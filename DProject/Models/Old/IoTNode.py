from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from server_api.Models2.base import Base


class IoTNode(Base):
    __tablename__ = "iotnode"
    id = Column(Integer, primary_key=True)
    state = Column(String(250))

    # Object

    objectID = Column(Integer, ForeignKey('object.id'))
    object = relationship("Object", back_populates="ioT_Nodes")

    def addObject(self, object):
        if self not in object.ioT_Nodes:
            if self.object is not None:
                object.removeIoTNode(self)
            self.object = object

    # NodeType

    nodeType_id = Column(Integer, ForeignKey("nodetype.id"))
    nodeType = relationship("NodeType")

    def addNodeType(self, nodeType):
        self.nodeType = nodeType

    # Pins

    pins = relationship("Pins", back_populates="iotNode")

    def addPin(self, pin):
        if pin not in self.pins:
            if pin.iotNode is not None:
                pin.iotNode.removePin(pin)

            self.pins.append(pin)

    def removePin(self, pin):
        self.pins.remove(pin)


    # StateHistory

    sHistories = relationship("StateHistory")

    def addStateHistory(self,sHistory):
        if sHistory not in self.sHistories :
            self.sHistories.append(sHistory)

