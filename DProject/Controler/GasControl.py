from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from DProject.Manager.GasManager import GasManager
# from managers.LightManager import LightManager
from DProject.Controler.AlchemyEncoder import AlchemyEncoder
import json
from DProject.Models.Empty import Empty
from DProject.Manager.LoginManager import LoginManager


@method_decorator(csrf_exempt)
def detection(request):
    if request.method == 'POST':
        try:
            info = request.body.decode('utf-8')
            data = json.loads(info)
        except ValueError:
            print("loads")
            return JsonResponse({},status=400)
        token = data.get("token")
        if token:
            lManager = LoginManager()
            account = lManager.check_token(token)
            if hasattr(account, 'userName'):
                gasManager = GasManager()
                # gasManager.createObject()
                result = gasManager.detection()

                gasManager.closeSession()

                return HttpResponse(result)
            else:
                result = '{"response":"invalid token"}'
            return HttpResponse(result)
        else:
            return JsonResponse({}, status=401)
    return JsonResponse({}, status=400)


@method_decorator(csrf_exempt)
def prevention(request):
    if request.method == 'POST':
        try:
            info = request.body.decode('utf-8')
            data = json.loads(info)
        except ValueError:
            print("loads")
            return JsonResponse({},status=400)
        token = data.get("token")
        if token:
            lManager = LoginManager()
            account = lManager.check_token(token)
            if hasattr(account, 'userName'):
                gasManager = GasManager()
                # gasManager.createObject()
                responce = gasManager.prevention()
                gasManager.closeSession()

                return HttpResponse(responce)
            else:
                result = '{"response":"invalid token"}'
            return HttpResponse(result)
        else:
            return JsonResponse({}, status=401)
    return JsonResponse({}, status=400)

