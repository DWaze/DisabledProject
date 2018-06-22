from DProject.Models.Empty import Empty
from DProject.Models.Object import Object
from DProject.Models.GPIOPins import GPIOPins
from DProject.Models.Agent import Agent
from DProject.Models.Area import Area

from DProject.DAO.ObjectDAO import ObjectDAO
from DProject.DAO.AgentDAO import AgentDAO
from DProject.DAO.GPIOPinsDAO import GPIOPinsDAO
from DProject.DAO.AreaDAO import AreaDAO

from DProject.Manager.MainManager import createSession

from DProject.Drivers.temp import run
from DProject.Drivers.temp import setup

import datetime


class TempManager(object):
    DBSession = None
    objectDao = None
    gpioPinDao = None
    agentDao = None
    objectIot = None
    agent = None
    area1 = None
    gpioPin = None

    def __init__(self):
        self.DBSession = createSession()
        self.objectDao = ObjectDAO(self.DBSession)
        # self.gpioPinDao = GPIOPinsDAO(self.DBSession)
        # self.agentDao = AgentDAO(self.DBSession)
        self.areaDAO = AreaDAO(self.DBSession)

        setup()

    def createObject(self):
        self.agent = Agent("192.168.1.109")
        self.agentDao.create(self.agent)
        self.objectIot = Object("Temperature Sensor", 23.25888, 12.567281, "Working", 20.25, "3cm")

        self.area1 = Area("Bedroom", 23.25, "room", 2)

        self.objectIot.addArea(self.area1)
        self.areaDAO.create(self.area1)

        self.objectDao.create(self.objectIot)


    def getTemp(self, id):
        res = run()

        objectNode = self.objectDao.find(id)

        results = self.normalize(objectNode, res)

        return results

    def closeSession(self):
        self.DBSession.close()

    def normalize(self, objectIot, temperature):
        result = Empty()
        result.objectName = objectIot.name
        result.temperature = temperature

        return result
