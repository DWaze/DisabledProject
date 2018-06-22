from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from DProject.Manager.FanManager import FanManager
# from managers.LightManager import LightManager
from DProject.Controler.AlchemyEncoder import AlchemyEncoder
import json
from DProject.Models.Empty import Empty
from DProject.Manager.LoginManager import LoginManager


@method_decorator(csrf_exempt)
def fanOn(request):
    if request.method == 'POST':
        try:
            info = request.body.decode('utf-8')
            data = json.loads(info)
        except ValueError:
            print("loads")
            return JsonResponse({},status=400)
        token = data.get("token")
        object_id = data.get("id")
        if token:
            lManager = LoginManager()
            account = lManager.check_token(token)
            if hasattr(account, 'userName'):
                fanManager = FanManager()
                # fanManager.createObject()
                result = fanManager.fanOn(object_id)

                responce = json.dumps(result.__dict__)
                fanManager.closeSession()

                return HttpResponse(responce)
            else:
                result = '{"response":"invalid token"}'
            return HttpResponse(result)
        else:
            return JsonResponse({}, status=401)
    return JsonResponse({}, status=400)


@method_decorator(csrf_exempt)
def fanOff(request):
    if request.method == 'POST':
        try:
            info = request.body.decode('utf-8')
            data = json.loads(info)
        except ValueError:
            print("loads")
            return JsonResponse({},status=400)
        token = data.get("token")
        object_id = data.get("id")
        if token:
            lManager = LoginManager()
            account = lManager.check_token(token)
            if hasattr(account, 'userName'):
                fanManager = FanManager()
                result = fanManager.fanOff(object_id)
                responce = json.dumps(result.__dict__)
                fanManager.closeSession()

                return HttpResponse(responce)
            else:
                result = '{"response":"invalid token"}'
            return HttpResponse(result)
        else:
            return JsonResponse({}, status=401)
    return JsonResponse({}, status=400)

