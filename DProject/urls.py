"""DisabledProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .Controler import Authentification
from .Controler import LightControl
from .Controler import FanControl
from .Controler import GmailControler
from .Controler import TempControl
from .Controler import GasControl
from .Controler import StatusControl
from .Controler import RGBControl

urlpatterns = [
    url(r'^login', Authentification.login, name="login"),
    url(r'^Light/On', LightControl.lightOn, name="Light On"),
    url(r'^Light/Off', LightControl.lightOff, name="Light Off"),
    url(r'^Fan/On', FanControl.fanOn, name="Fan On"),
    url(r'^Fan/Off', FanControl.fanOff, name="Fan Off"),
    url(r'^GetGMail', GmailControler.getGmail, name="GMail"),
    url(r'^GetTemperature', TempControl.getTemp, name="Temperature"),
    url(r'^GasDetection', GasControl.detection, name="GasDetection"),
    url(r'^GasPrevention', GasControl.prevention, name="GasPrevention"),
    url(r'^GetStatus', StatusControl.GetStatus, name="GetStatus"),
    url(r'^ChangeColor', RGBControl.SetColor, name='index'),
]
