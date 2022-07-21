from email import message
from pdb import post_mortem
from django.shortcuts import redirect, render
from .forms import RegistroTrabajadorForm, UsuarioForm
from django.contrib.auth import authenticate, login

# Create your views here.
def registro(request):
    data = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"]) #resibir usuario y password para hacer un login automatico
            #login(request, user)
            #message.success(request, 'Te has registrado correctamente')
            return redirect(to='home')
        data["form"] = formulario   


    return render(request,'registration/registro.html', data)


#area de trabajo

def AgregarArea(request):
    data = {
        'form' : RegistroTrabajadorForm()
    }
    if request.method == 'POST':
        formulario = RegistroTrabajadorForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='home')
        data['form'] = formulario #si el form no es valido    
    return render(request, 'area/agregar_area.html', data)    