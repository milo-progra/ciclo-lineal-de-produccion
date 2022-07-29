
from django.shortcuts import render
from app.models import RegistroTrabajador, Etapa, Entrada, Salida, Oportunidades


# Create your views here.

def homeAdmin(request):
    registros = RegistroTrabajador.objects.filter(id_usuario=request.user)

    data = {

            
            'registros': registros,
            

    }
    return render(request,'home_admin.html', data)




def entradasExtraccion(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Extraccion materia prima")
                entradas = Entrada.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'extraccion/entrada/tabla_entrada.html', data)
        else:
                return render(request, 'extraccion/entrada/tabla_entrada.html')

def SalidasExtraccion(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Extraccion materia prima")
                entradas = Salida.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'extraccion/salida/tabla_salida.html', data)
        else:
                return render(request, 'extraccion/salida/tabla_salida.html')
        

def OportunidadExtraccion(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Extraccion materia prima")
                entradas = Oportunidades.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'extraccion/oportunidad/tabla_oportunidad.html', data)
        else:
                return render(request, 'extraccion/oportunidad/tabla_oportunidad.html')



# Diseño y gestion     

def EntradaDiseño(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Diseño y produccion")
                entradas = Entrada.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'diseñoProduccion/entrada/tabla_entrada.html', data)
        else:
                return render(request, 'diseñoProduccion/entrada/tabla_entrada.html')

def salidaDiseño(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Diseño y produccion")
                entradas = Salida.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'diseñoProduccion/salida/tabla_salida.html', data)
        else:
                return render(request, 'diseñoProduccion/salida/tabla_salida.html')                              

def oportunidadDiseño(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Diseño y produccion")
                entradas = Oportunidades.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'diseñoProduccion/oportunidad/tabla_oportunidad.html', data)
        else:
                return render(request, 'diseñoProduccion/oportunidad/tabla_oportunidad.html')      


#logistica


def EntradaLogistica(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Logistica")
                entradas = Entrada.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'logistica/entrada/tabla_entrada.html', data)
        else:
                return render(request, 'logistica/entrada/tabla_entrada.html')


def salidaLogistica(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Logistica")
                entradas = Salida.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'logistica/salida/tabla_salida.html', data)
        else:
                return render(request, 'logistica/salida/tabla_salida.html') 


def oportunidadLogistica(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Logistica")
                entradas = Oportunidades.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'logistica/oportunidad/tabla_oportunidad.html', data)
        else:
                return render(request, 'logistica/oportunidad/tabla_oportunidad.html')                                     


# compra


def entradaCompra(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Compra")
                entradas = Entrada.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'compra/entrada/tabla_entrada.html', data)
        else:
                return render(request, 'compra/entrada/tabla_entrada.html')      

def salidaCompra(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Compra")
                entradas = Salida.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'compra/salida/tabla_salida.html', data)
        else:
                return render(request, 'compra/salida/tabla_salida.html') 


def oportunidadesCompra(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Compra")
                entradas = Oportunidades.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'compra/oportunidad/tabla_oportunidad.html', data)
        else:
                return render(request, 'compra/salida/tabla_oportunidad.html') 

#Uso consumo

def entradaUsoConsumo(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Uso consumo")
                entradas = Entrada.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'usoConsumo/entrada/tabla_entrada.html', data)
        else:
                return render(request, 'usoConsumo/entrada/tabla_entrada.html') 


def salidaUsoConsumo(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Uso consumo")
                entradas = Salida.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'usoConsumo/salida/tabla_salida.html', data)
        else:
                return render(request, 'usoConsumo/salida/tabla_salida.html')


def oportunidadUsoConsumo(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Uso consumo")
                entradas = Oportunidades.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'usoConsumo/oportunidad/tabla_oportunidad.html', data)
        else:
                return render(request, 'usoConsumo/oportunidad/tabla_oportunidad.html')



#Fin de vida
def entradaFin(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Fin de vida")
                entradas = Entrada.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'finVida/entrada/tabla_entrada.html', data)
        else:
                return render(request, 'finVida/entrada/tabla_entrada.html')               

def salidaFin(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Fin de vida")
                entradas = Salida.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'finVida/salida/tabla_salida.html', data)
        else:
                return render(request, 'finVida/salida/tabla_salida.html')

def oportunidadFin(request):

        if request.user.is_authenticated:

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Fin de vida")
                entradas = Oportunidades.objects.all()
                empresaArea = RegistroTrabajador.objects.all()
                
                # etapa = Etapa.objects.values_list("id_etapa", flat=True).filter(activo=True)
                print(etapa)

                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea

                }
       
                return render(request,'finVida/oportunidad/tabla_oportunidad.html', data)
        else:
                return render(request, 'finVida/oportunidad/tabla_oportunidad.html')
