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
from django.urls import path
from . import views
from . import views0
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name='home'),
    path('result/', views.result,name='result'),
    path('itil/', views0.itil,name='itil'),
    path('result0/', views0.result0,name='result0'),
    path('analysis/', views0.analysis,name='analysis'),
    path('analysis0/', views0.analysis0,name='analysis0'),
    path('analysisC/',views0.analysisC,name='analysisC')
]
