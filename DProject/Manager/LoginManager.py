from DProject.Manager.MainManager import createSession
from DProject.DAO.AccountDAO import AccountDAO
from DProject.DAO.UserDAO import UserDAO
import datetime
import uuid
from datetime import timedelta
from DProject.Models.Empty import Empty
from DProject.Models.Account import Account
from DProject.Models.User import User
import abc
import DProject.Models.base
import DProject.Models.Account
import DProject.Models.Action
import DProject.Models.ActionHistory
import DProject.Models.Agent
import DProject.Models.Building
import DProject.Models.Object
import DProject.Models.GPIOPins
import DProject.Models.Scenario
import DProject.Models.StateHistory
import DProject.Models.Area
import DProject.Models.User
from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker


class LoginManager(object):

    DBSession = None

    def __init__(self):
        self.DBSession = createSession()

    def normalize(self,account):
        accountObject = Empty()
        accountObject.id = account.id
        accountObject.userName = account.userName
        accountObject.password = account.password
        accountObject.email = account.email
        accountObject.type = account.type
        accountObject.token = account.token
        accountObject.tokenEndDate = account.tokenEndDate.strftime('%m/%d/%Y')
        accountObject.enabled = account.enabled
        accountObject.lastLogin = account.lastLogin.strftime('%m/%d/%Y')
        accountObject.firstAccess = account.firstAccess.strftime('%m/%d/%Y')
        accountObject.lastAccess = account.lastAccess.strftime('%m/%d/%Y')
        return accountObject

    def GetLoginInfo(self, username, password):
        accountDAO = AccountDAO(self.DBSession)
        # accountTest = Account("redha","1321","mail@mail.com")
        # accountDAO.create(accountTest)
        #
        # userDAO = UserDAO(self.DBSession)
        # userTest = User("Abbassen","Mohamed Redha",22,datetime.datetime.now(),"0665528461","cite 1000 logts","Constantine","Countery")
        # userTest.addAccount(accountTest)
        # userDAO.create(userTest)

        account = accountDAO.findLogin(username,password)

        dNow = datetime.datetime.now()
        if hasattr(account, 'userName'):
            dToken = account.tokenEndDate
            if (dNow > dToken or account.token is None):
                new_token = uuid.uuid4().hex
                account.token = new_token
                account.tokenEndDate = dNow + timedelta(days=15)
                accountDAO.update(account)
                accountObject = self.normalize(account)
                return accountObject
            else:
                accountObject = self.normalize(account)
                return accountObject
        else:
            return []

    def check_token(self,token):
        accountDAO = AccountDAO(self.DBSession)
        account = accountDAO.findByToken(token)
        dNow = datetime.datetime.now()
        if hasattr(account, 'userName'):
            dToken = account.tokenEndDate
            if (dNow > dToken or account.token is None):
                return False
            else:
                return account