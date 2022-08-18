from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializers
from rest_framework import status
from django.http import Http404
from user.models import Usuario

# Create your views here.
class User_APIView(APIView):
    def get(self, request, format=None, *args, **kwarqs):
        usuario = Usuario.objects.filter(is_staff = False)
        serializer = UserSerializers(usuario, many=True)

        return Response(serializer.data)