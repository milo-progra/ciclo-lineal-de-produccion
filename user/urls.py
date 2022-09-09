from unicodedata import name
from django.contrib import admin
from django.urls import  path
from .views import *
#from .views import home

urlpatterns = [
    path('registro/', registro, name="registro"),
    path('agregar_area/<id>/', AgregarArea, name="agregar_Area"),
    path('agregar_telegram/<id>/', agregraIDtelegram, name = "agregar_telegram"),
    path('registro_usuarios/',registro_usuario, name="registro_usuarios")
]