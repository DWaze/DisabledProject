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
from sqlalchemy import create_engine



class DAO(object):
    __metaclass__ = abc.ABCMeta
    DBSession = object()

    def __init__(self,DBSession):
        self.DBSession = DBSession

    @abc.abstractmethod
    def create(self,object):
        """Abstract Creation DAO"""
        return

    @abc.abstractmethod
    def delete(self,object):
        """Abstract Delete DAO"""
        return

    @abc.abstractmethod
    def update(self, object):
        """Abstract Update DAO"""
        return

    @abc.abstractmethod
    def find(self, id):
        """Abstract Select by id DAO"""
        return

    @abc.abstractmethod
    def findAll(self):
        """Abstract Select All DAO"""
        return








