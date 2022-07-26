from email import message
from time import process_time_ns
from django.shortcuts import get_object_or_404, redirect, render
from .models import Entrada, Etapa, RegistroTrabajador
from django.contrib import messages
from .forms import EntradaForm, SalidaForm, OportunidadForm
from user.models import Usuario
            

# Create your views here.
def home(request):
    #obj_cliente = User.objects.only('rut').get(rut=rut)
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(id_usuario = request.user )
        return render(request,'home.html', {'registros':registros})
    else:
        return render(request,'home.html')


def autoDiagnostico(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(id_usuario = request.user )
        return render(request,'autodiagnostico/auto_diagnostico.html', {'registros':registros})
    else:
        return render(request,'autodiagnostico/auto_diagnostico.html')



def extraccionMateriaPrima(request):
    if request.user.is_authenticated:

        registros = RegistroTrabajador.objects.filter(id_usuario = request.user )
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre = "Extraccion materia prima")
        entradas = Entrada.objects.filter(usuario = request.user )

        #etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
        print("La id de la etapa es!!!!!!!!: ", etapa)

        data = {

            'form' : EntradaForm(),
            'registros':registros,
            'entradas':entradas

        }
        print(f"la id del usuario es!!!!!!!!:", request.user.id)

        if request.method == 'POST':
            formulario = EntradaForm(data= request.POST, files= request.FILES)
            if formulario.is_valid():   
                post = formulario.save(commit = False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                formulario.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                data["form"] = formulario

        return render(request,'autodiagnostico/extraccion/home_extraccion.html', data )
    else:
        return render(request,'autodiagnostico/extraccion/home_extraccion.html')
  
 
def diseño_Produccion(request):
    if request.user.is_authenticated:

        registros = RegistroTrabajador.objects.filter(id_usuario = request.user )
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre = "Diseño y produccion")
        entradas = Entrada.objects.filter(usuario = request.user)

        #etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
        print("La id de la etapa es!!!!!!!!: ", etapa)

        data = {

            'form' : EntradaForm(),
            'registros':registros,
            'entradas':entradas

        }
        print(f"la id del usuario es!!!!!!!!:", request.user.id)

        if request.method == 'POST':
            formulario = EntradaForm(data= request.POST, files= request.FILES)
            if formulario.is_valid():   
                post = formulario.save(commit = False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                formulario.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                data["form"] = formulario

        return render(request,'autodiagnostico/diseñoProduccion/home_diseño.html', data )
    else:
        return render(request,'autodiagnostico/diseñoProduccion/home_diseño.html')
         


def agregarEntrada(request):
  
    #queryset(array de datos)
    #values_list()      = trae los valores que se encuentran dentro del queryset
    #flat=True          = Rompe el queryset para guardar solo el valor especificado 
    #get(pk=1)          = Busca la el registro con la primary key "1", al tener.filter() traigo el registro con el filtro especificado
    etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
    print("La id de la etapa es!!!!!!!!: ", etapa)

    data = {

        'form' : EntradaForm()
    }
    print(f"la id del usuario es!!!!!!!!:", request.user.id)

    if request.method == 'POST':
        formulario = EntradaForm(data= request.POST, files= request.FILES)
        if formulario.is_valid():   
            post = formulario.save(commit = False)
            post.nombre = request.POST["nombre"]
            post.usuario_id = request.user.id
            post.etapa_id = etapa
            formulario.save()
            messages.success(request, "Entrada Registrada con exito")
        else:
            data["form"] = formulario
    return render(request, 'entrada/agregar_entrada.html', data)            




def agregarSalida(request):
  
    #queryset(array de datos)
    #values_list()      = trae los valores que se encuentran dentro del queryset
    #flat=True          = Rompe el queryset para guardar solo el valor especificado 
    #get(pk=1)          = Busca la el registro con la primary key "1", al tener.filter() traigo el registro con el filtro especificado
    etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
    print("La id de la etapa es!!!!!!!!: ", etapa)

    data = {

        'form' : SalidaForm()
    }
    print(f"la id del usuario es!!!!!!!!:", request.user.id)

    if request.method == 'POST':
        formulario = SalidaForm(data= request.POST, files= request.FILES)
        if formulario.is_valid():   
            post = formulario.save(commit = False)
            post.nombre = request.POST["nombre"]
            post.usuario_id = request.user.id
            post.etapa_id = etapa
            formulario.save()
            messages.success(request, "Salida Registrada con exito")
        else:
            data["form"] = formulario
    return render(request, 'salida/agregar_salida.html', data)         


def agregarOportunidad(request):
  
    #queryset(array de datos)
    #values_list()      = trae los valores que se encuentran dentro del queryset
    #flat=True          = Rompe el queryset para guardar solo el valor especificado 
    #get(pk=1)          = Busca la el registro con la primary key "1", al tener.filter() traigo el registro con el filtro especificado
    etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
    print("La id de la etapa es!!!!!!!!: ", etapa)

    data = {

        'form' : OportunidadForm()
    }
    print(f"la id del usuario es!!!!!!!!:", request.user.id)

    if request.method == 'POST':
        formulario = OportunidadForm(data= request.POST, files= request.FILES)
        if formulario.is_valid():   
            post = formulario.save(commit = False)
            post.nombre = request.POST["nombre"]
            post.usuario_id = request.user.id
            post.etapa_id = etapa
            formulario.save()
            messages.success(request, "Salida Registrada con exito")
        else:
            data["form"] = formulario
    return render(request, 'oportunidad/agregar_oportunidad.html', data)             