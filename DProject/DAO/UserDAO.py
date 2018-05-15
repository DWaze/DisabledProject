from DProject.DAO.DAO import DAO
from sqlalchemy import exc
from sqlalchemy import delete
from DProject.Models.User import User


class UserDAO(DAO):

    def __init__(self,DBSession):
        super(UserDAO, self).__init__(DBSession)

    def create(self, user):
        session = self.DBSession
        try:
            session.add(user)
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def delete(self, user):
        try:
            session = self.DBSession
            session.delete(user)
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!", self.__class__.__name__)

    def update(self, user):
        session = self.DBSession
        try:
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def find(self, id):
        session = self.DBSession
        try:
            user = session.query(User).get(id)
            return user
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []

    def findAll(self):
        session = self.DBSession
        try:
            users = session.query(User).all()
            return users
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []