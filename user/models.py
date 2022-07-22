from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager

# Create your models here.

class UsuarioManager(UserManager):
    def create_user(self, username, nombre, apellido,telefono, correo, password = None):
        usuario = self.model(
            username    = username,
            telefono    = telefono,
            first_name  = nombre,
            last_name   = apellido,
            email       = correo
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, nombre, apellido,telefono, correo, password):
        usuario = self.create_user(
            username = username,
            telefono = telefono,
            first_name = nombre,
            last_name = apellido,
            email = correo
        ) 
        usuario.usuario_administrador = True      
        usuario.save()
        return usuario 


class Usuario(AbstractUser):
    telefono = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.username}, {self.email},         Administrador:{self.is_staff}'


    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True 

    # @property
    # def is_staff(self):
    #     return self.usuario_administrador    

    # def get_short_name(self):
    #     return self.username
    
    # def get_full_name(self):
    #     return self.username + '' + self.last_name    




#ingresar area del trabajador


