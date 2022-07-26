from django.contrib import admin
from django.urls import  path
from .views import home, agregarEntrada, agregarSalida, agregarOportunidad, autoDiagnostico, extraccionMateriaPrima, diseño_Produccion

urlpatterns = [
    path('', home, name="home"),
    path('auto_diagnostico', autoDiagnostico, name="auto_diagnostico"),
    #etapa extraccion materia prima
    path('extraccion_materiaPrima', extraccionMateriaPrima, name="extraccion_materiaPrima"),
    #etapa diseño y produccion
    path('diseño_Produccion', diseño_Produccion, name="diseño_Produccion"),
    path('agregar_entrada', agregarEntrada, name="agregar_entrada"),
    path('agregar_salida', agregarSalida, name="agregar_salida"),
    path('agregar_oportunidad', agregarOportunidad, name="agregar_oportunidad")
]