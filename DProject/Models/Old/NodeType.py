from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from server_api.Models2.base import Base


class NodeType(Base):
    __tablename__ = "nodetype"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    reference = Column(String(250))
    weight = Column(Float)
    size = Column(String)

    # Action

    actions = relationship("Action", back_populates="nodetype")

    def removeAction(self, actoin):
        self.actions.remove(actoin)

    def addAction(self, actoin):
        if actoin not in self.actions:
            if actoin.nodetype is not None:
                actoin.nodetype.removeAction(actoin)

            self.actions.append(actoin)

