from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from DProject.Manager.LightManager import LightManager
# from managers.LightManager import LightManager
from DProject.Controler.AlchemyEncoder import AlchemyEncoder
import json
from DProject.Models.Empty import Empty


pinLED = 4

# def Light(request, node_id, action):
#     LM = LightManager(node_id)
#     if action.lower() == "true":
#         LM.start()
#         return HttpResponse("<h1> LED on</h1>")
#     elif action.lower() == "false":
#         LM.stop()
#         return HttpResponse("<h1> LED off</h1>")
#     elif action.lower() == "sos":
#         LM.sos()
#         return HttpResponse("<h1> LED SOS</h1>")
#     else:
#         return HttpResponse("<h1> incorrect request</h1>", status=status.HTTP_400_BAD_REQUEST)
#         # LM.start()
#         # return HttpResponse("<h1> LED " + node_id + ": " + action + "</h1>")

@method_decorator(csrf_exempt)
def LightON(request):

    lightManager = LightManager()
    lightManager.createObject()
    res = lightManager.lightOn()
    # AH = json.dumps(res[0], cls=AlchemyEncoder)
    # action = json.dumps(res[0].action, cls=AlchemyEncoder)
    # SH = json.dumps(res[1], cls=AlchemyEncoder)
    result = Empty()
    result.objectName = res[2].name
    result.ActionName = res[0].action.name
    result.ActionDescription = res[0].action.description
    result.ActionDate = res[0].date.strftime('%m/%d/%Y')
    result.stateDate = res[1].date.strftime('%m/%d/%Y')
    result.stateChange = res[1].state

    responce = json.dumps(result.__dict__)
    lightManager.closeSession()

    return HttpResponse(responce)

@method_decorator(csrf_exempt)
def LightOff(request):
    lightManager = LightManager()
    lightManager.createObject()
    res = lightManager.lightOff()
    # AH = json.dumps(res[0], cls=AlchemyEncoder)
    # action = json.dumps(res[0].action, cls=AlchemyEncoder)
    # SH = json.dumps(res[1], cls=AlchemyEncoder)
    result = Empty()
    result.objectName = res[2].name
    result.ActionName = res[0].action.name
    result.ActionDescription = res[0].action.description
    result.ActionDate = res[0].date.strftime('%m/%d/%Y')
    result.stateDate = res[1].date.strftime('%m/%d/%Y')
    result.stateChange = res[1].state

    responce = json.dumps(result.__dict__)
    lightManager.closeSession()


    return HttpResponse(responce)

