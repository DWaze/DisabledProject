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
from .Controler import GmailControler

urlpatterns = [
    url(r'^login', Authentification.login, name="login"),
    url(r'^Light/On', LightControl.LightON, name="Light On"),
    url(r'^Light/Off', LightControl.LightOff, name="Light Off"),
    url(r'^GetGMail', GmailControler.getGmail, name="GMail"),
]
