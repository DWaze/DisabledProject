from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base


class Action(Base):
    __tablename__ = "action"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))

    def __init__(self, name, description):
        self.name =name
        self.description = description

    # Object

    object_id = Column(Integer, ForeignKey('object.id'))
    object = relationship("Object", back_populates="actions")

    def addObject(self, object):
        if self not in object.actions:
            if self.object is not None:
                object.removeAction(self)
            self.object = object

    # ActionHistory

    actionHistories = relationship("ActionHistory", back_populates="action")

    def removeActionH(self, actionHistorie):
        self.actionHistories.remove(actionHistorie)

    def addActionH(self, actionHistorie):
        if actionHistorie not in self.actionHistories:
            if actionHistorie.action is not None:
                actionHistorie.action.removeActionH(actionHistorie)

            self.actionHistories.append(actionHistorie)

    # Scenario

    orderActions = relationship("OrderAction",
                        back_populates="action")

    def removeOrderAction(self, orderAction):
        self.orderActions.remove(orderAction)

    def addOrderAction(self, orderAction):
        if orderAction not in self.orderActions:
            if orderAction.action is not None:
                orderAction.action.removeOrderAction(orderAction)
            orderAction.action = self