from django.contrib import admin
from django.urls import  path
from .views import registro, AgregarArea
#from .views import home

urlpatterns = [
    path('registro/', registro, name="registro"),
    path('agregar_area/<id>/', AgregarArea, name="agregar_Area")
]