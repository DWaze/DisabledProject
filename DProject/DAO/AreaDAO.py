from DProject.DAO.DAO import DAO
from sqlalchemy import exc
from sqlalchemy import delete
from DProject.Models.Area import Area


class AreaDAO(DAO):

    def __init__(self,DBSession):
        super(AreaDAO, self).__init__(DBSession)

    def create(self, area):
        session = self.DBSession
        try:
            session.add(area)
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def delete(self, area):
        try:
            session = self.DBSession
            session.delete(area)
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!", self.__class__.__name__)

    def update(self, area):
        session = self.DBSession
        try:
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def find(self, id):
        session = self.DBSession
        try:
            building = session.query(Area).get(id)
            return building
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []

    def findAll(self):
        session = self.DBSession
        try:
            buildings = session.query(Area).all()
            return buildings
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []