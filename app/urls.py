from django.contrib import admin
from django.urls import  path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('auto_diagnostico', autoDiagnostico, name="auto_diagnostico"),
    #etapa extraccion materia prima
    path('extraccion_materiaPrima', extraccionMateriaPrima, name="extraccion_materiaPrima"),
    path('agregar_entrada_extraccion', agregarEntradaExtraccion, name="agregar_entrada_extraccion"),
    path('agregar_salida_extraccion', agregarSalidaExtraccion, name="agregar_salida_extraccion"),
    path('agregar_oportunidad_extraccion', agregarOportunidadExtraccion, name="agregar_oportunidad_extraccion"),

    #etapa diseño y produccion
    path('diseño_Produccion', diseño_Produccion, name="diseño_Produccion"),
    path('agregar_entrada_diseño', agregarEntradaDiseño, name="agregar_entrada_diseño"),
    path('agregar_salida_diseño', agregarSalidaDiseño, name="agregar_salida_diseño"),
    path('agregar_oportunidad_diseño', agregarOportunidadDiseño, name="agregar_oportunidad_diseño"),

    #Etapa logistica
    path('logistica', logistica, name="logistica"),
    path('agregar_entrada_logistica', agregarEntradaLogistica, name="agregar_entrada_logistica"),
    path('agregar_salida_logistica', agregarSalidaLogistica, name="agregar_salida_logistica"),
    path('agregar_oportunidad_logistica', agregarOportunidadLogistica, name="agregar_oportunidad_logistica"),

    #Etapa compra
    path('compra', compra, name="compra"),
    path('agregar_entrada_compra', agregarEntradaCompra, name="agregar_entrada_compra"),
    path('agregar_salida_compra', agregarSalidaCompra, name="agregar_salida_compra"),
    path('agregar_oportunidad_compra', agregarOportunidadCompra, name="agregar_oportunidad_compra"),


    #Etapa Uso Consumo
    path('uso_consumo', usoConsumo, name="uso_consumo"),
    path('agregar_entrada_uso', agregarEntradaUso, name="agregar_entrada_uso"),
    path('agregar_salida_uso', agregarSalidaUso, name="agregar_salida_uso"),
    path('agregar_oportunidad_uso', agregarOportunidadUso, name="agregar_oportunidad_uso"),


    #Etapa fin de vida
    path('fin_vida', finVida, name="fin_vida"),
    path('agregar_entrada_fin', agregarEntradaFin, name="agregar_entrada_fin"),
    path('agregar_salida_fin', agregarSalidaFin, name="agregar_salida_fin"),
    path('agregar_oportunidad_fin', agregarOportunidadFin, name="agregar_oportunidad_fin"),


]