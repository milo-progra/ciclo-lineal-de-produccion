from pathlib import Path
from django.contrib import admin
from django.urls import  path
from .views import homeAdmin, home_empresa, tablasExtraccion, entradasExtraccion, SalidasExtraccion, OportunidadExtraccion, EntradaDiseño, salidaDiseño, oportunidadDiseño, EntradaLogistica, \
                salidaLogistica, oportunidadLogistica, entradaCompra, salidaCompra, oportunidadesCompra, entradaUsoConsumo, salidaUsoConsumo, oportunidadUsoConsumo, \
                entradaFin, salidaFin, oportunidadFin, tablasDiseño, tablasLogistica, tablasCompra, tablasUso, tablasFin, promedioArea, promedioHome, homeFrecuenciaDiseño, \
                homeFrecuenciaLogistica, homeFrecuenciaCompra, homeFrecuenciaUso, homeFrecuenciaFin, frecuenciaDiseño, frecuenciaLogistica, frecuenciaCompra, frecuenciaUso, \
                frecuenciaFin         

urlpatterns = [
    path('home_admin', homeAdmin, name='home_admin'),
    path('home_empresa/<id>/', home_empresa, name='home_empresa'),
    path('tablas_extraccion/<id>/', tablasExtraccion, name='tablas_extraccion'),
    path('tablas_diseño/<id>/', tablasDiseño, name='tablas_diseño'),
    path('tablas_logistica/<id>/', tablasLogistica, name='tablas_logistica'),
    path('tablas_compra/<id>/', tablasCompra, name='tablas_compra'),
    path('tablas_uso/<id>/', tablasUso, name='tablas_uso'),
    path('tablas_fin/<id>/', tablasFin, name='tablas_fin'),
    path('promedio_home/<id>/', promedioHome, name ='promedio_home' ),

    #Levenshtein
    path('promedio_area/<id>/', promedioArea, name='promedio_area'),


    #extraccion
    path('entradas_extraccion', entradasExtraccion, name='entradas_extraccion'),
    path('salidas_extraccion', SalidasExtraccion, name='salidas_extraccion'),
    path('oportuniades_extraccion', OportunidadExtraccion, name='oportuniades_extraccion'),
    #diseño
    path('entradas_diseño', EntradaDiseño, name='entradas_diseño'),
    path('salida_diseño', salidaDiseño, name='salida_diseño'),
    path('oportunidad_diseño', oportunidadDiseño, name='oportunidad_diseño'),
    path('home_frecuencia_diseño/<id>/', homeFrecuenciaDiseño, name='home_frecuencia_diseño'),
    path('frecuencia_diseño/<id>/', frecuenciaDiseño, name='frecuencia_diseño'),
    #logistica
    path('entradas_logistica', EntradaLogistica, name='entradas_logistica'),
    path('salida_logistica', salidaLogistica, name='salida_logistica'),
    path('oportunidad_logistica', oportunidadLogistica, name='oportunidad_logistica'),
    path('home_frecuencia_logistica/<id>/', homeFrecuenciaLogistica, name='home_frecuencia_logistica'),
    path('frecuencia_logistica/<id>/', frecuenciaLogistica, name='frecuencia_logistica'),
    #compra
    path('entradas_compra', entradaCompra, name='entradas_compra'),
    path('salida_compra', salidaCompra, name='salida_compra'),
    path('oportunidad_compra', oportunidadesCompra, name='oportunidad_compra'),
    path('home_frecuencia_compra/<id>/', homeFrecuenciaCompra, name='home_frecuencia_compra'),
    path('frecuencia_compra/<id>/', frecuenciaCompra, name='frecuencia_compra'),
    #Uso consumo
    path('entradas_uso', entradaUsoConsumo, name='entradas_uso'),
    path('salidas_uso', salidaUsoConsumo, name='salidas_uso'),
    path('oportunidad_uso', oportunidadUsoConsumo, name='oportunidad_uso'),
    path('home_frecuencia_uso/<id>/', homeFrecuenciaUso, name='home_frecuencia_uso'),
    path('frecuencia_uso/<id>/', frecuenciaUso, name='frecuencia_uso'),
    #fin de vida
    path('entrada_fin', entradaFin, name='entrada_fin'),
    path('salidas_fin', salidaFin, name='salidas_fin'),
    path('oportunidad_fin', oportunidadFin, name='oportunidad_fin'),
    path('home_frecuencia_fin/<id>/', homeFrecuenciaFin, name='home_frecuencia_fin'),
    path('frecuencia_fin/<id>/', frecuenciaFin, name='frecuencia_fin'),


]