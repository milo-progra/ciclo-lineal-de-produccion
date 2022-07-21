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

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True   




#ingresar area del trabajador


