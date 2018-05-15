from DProject.Models.StateHistory import StateHistory
from DProject.Models.ActionHistory import ActionHistory
from DProject.Models.Action import Action
from DProject.Models.Object import Object
from DProject.Models.ActionHistory import ActionHistory

from DProject.DAO.ActionHistoryDAO import ActionHistoryDAO
from DProject.DAO.StateHistoryDAO import StateHistoryDAO
from DProject.DAO.ActionDAO import ActionDAO
from DProject.DAO.ObjectDAO import ObjectDAO

from DProject.Manager.MainManager import createSession

from DProject.Drivers.relay import changeOff
from DProject.Drivers.relay import changeOn
from DProject.Drivers.relay import setup

import datetime


class LightManager(object):
    DBSession = None
    AHDao = None
    SHDao = None
    actionDao = None
    objectDao = None
    SH = None
    AH = None
    action1 = None
    action2 = None
    objectIot = None

    def __init__(self):
        self.DBSession = createSession()
        self.AHDao = ActionHistoryDAO(self.DBSession)
        self.SHDao = StateHistoryDAO(self.DBSession)
        self.actionDao = ActionDAO(self.DBSession)
        self.objectDao = ObjectDAO(self.DBSession)
        setup()

    def createObject(self):
        self.objectIot = Object("Lamp", 23.25298, 12.565981, "Off", 100.25, "5cm")

        self.action1 = Action("Turning On", "Changing the state of the lamp to On")
        self.action2 = Action("Turning Off", "Changing the state of the lamp to Off")

        self.objectIot.addAction(self.action1)
        self.objectIot.addAction(self.action2)

        self.actionDao.create(self.action1)
        self.actionDao.create(self.action2)
        self.objectDao.create(self.objectIot)

    def lightOn(self):
        changeOn()
        self.AH = ActionHistory(datetime.datetime.now())
        self.AH.addAction(self.action1)
        self.SH = StateHistory(datetime.datetime.now(),"On")
        self.objectIot.addStateHistory(self.SH)

        self.SHDao.create(self.SH)
        self.AHDao.create(self.AH)
        self.objectDao.update(self.objectIot)

        results = [self.AH,self.SH,self.objectIot]

        return results

    def lightOff(self):
        changeOff()
        self.AH = ActionHistory(datetime.datetime.now())
        self.AH.addAction(self.action2)
        self.SH = StateHistory(datetime.datetime.now(),"Off")
        self.objectIot.addStateHistory(self.SH)

        self.SHDao.create(self.SH)
        self.AHDao.create(self.AH)
        self.objectDao.update(self.objectIot)

        results = [self.AH,self.SH,self.objectIot]

        return results

    def closeSession(self):
        self.DBSession.close()
