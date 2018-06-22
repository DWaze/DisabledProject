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

import json

import datetime


class StatusManager(object):

    DBSession = None
    objectDao = None
    objectIot = None

    def __init__(self):
        self.DBSession = createSession()
        self.objectDao = ObjectDAO(self.DBSession)
        setup()

    def getStatus(self):

        objects = self.objectDao.findAll()

        results = self.normalize(objects)

        return results

    def closeSession(self):
        self.DBSession.close()

    def normalize(self, objects):

        resultList = []
        json_string = None

        for object in objects:
            result = Empty()
            result.objectName = object.name
            result.longitude = object.longitude
            result.latitude = object.latitude
            result.state = object.state
            result.weight = object.weight
            result.size = object.size
            resultList.append(result)
            json_string = json.dumps([result.__dict__ for result in resultList])

        return json_string
