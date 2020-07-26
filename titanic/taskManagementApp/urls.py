
from django.urls import path
from . import views

urlpatterns = [
    path('tell', views.tell,name='tell'),
    path('delete/<list_id>', views.delete,name='delete'),
]
