from DProject.DAO.DAO import DAO
from sqlalchemy import exc
from sqlalchemy import delete
from DProject.Models.Account import Account


class AccountDAO(DAO):

    def __init__(self,DBSession):
        super(AccountDAO, self).__init__(DBSession)

    def create(self, account):
        session = self.DBSession
        try:
            session.add(account)
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def delete(self, account):
        try:
            session = self.DBSession
            session.delete(account)
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!", self.__class__.__name__)

    def update(self, account):
        session = self.DBSession
        try:
            session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)

    def find(self, id):
        session = self.DBSession
        try:
            account = session.query(Account).get(id)
            return account
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []

    def findLogin(self, username, password):
        session = self.DBSession
        try:
            account = session.query(Account).filter(Account.userName == username,Account.password == password).first()
            return account
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!", self.__class__.__name__)
            return []

    def findAll(self):
        session = self.DBSession
        try:
            accounts = session.query(Account).all()
            return accounts
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!",self.__class__.__name__)
            return []

    def findByToken(self,token):
        session = self.DBSession
        try:
            account = session.query(Account).filter(Account.token == token).first()
            return account
        except exc.SQLAlchemyError as e:
            print(e)
            print("SQLAlchemy error in  class!", self.__class__.__name__)
            return []