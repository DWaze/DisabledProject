from DProject.Models.Empty import Empty
from DProject.Models.StateHistory import StateHistory
from DProject.Models.ActionHistory import ActionHistory
from DProject.Models.Action import Action
from DProject.Models.Object import Object
from DProject.Models.ActionHistory import ActionHistory
from DProject.Models.Area import Area

from DProject.DAO.ActionHistoryDAO import ActionHistoryDAO
from DProject.DAO.StateHistoryDAO import StateHistoryDAO
from DProject.DAO.ActionDAO import ActionDAO
from DProject.DAO.ObjectDAO import ObjectDAO
from DProject.DAO.AreaDAO import AreaDAO

from DProject.Manager.MainManager import createSession

from DProject.Drivers.relayfan import changeOff
from DProject.Drivers.relayfan import changeOn
from DProject.Drivers.relayfan import setup

import datetime


class FanManager(object):

    DBSession = None
    AHDao = None
    SHDao = None
    actionDao = None
    objectDao = None
    areaDAO = None
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
        setup()

    def createObject(self):
        self.objectIot = Object("Fan", 23.25298, 12.565981, "Off", 100.25, "5cm")

        self.action1 = Action("Turning On", "Changing the state of the Fan to On")
        self.action2 = Action("Turning Off", "Changing the state of the Fan to Off")

        self.area1 = Area("Bedroom",23.25,"room",2)

        self.objectIot.addAction(self.action1)
        self.objectIot.addAction(self.action2)

        self.objectIot.addArea(self.area1)

        self.actionDao.create(self.action1)
        self.actionDao.create(self.action2)
        self.areaDAO.create(self.area1)
        self.objectDao.create(self.objectIot)

    def fanOn(self,id):

        changeOn()

        objectNode = self.objectDao.find(id)

        self.AH = ActionHistory(datetime.datetime.now())
        self.AH.addAction(objectNode.actions[0])
        self.SH = StateHistory(datetime.datetime.now(),"On")
        objectNode.addStateHistory(self.SH)
        objectNode.state = "On"

        self.SHDao.create(self.SH)
        self.AHDao.create(self.AH)
        self.objectDao.update(objectNode)

        results = self.normalize(self.AH,self.SH,objectNode)

        return results

    def fanOff(self,id):
        changeOff()

        objectNode = self.objectDao.find(id)

        self.AH = ActionHistory(datetime.datetime.now())
        self.AH.addAction(objectNode.actions[1])
        self.SH = StateHistory(datetime.datetime.now(),"Off")
        objectNode.addStateHistory(self.SH)
        objectNode.state = "Off"

        self.SHDao.create(self.SH)
        self.AHDao.create(self.AH)
        self.objectDao.update(objectNode)

        results = self.normalize(self.AH,self.SH,objectNode)

        return results

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
