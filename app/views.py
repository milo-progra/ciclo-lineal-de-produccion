from email import message
from time import process_time_ns
from django.shortcuts import get_object_or_404, redirect, render
from .models import AreaEmpresa, Entrada, Etapa, RegistroTrabajador, Salida, Oportunidades
from django.contrib import messages
from .forms import EntradaForm, SalidaForm, OportunidadForm
from user.models import Usuario


# Create your views here.
def home(request):
    # obj_cliente = User.objects.only('rut').get(rut=rut)
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        return render(request, 'home.html', {'registros': registros})
    else:
        return render(request, 'home.html')






def autoDiagnostico(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        return render(request, 'autodiagnostico/auto_diagnostico.html', {'registros': registros})
    else:
        return render(request, 'autodiagnostico/auto_diagnostico.html')


def extraccionMateriaPrima(request):
    if request.user.is_authenticated:

        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Extraccion materia prima")
        entradas = Entrada.objects.filter(usuario=request.user)
        # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
        print("La id de la etapa es!!!!!!!!: ", etapa)

        # data = {

        #     'form' : EntradaForm(),
        #     'registros':registros,
        #     'entradas':entradas,
        #     'formSalida': SalidaForm()

        # }
        print(f"la id del usuario es!!!!!!!!:", request.user.id)
        formulario = EntradaForm()
        formularioSalida = SalidaForm()

        if request.method == 'POST':
            formulario = EntradaForm(request.POST)
            formularioSalida = SalidaForm(request.POST)

            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                formulario.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                formulario = EntradaForm()

            if formularioSalida.is_valid():
                post = formularioSalida.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                formularioSalida.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                formulario = SalidaForm()
        return render(request, 'autodiagnostico/extraccion/home_extraccion.html', {'form': formulario, 'registros': registros, 'entradas': entradas})
    else:
        return render(request, 'autodiagnostico/extraccion/home_extraccion.html')


def agregarEntradaExtraccion(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Extraccion materia prima")
        entradas = Entrada.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)
     
        # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
        print("La id de la etapa es!!!!!!!!: ", etapa)
        print("La id del area es!!!!!!!!: ", areaTrabajador)

        # print("La id de la empresa es!!!!!!!!: ", empresa)
        data = {

            'form': EntradaForm(),
            'registros': registros,
            'entradas': entradas,
            'areaTrabajador': areaTrabajador

        }
        print(f"la id del usuario es!!!!!!!!:", request.user.id)

        if request.method == 'POST':
            formulario = EntradaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/extraccion/entrada/agregar_entrada.html', data)
    else:
        return render(request, 'autodiagnostico/extraccion/entrada/agregar_entrada.html')


def agregarSalidaExtraccion(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Extraccion materia prima")
        salidas = Salida.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': SalidaForm(),
            'registros': registros,
            'salidas': salidas

        }
        print(f"la id del usuario es!!!!!!!!:", request.user.id)

        if request.method == 'POST':
            formulario = SalidaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/extraccion/salida/agregar_salida.html', data)
    else:
        return render(request, 'autodiagnostico/extraccion/entrada/agregar_salida.html')




def agregarOportunidadExtraccion(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Extraccion materia prima")
        oportunidades = Oportunidades.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': OportunidadForm(),
            'registros': registros,
            'oportunidad': oportunidades

        }

        if request.method == 'POST':
            formulario = OportunidadForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/extraccion/oportunidad/agregar_oportunidad.html', data)
    else:
        return render(request, 'autodiagnostico/extraccion/oportunidad/agregar_oportunidad.html')







# Diseño y produccion

def diseño_Produccion(request):
    registros = RegistroTrabajador.objects.filter(usuario=request.user)

    data = {

            
            'registros': registros,
            

    }
    return render(request,'autodiagnostico/diseñoProduccion/home_diseño.html', data)


def agregarEntradaDiseño(request):
    if request.user.is_authenticated:

        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Diseño y produccion")
        entradas = Entrada.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)
        # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
        data = {

            'form': EntradaForm(),
            'registros': registros,
            'entradas': entradas

        }
        if request.method == 'POST':
            formulario = EntradaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/diseñoProduccion/entrada/agregar_entrada.html', data)
    else:
        return render(request, 'autodiagnostico/diseñoProduccion/entrada/agregar_entrada.html')



def agregarSalidaDiseño(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Diseño y produccion")
        salidas = Salida.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': SalidaForm(),
            'registros': registros,
            'salidas': salidas

        }

        if request.method == 'POST':
            formulario = SalidaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/diseñoProduccion/salida/agregar_salida.html', data)
    else:
        return render(request, 'autodiagnostico/diseñoProduccion/entrada/agregar_salida.html')

def agregarOportunidadDiseño(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Diseño y produccion")
        oportunidades = Oportunidades.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': OportunidadForm(),
            'registros': registros,
            'oportunidad': oportunidades

        }

        if request.method == 'POST':
            formulario = OportunidadForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/diseñoProduccion/oportunidad/agregar_oportunidad.html', data)
    else:
        return render(request, 'autodiagnostico/diseñoProduccion/oportunidad/agregar_oportunidad.html')


# logistica

def logistica(request):
    registros = RegistroTrabajador.objects.filter(usuario=request.user)

    data = {  
            'registros': registros, 
    }

    return render(request,'autodiagnostico/logistica/home_logistica.html', data)


def agregarEntradaLogistica(request):
    if request.user.is_authenticated:

        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Logistica")
        entradas = Entrada.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)
        # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
        data = {

            'form': EntradaForm(),
            'registros': registros,
            'entradas': entradas

        }
        if request.method == 'POST':
            formulario = EntradaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/logistica/entrada/agregar_entrada.html', data)
    else:
        return render(request, 'autodiagnostico/logistica/entrada/agregar_entrada.html')


def agregarSalidaLogistica(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Logistica")
        salidas = Salida.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': SalidaForm(),
            'registros': registros,
            'salidas': salidas

        }

        if request.method == 'POST':
            formulario = SalidaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/logistica/salida/agregar_salida.html', data)
    else:
        return render(request, 'autodiagnostico/logistica/entrada/agregar_salida.html')


def agregarOportunidadLogistica(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Logistica")
        oportunidades = Oportunidades.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': OportunidadForm(),
            'registros': registros,
            'oportunidad': oportunidades

        }

        if request.method == 'POST':
            formulario = OportunidadForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/logistica/oportunidad/agregar_oportunidad.html', data)
    else:
        return render(request, 'autodiagnostico/logistica/oportunidad/agregar_oportunidad.html')


#compra

def compra(request):
    registros = RegistroTrabajador.objects.filter(usuario=request.user)

    data = {  
            'registros': registros, 
    }

    return render(request,'autodiagnostico/compra/home_compra.html', data)


def agregarEntradaCompra(request):
    if request.user.is_authenticated:

        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Compra")
        entradas = Entrada.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)
        # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
        data = {

            'form': EntradaForm(),
            'registros': registros,
            'entradas': entradas

        }
        if request.method == 'POST':
            formulario = EntradaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/compra/entrada/agregar_entrada.html', data)
    else:
        return render(request, 'autodiagnostico/compra/entrada/agregar_entrada.html')   


def agregarSalidaCompra(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Compra")
        salidas = Salida.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': SalidaForm(),
            'registros': registros,
            'salidas': salidas

        }

        if request.method == 'POST':
            formulario = SalidaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/compra/salida/agregar_salida.html', data)
    else:
        return render(request,'autodiagnostico/compra/salida/agregar_salida.html')       


def agregarOportunidadCompra(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Compra")
        oportunidades = Oportunidades.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': OportunidadForm(),
            'registros': registros,
            'oportunidad': oportunidades

        }

        if request.method == 'POST':
            formulario = OportunidadForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/compra/oportunidad/agregar_oportunidad.html', data)
    else:
        return render(request, 'autodiagnostico/compra/oportunidad/agregar_oportunidad.html')        


#Uso consumo

def usoConsumo(request):
    registros = RegistroTrabajador.objects.filter(usuario=request.user)

    data = {  
            'registros': registros, 
    }

    return render(request,'autodiagnostico/usoConsumo/home_usoConsumo.html', data)        


def agregarEntradaUso(request):
    if request.user.is_authenticated:

        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Uso consumo")
        entradas = Entrada.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)
        # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
        data = {

            'form': EntradaForm(),
            'registros': registros,
            'entradas': entradas

        }
        if request.method == 'POST':
            formulario = EntradaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/usoConsumo/entrada/agregar_entrada.html', data)
    else:
        return render(request, 'autodiagnostico/usoConsumo/entrada/agregar_entrada.html')       


def agregarSalidaUso(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Uso consumo")
        salidas = Salida.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': SalidaForm(),
            'registros': registros,
            'salidas': salidas

        }

        if request.method == 'POST':
            formulario = SalidaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/usoConsumo/salida/agregar_salida.html', data)
    else:
        return render(request,'autodiagnostico/usoConsumo/salida/agregar_salida.html')       



def agregarOportunidadUso(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Uso consumo")
        oportunidades = Oportunidades.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': OportunidadForm(),
            'registros': registros,
            'oportunidad': oportunidades

        }

        if request.method == 'POST':
            formulario = OportunidadForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/usoConsumo/oportunidad/agregar_oportunidad.html', data)
    else:
        return render(request, 'autodiagnostico/usoConsumo/oportunidad/agregar_oportunidad.html')   


# Fin de vida

def finVida(request):
    registros = RegistroTrabajador.objects.filter(usuario=request.user)

    data = {  
            'registros': registros, 
    }

    return render(request,'autodiagnostico/finVida/home_finVida.html', data)


def agregarEntradaFin(request):
    if request.user.is_authenticated:

        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Fin de vida")
        entradas = Entrada.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)
        # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
        data = {

            'form': EntradaForm(),
            'registros': registros,
            'entradas': entradas

        }
        if request.method == 'POST':
            formulario = EntradaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Entrada Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/finVida/entrada/agregar_entrada.html', data)
    else:
        return render(request, 'autodiagnostico/finVida/entrada/agregar_entrada.html')       




def agregarSalidaFin(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Fin de vida")
        salidas = Salida.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': SalidaForm(),
            'registros': registros,
            'salidas': salidas

        }

        if request.method == 'POST':
            formulario = SalidaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/finVida/salida/agregar_salida.html', data)
    else:
        return render(request,'autodiagnostico/finVida/salida/agregar_salida.html')     



def agregarOportunidadFin(request):
    if request.user.is_authenticated:
        registros = RegistroTrabajador.objects.filter(usuario=request.user)
        etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Fin de vida")
        oportunidades = Oportunidades.objects.filter(usuario=request.user)
        areaTrabajador = RegistroTrabajador.objects.values_list("id_area", flat=True).filter(usuario = request.user)

        data = {

            'form': OportunidadForm(),
            'registros': registros,
            'oportunidad': oportunidades

        }

        if request.method == 'POST':
            formulario = OportunidadForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                post = formulario.save(commit=False)
                post.nombre = request.POST["nombre"]
                post.usuario_id = request.user.id
                post.etapa_id = etapa
                post.id_area_id = areaTrabajador
                formulario.save()
                messages.success(request, "Salida Registrada con exito")
            else:
                data["form"] = formulario
        return render(request,'autodiagnostico/finVida/oportunidad/agregar_oportunidad.html', data)
    else:
        return render(request, 'autodiagnostico/finVida/oportunidad/agregar_oportunidad.html') 