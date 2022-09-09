from ast import Try
from email import message
from pdb import post_mortem
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import RegistroTrabajadorForm, UsuarioForm, TelegramForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from app.models import AreaEmpresa, RegistroTrabajador
from .models import Usuario
from tablib import Dataset 
import csv
# Create your views here.


def registro(request):
    data = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # resibir usuario y password para hacer un login automatico
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password"])
            login(request, user)
            #message.success(request, 'Te has registrado correctamente')
            return redirect(to='auto_diagnostico')
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)


# area de trabajo


def AgregarArea(request, id):
    if request.method == "POST":
        try:

            # codigo a ejecutar
            # podria haber un error en este bloque
            action = str(request.POST['action'])
            if str(action) == 'buscar_area':

                data = []  # creo una array vasio
                for i in AreaEmpresa.objects.filter(id_empresa=request.POST['id']):
                    # me agregara estos iteam al final de la lista hasta que termine el for
                    data.append({'area': i.id_area, 'nombre': i.nombre})
                return JsonResponse(data, safe=False)

        except:
            # Haz esto para manejar la excepcion
            # El bloque except se ejecutara si el bloque try lanza un error
            form = RegistroTrabajadorForm(request.POST)

            if form.is_valid():
                post = form.save(commit=False)
                post.usuario = Usuario.objects.only('id').get(id=id)
                post.id_area = AreaEmpresa.objects.get(
                    id_area=request.POST['id_area'])
                post.descripcion = request.POST['descripcion']
                post.save()
                return redirect(to='auto_diagnostico')
    else:
        print("No es un post!!!!")
        form = RegistroTrabajadorForm
    return render(request, 'area/agregar_area.html', {'form': form})



def agregraIDtelegram(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    data = {
        'form': TelegramForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = TelegramForm(data= request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="home")
        else:
            data["form"] = formulario    
    return render(request, 'telegram/agregar_telegram.html', data)


def registro_usuario(request):
    pass
