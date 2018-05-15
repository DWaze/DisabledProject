from DProject.DAO.DAO import DAO
from sqlalchemy import exc
from sqlalchemy import delete
from DProject.Models.StateHistory import StateHistory


class StateHistoryDAO(DAO):

    def __init__(self,DBSession):
        super(StateHistoryDAO, self).__init__(DBSession)

    def create(self, sHistory):
        session = self.DBSession
        try:
            session.add(sHistory)
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def delete(self, sHistory):
        try:
            session = self.DBSession
            session.delete(sHistory)
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!", self.__class__.__name__)

    def update(self, sHistory):
        session = self.DBSession
        try:
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def find(self, id):
        session = self.DBSession
        try:
            sHistory = session.query(StateHistory).get(id)
            return sHistory
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []

    def findAll(self):
        session = self.DBSession
        try:
            sHistories = session.query(StateHistory).all()
            return sHistories
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []