from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializers
from rest_framework import status
from django.http import Http404
from user.models import Usuario
from app.models import RegistroTrabajador
import json
# Create your views here.

def home_api(request):
    if request.user.is_authenticated:
        
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        data = {
            'registros':registros
        }
        
    return render(request,'home_api.html',data)


class User_APIView(APIView):
    def get(self, request, format=None, *args, **kwarqs):
        usuario = Usuario.objects.filter(is_staff=False)
        serializer = UserSerializers(usuario, many=True)

        return Response(serializer.data)


class Ubicacion_APIView(APIView):
    def get(self, request, format=None, *args, **kwarqs):
        # with open("cicloProduccion/api/ubicacion/ubicacion1.json", 'r') as j:
        #     mydata = json.load(j)
        
        #Creo un diccionario vacio
        datos = {}
        
        #Creo un conjunto de datos llamada ubicacion, ese conjunto de datos tendra principalmente una lista vacia
        datos['ubicacion'] = []

        #creo 3 elementos para el conjunto de datos ubicacion
        ubicacion1 = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [289.3263383, -33.4409602]}, "properties": {
            "EMPRESA": "Panaderia FF", "AREA": "Casa Matriz", "Direccion": "Calle 1 Oficina 1 ", "COMUNA": "Santiago Centro"}}

        ubicacion2 = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [289.1893511, -33.3549203]}, "properties": {
            "EMPRESA": "Panaderia FF", "AREA": "Cocina", "Direccion": "Calle 2 Oficina 2 ", "COMUNA": "Quilicura"}}

        ubicacion3 = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [289.2523086, -33.5022488]}, "properties": {
            "EMPRESA": "Panaderia FF", "AREA": "Transporte", "Direccion": "Calle 3 Oficina 3 ", "COMUNA": "Cerrillos"}}


        #agrego los elementos al diccionario   al conjunto ubicacion
        datos['ubicacion'].append(ubicacion1)

        datos['ubicacion'].append(ubicacion2)

        datos['ubicacion'].append(ubicacion3)

        print(len(datos['ubicacion']))  # len indica la cantidad de elementos del array


        #ruta para pythonenywhere
        # with open("/home/miloVan/ciclo-lineal-de-produccion/api/ubicacion/ubicacion_json.json", 'w') as f:
        #     json.dump(datos, f)
        
        #Escribir los datos en un json
        with open("api/ubicacion/ubicacion_json.json", 'w') as f:
            json.dump(datos, f)
      
        # Lectura de datos del archivo json
        with open("api/ubicacion/ubicacion_json.json", 'r') as j:
            mydata = json.load(j)
    
        return Response(mydata)
