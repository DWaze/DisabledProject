from DProject.DAO.DAO import DAO
from sqlalchemy import exc
from sqlalchemy import delete
from DProject.Models.ActionHistory import ActionHistory


class ActionHistoryDAO(DAO):

    def __init__(self,DBSession):
        super(ActionHistoryDAO, self).__init__(DBSession)

    def create(self, actionHistory):
        session = self.DBSession
        try:
            session.add(actionHistory)
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def delete(self, actionHistory):
        try:
            session = self.DBSession
            session.delete(actionHistory)
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!", self.__class__.__name__)

    def update(self, actionHistory):
        session = self.DBSession
        try:
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def find(self, id):
        session = self.DBSession
        try:
            actionHistory = session.query(ActionHistory).get(id)
            return actionHistory
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []

    def findAll(self):
        session = self.DBSession
        try:
            actionHistories = session.query(ActionHistory).all()
            return actionHistories
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []