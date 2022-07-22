from ast import Try
from email import message
from pdb import post_mortem
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import RegistroTrabajadorForm, UsuarioForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from app.models import AreaEmpresa
from .models import Usuario

# Create your views here.


def registro(request):
    data = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"]) #resibir usuario y password para hacer un login automatico
            #login(request, user)
            #message.success(request, 'Te has registrado correctamente')
            return redirect(to='home')
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)


# area de trabajo


def AgregarArea(request, id):
    if request.method == "POST":
        try:
            
            #codigo a ejecutar
            #podria haber un error en este bloque
            action = str(request.POST['action'])
            if str(action) == 'buscar_area':
                
                data = [] #creo una array vasio
                for i in AreaEmpresa.objects.filter(id_empresa = request.POST['id']):
                    data.append({'area' : i.id_area, 'nombre': i.nombre}) #me agregara estos iteam al final de la lista hasta que termine el for
                return JsonResponse(data, safe=False)

        except:
            # Haz esto para manejar la excepcion
            # El bloque except se ejecutara si el bloque try lanza un error
            form = RegistroTrabajadorForm(request.POST)
            
            if form.is_valid():
                post = form.save(commit = False)
                post.id_usuario = Usuario.objects.only('id').get(id=id)
                post.id_area = AreaEmpresa.objects.get(id_area = request.POST['id_area'])
                post.descripcion = request.POST['descripcion']
                post.save()
                return redirect(to='home')
    else:
        print("No es un post!!!!")
        form =  RegistroTrabajadorForm
    return render(request, 'area/agregar_area.html', {'form':form})
    




    # data = {
    #     'form' : RegistroTrabajadorForm()
    # }
    # if request.method == 'POST':
    #     formulario = RegistroTrabajadorForm(data = request.POST)
    #     if formulario.is_valid():
    #         formulario.save()
    #         return redirect(to='home')
    #     data['form'] = formulario #si el form no es valido
    # return render(request, 'area/agregar_area.html', data)


# class AgregarArea(TemplateView):
#     template_name = "agregar_area.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Select Anidados | Django'
#         return context




#if request.method == "POST":
    #     data = {}
    #     for i in AreaEmpresa.objects.filter(id_empresa = request.POST['id']):
    #         data.append({'id' : i.id_area, 'nombre': i.nombre})
    #     try:
    #         action = request.POST['action']
    #         if action == 'buscar_area':
    #             pass
    #         else:
    #             data['error'] = 'ha ocurrido un error'
    #         # codigo a ejecutar
    #         # podria haber un error en este bloque

    #     except Exception as e:
    #         data['error'] = str(e)
           
    #     return JsonResponse(data, safe=False)
  

    #         # Haz esto para manejar la excepcion
    #         # El bloque except se ejecutara si el bloque try lanza un error
    # return render(request, 'area/agregar_area.html')