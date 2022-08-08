

from django.shortcuts import render
from app.models import RegistroTrabajador, Etapa, Entrada, Salida, Oportunidades, Empresa, AreaEmpresa
from django.db.models import Count
import collections
from Levenshtein import distance, editops, apply_edit, jaro





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


                #/////////////// Levenshtein ///////////////
                lista_u = []
                plabra_es = []
                lista_t = [] 
                nombre_espa = ""
                for e in entradas:
                        for a in area:
                                if e.id_area_id == a.id_area:        
                                        #print("las notas son: ",e.nombre) 
                                        e_nombre = e.nombre
                                        result = len(e_nombre.split()) #cuanta las palabras que tiene cada registro
                                        #print(result)
                                        #si el registro tiene mas de un 1 palabra guardalo en la variable nombre_espa
                                        if result > 1 :
                                                nombre_espa = e.nombre
                                                print(nombre_espa)
                                                separador = " "
                                                maximo_numero_de_separaciones = 2
                                                separado_por_espacios = nombre_espa.split(separador, maximo_numero_de_separaciones)
                                                plabra_es = plabra_es + separado_por_espacios
                                                
                                        else:
                                                lista_u.append(e_nombre)

                lista_t =  plabra_es + lista_u                       
                #print(lista_t)                    

                #////////////////////////////////////////
                
                result = (Entrada.objects
                .values('id_area')
                .annotate(dcount=Count('id_area'))
                .order_by()
                )
                #print("variable result!!!!!!!: ",result)

               

                theanswer = Entrada.objects.values('id_area').annotate(Count('id_area')).filter(etapa_id = etapa) #requiere importar from django.db.models import Count
                #print(theanswer)
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
                'empresa':empresa,
                'lista_t':lista_t
                

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



def promedioArea(request, id):
        registros = RegistroTrabajador.objects.filter(id_usuario=request.user)
        empresas = Empresa.objects.all()
        empresa = Empresa.objects.filter(id_empresa = id)

        entradas = Entrada.objects.filter(id_area_id = id)
        total_entradas = Entrada.objects.filter(id_area_id = id).count()
        total_salidas = Salida.objects.filter(id_area_id = id).count()
        total_oportunidades = Oportunidades.objects.filter(id_area_id = id).count()

        

#/////////////// Levenshtein ///////////////
        lista_u = []
        plabra_es = []
        lista_t = [] 
        nombre_espa = ""


        for e in entradas:
                #print("las notas son: ",e.nombre) 
                e_nombre = e.nombre
                result = len(e_nombre.split()) #cuanta las palabras que tiene cada registro
                #print(result)
                #si el registro tiene mas de un 1 palabra guardalo en la variable nombre_espa
                if result > 1 :
                        nombre_espa = e.nombre
                        #print(nombre_espa)
                        separador = " "
                        maximo_numero_de_separaciones = 2
                        separado_por_espacios = nombre_espa.split(separador, maximo_numero_de_separaciones)
                        plabra_es = plabra_es + separado_por_espacios
                                                
                else:
                        lista_u.append(e_nombre)

        lista_t =  plabra_es + lista_u                       
        print(lista_t)       
        c = collections.Counter(lista_t) #crea un diccionario agrupando por palabras
        print(c)
        
        clave = c.keys()
        valor = c.values()
        cantidad_datos = c.items()

        for clave, valor in cantidad_datos:
                print (clave , ": " , valor)


        values = c.values()
        #print(c['harina'])
        p = c['harina']
        

        nota_masRepetida = ""
        b = 0
        for i in c:
                n = c[i]
                if b < n:
                        b = n 
                               
                if n == b :
                        nota_masRepetida = i
        #print("la nota mas repetida es: ", nota_masRepetida) 
       

        #///////////// Levenshetein ///////////////////////////
        import numpy as np
        # filas = len(lista_t)
        # columnas = len(lista_t)


        # A = np.zeros([filas,columnas])

        # for i in range(filas):
        #         for j in range(columnas):
        #                 a = i+1
        #                 x = j+1
        #                 A[i,j] = a+x
        # print(A)

        n_filas = len(lista_t)          #Cantidad de registros
        n_columnas = len(lista_t)       #Cantidad de registros
        
        A = np.zeros([n_filas, n_columnas]) #Creo un array vacio

        for i in range(n_filas):
                for j in range(n_columnas):
                        a = lista_t[i]
                        b = lista_t[j]
                        A[i,j] = round(jaro(a,b)*100)
                       
        #print(A)   
        # for line in A:
        #         c = map
        #         print (' '.join(map(str, line)))
        arr = A
        # for i in A:
        #         print (i)
       
        for i in range(n_filas):
                canti_registros =  i
                columna = [fila[i] for fila in A] 
                print(columna)    
        #print(canti_registros)
        #////////////////////////////////////////                

        data = {

                
                'registros': registros,
                'empresas': empresas,
                'empresa':empresa,
                'total_entradas':total_entradas,
                'total_salidas':total_salidas,
                'total_oportunidades':total_salidas,
                'nota_masRepetida':nota_masRepetida,
                'lista_t':lista_t,
                'clave':clave,
                'valor':valor,
                'cantidad_datos':cantidad_datos,
                'A':A,
                'arr':arr,
                'n_filas':n_filas,
                'n_columnas':n_columnas,
                'canti_registros':canti_registros
 
        }

        return render(request, 'empresa_1/promedios/promedio.html', data)



        







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
