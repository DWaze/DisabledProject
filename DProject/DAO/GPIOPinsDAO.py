from DProject.DAO.DAO import DAO
from sqlalchemy import exc
from sqlalchemy import delete
from DProject.Models.GPIOPins import GPIOPins


class GPIOPinsDAO(DAO):

    def __init__(self,DBSession):
        super(GPIOPinsDAO, self).__init__(DBSession)

    def create(self, pin):
        session = self.DBSession
        try:
            session.add(pin)
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def delete(self, pin):
        try:
            session = self.DBSession
            session.delete(pin)
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!", self.__class__.__name__)

    def update(self, pin):
        session = self.DBSession
        try:
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def find(self, id):
        session = self.DBSession
        try:
            pin = session.query(GPIOPins).get(id)
            return pin
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []

    def findAll(self):
        session = self.DBSession
        try:
            pins = session.query(GPIOPins).all()
            return pins
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []