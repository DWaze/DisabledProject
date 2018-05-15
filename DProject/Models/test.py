from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime
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
import json


from DProject.Models.Role import Role
from DProject.Models.Role import Constraint
from DProject.Models.Account import Account
from DProject.Models.Agent import Agent
from DProject.Models.Building import Building
from DProject.DAO.BuildingDAO import BuildingDAO
from sqlalchemy.orm import sessionmaker



class Empty:
    pass

engine = create_engine("sqlite:///iot.db")
DProject.Models.base.Base.metadata.create_all(engine, checkfirst=True)

DBSession = sessionmaker(bind=engine)

session = DBSession()

buildingDAO = BuildingDAO(session)

building1 = Building("cite 100 logts", 3, "Office", "Algeria", "Constantine", 26.23655, 11.2165)
building2 = Building("cite 2003 logts", 3, "Coffee", "Algeria", "Constantine", 26.265165, 11.502165)
building3 = Building("cite 1100 logts", 3, "Shop", "Algeria", "Constantine", 26.270655, 11.216515)
building4 = Building("cite 900 logts", 3, "Restaurant", "Algeria", "Constantine", 26.34655, 11.782165)





buildingDAO.create(building1)
buildingDAO.create(building2)
buildingDAO.create(building3)
buildingDAO.create(building4)



buildingDAO.delete(building2)

building1.address = "Setif 100 cities 85"

buildingDAO.update(building1)

buildingGet1 = buildingDAO.find(1)

buidingObject = Empty()

buidingObject.id = buildingGet1.id
buidingObject.address = buildingGet1.address
buidingObject.floor = buildingGet1.floor
buidingObject.typeBuilding = buildingGet1.typeBuilding
buidingObject.country = buildingGet1.country
buidingObject.city = buildingGet1.city
buidingObject.longitude = buildingGet1.longitude
buidingObject.latitude = buildingGet1.latitude

json_string_result = json.dumps(buidingObject.__dict__)

allBuildings = buildingDAO.findAll()

print(json_string_result)
# a=secrets.token_urlsafe()
# print(a)

