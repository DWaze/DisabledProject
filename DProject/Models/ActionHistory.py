from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base
import datetime


class ActionHistory(Base):
    __tablename__ = "actionhistory"
    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.datetime.utcnow)

    def __init__(self,date):
        self.date = date

    # Actions

    action_id = Column(Integer, ForeignKey('action.id'))
    action = relationship("Action", back_populates="actionHistories")

    def addAction(self, action):
        if self not in action.actionHistories:
            if self.action is not None:
                action.removeActionH(self)
            self.action = action

    # User

    userId = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="actionHistories")

    def addUser(self, user):
        if self not in user.actionHistories:
            if self.user is not None:
                user.removeActionH(self)
            self.user = user

