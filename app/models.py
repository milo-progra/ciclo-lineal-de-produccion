from lib2to3.pgen2.token import OP
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=20)    

    def __str__(self):
        return self.nombre


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=20)   
    productos = models.CharField(max_length=50)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE) 

    def nombre_area(self):
        return "{}, {}". format(self.nombre, self.id_empresa)

    def __str__(self):
        return self.nombre_area()    


class Etapa(models.Model):
    id_etapa = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=50) 
    fecha_inicio  = models.DateField() 
    fecha_termino  = models.DateField()
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE)  

    def __str__(self):
        return self.nombre

class Ciclo(models.Model):
    id_ciclo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    fecha = models.DateField()
    are = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
        

class Opcion(models.Model):
    id_Opcion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre
        

class Carta(models.Model):
    id_Carta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    fecha = models.DateField()


    def __str__(self):
        return self.nombre
        




class Entrada(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=50) 
    fecha = models.DateField()
    id_etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    id_usuario =models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Salida(models.Model):
    id_salida = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=50) 
    fecha = models.DateField()
    id_etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    id_usuario =models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Oportunidades(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=50) 
    fecha = models.DateField()
    id_etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    id_usuario =models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
                        
        
        
          


