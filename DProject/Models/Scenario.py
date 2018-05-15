from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base


class OrderAction(Base):
    __tablename__= 'orderAction'
    action_id = Column(Integer, ForeignKey('action.id'), primary_key=True)
    scenario_id = Column(Integer, ForeignKey('scenario.id'), primary_key=True)
    orderNum = Column(Integer)
    action = relationship("Action", back_populates="orderActions")
    scenario = relationship("Scenario", back_populates="orderActions")

    def __init__(self,orderNum):
        self.orderNum = orderNum

    def addAction(self, action):
        if self not in action.scenarios:
            if self.action is not None:
                self.action.removeScenario(self)
            self.action = action

    def addScenario(self, scenario):
        if self not in scenario.actions:
            if(self.scenario is not None):
                self.scenario.removeAction(self)
            self.scenario = scenario


class Scenario(Base):
    __tablename__ = "scenario"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))
    state = Column(String(250))

    # Action

    orderActions = relationship("OrderAction",
                            back_populates="scenario")

    def removeOrderAction(self, action):
        self.orderActions.remove(action)

    def addOrderAction(self, orderAction):
        if orderAction not in self.orderActions:
            if orderAction.scenario is not None:
                orderAction.scenario.removeOrderAction(orderAction)
            orderAction.scenario=self

