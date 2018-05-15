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


engine = create_engine("sqlite:///iot.db")
DProject.Models.base.Base.metadata.create_all(engine, checkfirst=True)

DBSession = sessionmaker(bind=engine)

session = DBSession()

# agent1 = Agent()
# agent1.ipAddress = "192.168.1.123"
# agent2 = Agent("192.168.1.124")
# agent3 = Agent("192.168.1.125")
# agent4 = Agent("192.168.1.126")
# agent5 = Agent("192.168.1.127")
#
# house1 = Building("Constantine 1000 log", 2, "A4", "Algeria", "Constantine", 32.256516, 25.2365165)
# house2 = Building("Setif 1000 log", 3, "A2", "Algeria", "Setif", 32.256516, 25.2365165)
# house3 = Building("El Elma 1000 log", 4, "A3", "Algeria", "El Elma", 32.256516, 25.2365165)
# house4 = Building("Mssila 1000 log", 5, "A1", "Algeria", "Mssila", 32.256516, 25.2365165)
# house5 = Building("Constantine 1023 log", 6, "A5", "Algeria", "Constantine", 32.256516, 25.2365165)
#
# house1.addAgent(agent1)
# house1.addAgent(agent2)
#
# house2.addAgent(agent1)
# house2.addAgent(agent3)
#
# house3.addAgent(agent1)
# house3.addAgent(agent5)
#
# agent4.addBuilding(house4)
#
# session.add_all([agent1, agent2, agent3, agent4, agent5, house1, house2, house3, house4, house5])
# session.commit()
#
# role1 = Role("admin")
# role2 = Role("sub-admin")
# role3 = Role("user")
#
# account1 = Account("redha", "mohamed", "mail@mail.com")
# account2 = Account("sami", "khammar", "mail@hotmail.com")
# account3 = Account("mega", "pupi", "gmai@mailo.com")
#
# constraint1 = Constraint(datetime.datetime.utcnow(), datetime.datetime.utcnow())
# constraint2 = Constraint(datetime.datetime.utcnow(), datetime.datetime.utcnow())
# constraint3 = Constraint(datetime.datetime.utcnow(), datetime.datetime.utcnow())
#
#
# account1.addConstraint(constraint1)
# role1.addConstraint(constraint1)
# account1.addConstraint(constraint1)
# role2.addConstraint(constraint2)
# account1.addConstraint(constraint2)
# role3.addConstraint(constraint3)
# account1.addConstraint(constraint3)
#
# account2.addConstraint(constraint1)
#
#
# session.add_all([role1, role2, role3, account1, account2, account3, constraint1, constraint2, constraint3])
# session.commit()


# accounts = session.query(Account).all()
#
# for account in accounts:
#     print(account.userName)
#
# for account in accounts:
#     account.userName="change"
#
# session.commit()
#
# accounts = session.query(Account).all()
#
# for account in accounts:
#     print(account.userName)

#
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

allBuildings = buildingDAO.findAll()

# a=secrets.token_urlsafe()
# print(a)