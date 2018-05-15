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
from sqlalchemy.orm import sessionmaker


def createSession():
    engine = create_engine("sqlite:///iot.db")
    DProject.Models.base.Base.metadata.create_all(engine, checkfirst=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session