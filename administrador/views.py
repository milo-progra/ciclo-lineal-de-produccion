
from ast import For
from django.shortcuts import render
from app.models import RegistroTrabajador, Etapa, Entrada, Salida, Oportunidades, Empresa, AreaEmpresa
from django.db.models import Count





# Create your views here.

def homeAdmin(request):
    registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
    empresas = Empresa.objects.all()

    data = {

            
            'registros': registros,
            'empresas': empresas
            

    }
    return render(request,'home_admin.html', data)


def home_empresa(request, id):
    registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
    empresas = Empresa.objects.all()
    empresa = Empresa.objects.filter(id_empresa = id)

    data = {
            'registros': registros,  
            'empresa':empresa,
            'empresas':empresas
    }

    return render(request,'empresa_1/home_empresa.html', data)   




def tablasExtraccion(request,id):
        if request.user.is_authenticated:
                empresas = Empresa.objects.all()
                empresa = Empresa.objects.filter(id_empresa = id)

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapas = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Extraccion materia prima")
                etapa = Etapa.objects.get(nombre = "Extraccion materia prima") #trar solo la ID de la etapa "Extraccion materia prima"
                #empresa = Empresa.objects.get(id)
                empresaArea = RegistroTrabajador.objects.all()
                
                area = AreaEmpresa.objects.filter(id_empresa = id)
                entradas = Entrada.objects.filter(etapa_id = etapa)
                
                
                result = (Entrada.objects
                .values('id_area')
                .annotate(dcount=Count('id_area'))
                .order_by()
                )
                print("variable result!!!!!!!: ",result)

               

                theanswer = Entrada.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa) #requiere importar from django.db.models import Count
                print(theanswer)
                salidas_count = Salida.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
                
                oportunidad_count = Oportunidades.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
              
                t = theanswer[0]
                                
                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea,
                'area' : area,
                't': t,
                'theanswer': theanswer,
                'salidas_count':salidas_count,
                'oportunidad_count':oportunidad_count,
                'empresas':empresas,
                'empresa':empresa
                

                }
       
                return render(request,'empresa_1/tablas_extraccion.html', data)
        else:
                return render(request, 'empresa_1/tabla_extraccion.html')


def tablasDiseño(request,id):
        if request.user.is_authenticated:
                empresas = Empresa.objects.all()
                empresa = Empresa.objects.filter(id_empresa = id)

                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapas = Etapa.objects.values_list("id_etapa", flat=True).filter(nombre="Extraccion materia prima")
                etapa = Etapa.objects.get(nombre = "Diseño y produccion") #trar solo la ID de la etapa "Extraccion materia prima"
                #empresa = Empresa.objects.get(id)
                empresaArea = RegistroTrabajador.objects.all()
                
                area = AreaEmpresa.objects.filter(id_empresa = id)
                entradas = Entrada.objects.filter(etapa_id = etapa)
                
                
                result = (Entrada.objects
                .values('id_area')
                .annotate(dcount=Count('id_area'))
                .order_by()
                )
                print("variable result!!!!!!!: ",result)

               

                theanswer = Entrada.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa) #requiere importar from django.db.models import Count
                print(theanswer)
                salidas_count = Salida.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
                
                oportunidad_count = Oportunidades.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
              
                
                                
                data = {

                'registros': registros,
                'entradas': entradas,
                'empresaArea':empresaArea,
                'area' : area,
                'theanswer': theanswer,
                'salidas_count':salidas_count,
                'oportunidad_count':oportunidad_count,
                'empresas':empresas,
                'empresa':empresa
                

                }
       
                return render(request,'empresa_1/tablas_diseño.html', data)
        else:
                return render(request, 'empresa_1/tabla_diseño.html')


def tablasLogistica(request,id):
        if request.user.is_authenticated:
                empresas = Empresa.objects.all()
                empresa = Empresa.objects.filter(id_empresa = id)
                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.get(nombre = "Logistica") #trar solo la ID de la etapa "Extraccion materia prima"
                empresaArea = RegistroTrabajador.objects.all()
                area = AreaEmpresa.objects.filter(id_empresa = id)
                theanswer = Entrada.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa) #requiere importar from django.db.models import Count
                salidas_count = Salida.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
                oportunidad_count = Oportunidades.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
                            
                data = {

                'registros': registros,
                'empresaArea':empresaArea,
                'area' : area,
                'theanswer': theanswer,
                'salidas_count':salidas_count,
                'oportunidad_count':oportunidad_count,
                'empresas':empresas,
                'empresa':empresa
        
                }
       
                return render(request,'empresa_1/tablas_logistica.html', data)
        else:
                return render(request, 'empresa_1/tabla_logistica.html')


def tablasCompra(request,id):
        if request.user.is_authenticated:
                empresas = Empresa.objects.all()
                empresa = Empresa.objects.filter(id_empresa = id)
                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.get(nombre = "Compra") #trar solo la ID de la etapa "Extraccion materia prima"
                empresaArea = RegistroTrabajador.objects.all()
                area = AreaEmpresa.objects.filter(id_empresa = id)
                theanswer = Entrada.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa) #requiere importar from django.db.models import Count
                salidas_count = Salida.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
                oportunidad_count = Oportunidades.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
                            
                data = {

                'registros': registros,
                'empresaArea':empresaArea,
                'area' : area,
                'theanswer': theanswer,
                'salidas_count':salidas_count,
                'oportunidad_count':oportunidad_count,
                'empresas':empresas,
                'empresa':empresa
        
                }
       
                return render(request,'empresa_1/tablas_compra.html', data)
        else:
                return render(request, 'empresa_1/tabla_compra.html')

def tablasUso(request,id):
        if request.user.is_authenticated:
                empresas = Empresa.objects.all()
                empresa = Empresa.objects.filter(id_empresa = id)
                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.get(nombre = "Uso consumo") #trar solo la ID de la etapa "Extraccion materia prima"
                empresaArea = RegistroTrabajador.objects.all()
                area = AreaEmpresa.objects.filter(id_empresa = id)
                theanswer = Entrada.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa) #requiere importar from django.db.models import Count
                salidas_count = Salida.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
                oportunidad_count = Oportunidades.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
                            
                data = {

                'registros': registros,
                'empresaArea':empresaArea,
                'area' : area,
                'theanswer': theanswer,
                'salidas_count':salidas_count,
                'oportunidad_count':oportunidad_count,
                'empresas':empresas,
                'empresa':empresa
        
                }
       
                return render(request,'empresa_1/tablas_uso.html', data)
        else:
                return render(request, 'empresa_1/tabla_uso.html')


def tablasFin(request,id):
        if request.user.is_authenticated:
                empresas = Empresa.objects.all()
                empresa = Empresa.objects.filter(id_empresa = id)
                registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
                etapa = Etapa.objects.get(nombre = "Fin de vida") #trar solo la ID de la etapa "Extraccion materia prima"
                empresaArea = RegistroTrabajador.objects.all()
                area = AreaEmpresa.objects.filter(id_empresa = id)
                theanswer = Entrada.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa) #requiere importar from django.db.models import Count
                salidas_count = Salida.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
                oportunidad_count = Oportunidades.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa)
                            
                data = {

                'registros': registros,
                'empresaArea':empresaArea,
                'area' : area,
                'theanswer': theanswer,
                'salidas_count':salidas_count,
                'oportunidad_count':oportunidad_count,
                'empresas':empresas,
                'empresa':empresa
        
                }
       
                return render(request,'empresa_1/tablas_fin.html', data)
        else:
                return render(request, 'empresa_1/tabla_fin.html')

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
