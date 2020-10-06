"""titanic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from taskManagementApp import views
from . import views
from . import views0
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome,name='welcome'),
    path('index/', views.index,name='index'),
    path('result/', views.result,name='result'),
    path('it/', views0.it,name='it'),
    path('ann/', views0.ann,name='ann'),
    path('prophet/', views0.prophet,name='prophet'),
    path('orders/', views0.orders,name='orders'),
    path('annresult/', views0.annresult,name='annresult'),
    path('result0/', views0.result0,name='result0'),
    path('analysis/', views0.analysis,name='analysis'),
    path('analysis1/', views0.analysis1,name='analysis1'),
    path('analysis0/', views0.analysis0,name='analysis0'),
    path('hr/', views.hr,name='hr'),
    path('hrresult/', views.hrresult,name='hrresult'),
    path('hrranalysis/', views.hrranalysis,name='hrranalysis'),
    path('hranalysismore/', views.hranalysismore,name='hranalysismore'),
    path('sigmoid/', views.sigmoid,name='sigmoid'),
    path('pearl/', views.pearl,name='pearl'),
    path('analysisC/',views0.analysisC,name='analysisC'),
    path('nlp/',views0.nlp,name='nlp'),
    path('nlpresult/',views0.nlpresult,name='nlpresult'),
    path('', include('taskManagementApp.urls')),
]
