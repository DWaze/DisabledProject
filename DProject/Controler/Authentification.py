from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from DProject.Manager.LoginManager import LoginManager
import json


# 400	Bad Request
# 401	Unauthorized
# 200  	OK

@method_decorator(csrf_exempt)
def login(request):
    if request.method == 'POST':
        try:
            info=request.body.decode('utf-8')
            data = json.loads(info)
        except ValueError:
            print("loads")
            return JsonResponse({},status=400)
        username = data.get("username")
        password = data.get("password")
        if username and password:
            try:
                lManager = LoginManager()
                account = lManager.GetLoginInfo(username, password)
                if hasattr(account, 'userName'):
                    result = json.dumps(account.__dict__)
                else:
                    result = '{"response":"invalid user"}'
                return HttpResponse(result)
            except ObjectDoesNotExist:
                return JsonResponse({},status=401)
        else:
            return JsonResponse({},status=401)
    return JsonResponse({},status=400)

# class User (object):
#     username = ""
#     password = ""
#     pk = ""
#     email = ""
#     def __init__ (self, username,password,pk,email):
#         self.username = username
#         self.password = password
#         self.pk=pk
#         self.email = email
#
# def get_account_by_token(token):
#     if token :
#         try:
#             user_account = Account.objects.get(token=token)
#             tokenIssueDate=user_account.tokenIssueDate
#             return user_account
#             #  now = datetime.datetime.now()
#             #  if tokenIssueDate.timetz() > now:
#             #     return user_account
#             # else:
#             #   return
#         except ObjectDoesNotExist:
#             return
#     else:
#         return
#
# def has_permissions(user_account, iot_node):
#     constraint= Constraint.objects.filter(account=user_account)
#     for cons in constraint:
#         role=cons.role
#         iotnodes=role.iot_nodes.all()
#         for r_i in iotnodes:
#             if iot_node==r_i:
#                 return True
#     return False
#
#
# # def has_permission(user_account, iot_node):
# #     constraint= Constraint.objects.filter(account=user_account)
# #     for cons in constraint:
# #         role_iotnodes=Role_IoTNodes.objects.filter(role=cons.role)
# #         for r_i in role_iotnodes:
# #             if iot_node==r_i.iot_node:
# #                 return True
# #     return False
#
# def find_pass(request, account):
#     try:
#         user = User.objects.get(firstName=account)
#         return HttpResponse('10 =' + account)
#     except ObjectDoesNotExist:
#         return HttpResponse('-10 =' + account)
#
#
# def verify_user(request, data):
#     user = data.get("token")
#     if user:
#         try:
#             user = Account.objects.get(username=user)
#             return 200
#         except ObjectDoesNotExist:
#             return 401
#     else:
#         return 401



