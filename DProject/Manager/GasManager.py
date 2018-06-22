from DProject.Drivers import GasDetection, GasPrevention,rgb
from DProject.Models.Empty import Empty
from DProject.Models.StateHistory import StateHistory
from DProject.Models.ActionHistory import ActionHistory
from DProject.Models.Action import Action
from DProject.Models.Object import Object
from DProject.Models.Area import Area
from DProject.Models.ActionHistory import ActionHistory

from DProject.DAO.ActionHistoryDAO import ActionHistoryDAO
from DProject.DAO.StateHistoryDAO import StateHistoryDAO
from DProject.DAO.ActionDAO import ActionDAO
from DProject.DAO.ObjectDAO import ObjectDAO
from DProject.DAO.AreaDAO import AreaDAO

from DProject.Manager.MainManager import createSession

import DProject.Drivers.GasPrevention


import datetime


class GasManager(object):
    DBSession = None
    AHDao = None
    SHDao = None
    actionDao = None
    objectDao = None
    SH = None
    AH = None
    action1 = None
    action2 = None
    area1 = None
    objectIot = None

    def __init__(self):
        self.DBSession = createSession()
        self.AHDao = ActionHistoryDAO(self.DBSession)
        self.SHDao = StateHistoryDAO(self.DBSession)
        self.actionDao = ActionDAO(self.DBSession)
        self.objectDao = ObjectDAO(self.DBSession)
        self.areaDAO = AreaDAO(self.DBSession)

    def createObject(self):
        # self.objectIot = Object("Lamp", 23.25298, 12.565981, "Off", 100.25, "5cm")
        # self.objectIot = Object("Fan", 23.25298, 12.565981, "Off", 100.25, "5cm")
        #
        # self.action1 = Action("Turning On", "Changing the state of the Fan to On")
        # self.action2 = Action("Turning Off", "Changing the state of the Fan to Off")
        #
        # self.objectIot.addAction(self.action1)
        # self.objectIot.addAction(self.action2)
        #
        # self.actionDao.create(self.action1)
        # self.actionDao.create(self.action2)
        # self.objectDao.create(self.objectIot)

        self.objectIot = Object("LED", 23.25298, 12.565981, "Off", 100.25, "5cm")

        self.action1 = Action("Turning On", "Changing the state of the LED to On")
        self.action2 = Action("Turning Off", "Changing the state of the LED to Off")

        self.area1 = Area("Bedroom", 23.25, "room", 2)

        self.objectIot.addAction(self.action1)
        self.objectIot.addAction(self.action2)

        self.objectIot.addArea(self.area1)

        self.actionDao.create(self.action1)
        self.actionDao.create(self.action2)
        self.areaDAO.create(self.area1)
        self.objectDao.create(self.objectIot)

    def detection(self):
        GasDetection.setup()
        result = ""
        try:
            result = GasDetection.detect()
        except KeyboardInterrupt:
            GasDetection.destroy()
        return result

    def prevention(self):
        GasPrevention.setup()
        result = GasPrevention.prevention()

        name = ["LED","Fan"]
        led = self.objectDao.findName(name[0])
        fan = self.objectDao.findName(name[1])

        self.SH = StateHistory(datetime.datetime.now(),"Off")
        led.addStateHistory(self.SH)
        led.state = "Off"

        self.SHDao.create(self.SH)
        self.objectDao.update(led)

        self.SH = StateHistory(datetime.datetime.now(),"On")
        fan.addStateHistory(self.SH)
        fan.state = "On"

        self.SHDao.create(self.SH)
        self.objectDao.update(fan)

        # results = self.normalize(self.AH,self.SH,objectNode)

        return result

    def closeSession(self):
        self.DBSession.close()

    def normalize(self,AH,SH,objectIot):

        result = Empty()
        result.objectName = objectIot.name
        result.ActionName = AH.action.name
        result.ActionDescription = AH.action.description
        result.ActionDate = AH.date.strftime('%m/%d/%Y')
        result.stateDate = SH.date.strftime('%m/%d/%Y')
        result.stateChange = SH.state

        return result
