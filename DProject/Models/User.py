from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from DProject.Models.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    firstName = Column(String(250))
    lastName = Column(String(250))
    age = Column(Integer)
    birthDate = Column(Date)
    phoneNumber = Column(String(250))
    address = Column(String(250))
    city = Column(String(250))
    country = Column(String(250))

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
