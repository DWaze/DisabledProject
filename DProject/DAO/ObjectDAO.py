from DProject.DAO.DAO import DAO
from sqlalchemy import exc
from sqlalchemy import delete
from DProject.Models.Object import Object


class ObjectDAO(DAO):

    def __init__(self,DBSession):
        super(ObjectDAO, self).__init__(DBSession)

    def create(self, object):
        session = self.DBSession
        try:
            session.add(object)
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def delete(self, object):
        try:
            session = self.DBSession
            session.delete(object)
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!", self.__class__.__name__)

    def update(self, object):
        session = self.DBSession
        try:
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def find(self, id):
        session = self.DBSession
        try:
            object = session.query(Object).get(id)
            return object
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []

    def findName(self, name):
        session = self.DBSession
        try:
            object = session.query(Object).filter(Object.name == name).first()
            return object
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!", self.__class__.__name__)
            return []

    def findAll(self):
        session = self.DBSession
        try:
            objects = session.query(Object).all()
            return objects
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []