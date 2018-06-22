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

from DProject.Drivers.rgb import setup
from DProject.Drivers.rgb import run


import json

import datetime


class RGBManager(object):

    def setColor(self,color):

        color = int('0x' + color, 16)
        responce = run(color)

        return responce
