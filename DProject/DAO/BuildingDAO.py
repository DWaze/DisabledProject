from DProject.DAO.DAO import DAO
from sqlalchemy import exc
from sqlalchemy import delete
from DProject.Models.Building import Building


class BuildingDAO(DAO):

    def __init__(self,DBSession):
        super(BuildingDAO, self).__init__(DBSession)

    def create(self, building):
        session = self.DBSession
        try:
            session.add(building)
            session.commit()
        except exc.SQLAlchemyError:
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def delete(self, building):
        try:
            session = self.DBSession
            session.delete(building)
        except exc.SQLAlchemyError:
            print("SQLAlchemy error in  class!", self.__class__.__name__)

    def update(self, building):
        session = self.DBSession
        try:
            session.commit()
        except exc.SQLAlchemyError:
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def find(self, id):
        session = self.DBSession
        try:
            building = session.query(Building).get(id)
            return building
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []

    def findAll(self):
        session = self.DBSession
        try:
            buildings = session.query(Building).all()
            return buildings
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []