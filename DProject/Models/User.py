from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base
import datetime


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    firstName = Column(String(250))
    lastName = Column(String(250))
    age = Column(Integer)
    birthDate = Column(DateTime, default=datetime.datetime.utcnow)
    phoneNumber = Column(String(250))
    address = Column(String(250))
    city = Column(String(250))
    country = Column(String(250))


    def __init__(self, firstName, lastName, age, birthDate, phoneNumber, address, city,country):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.birthDate = birthDate
        self.phoneNumber = phoneNumber
        self.address = address
        self.city = city
        self.country = country



    # ActionHistories

    actionHistories = relationship("ActionHistory", back_populates="user")

    def removeActionH(self, actionH):
        self.actionHistories.remove(actionH)

    def addActionH(self, actionH):
        if actionH not in self.actionHistories:
            if actionH.user is not None:
                actionH.user.removeActionH(actionH)

            self.actionHistories.append(actionH)

    # Account

    accountID = Column(Integer, ForeignKey('account.id'))
    account = relationship("Account", back_populates="user")

    def addAccount(self, account):
        if account.user is not None:
            account.user = None

        if self.account is not None:
            self.account.user = None

        self.account = account
