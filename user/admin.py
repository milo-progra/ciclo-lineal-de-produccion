
from dataclasses import Field, fields
from django.contrib import admin
from .models    import Usuario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import AdminFormaCreacionUsuario, AdminFormaActualizar, RegistroTrabajador
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from django.contrib.auth.hashers import make_password

# Register your models here.

#importar datosde usuarios de excel
class UserResource(resources.ModelResource):
   # funcion para encriptar contraseña al importar los registros desde excel
    def before_import_row(self, row, **kwargs):
        value = row['password']
        row['password'] = make_password(value)

    class Meta:
        model = Usuario
        fields = 'id','username', 'first_name', 'last_name', 'email', 'telefono', 'password'


class UserAdmin(BaseUserAdmin, ImportExportModelAdmin):
    
    form = AdminFormaActualizar
    add_form = AdminFormaCreacionUsuario
    resource_class = UserResource


    #modelos que seran utilizados para mostrar el modelo de usuario

    #list_display = ('email', 'username')
    list_filter = ('email',)
    fieldsets = (
        (None,{'fields': ('username','email', 'password', 'telefono')}),
        ('Informacion personal', {'fields': ( 'first_name', 'last_name')}),
        ('Permisos Django', {'fields': ('is_staff', 'is_active')})

    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('username','password1', 'password2')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    


admin.site.register(Usuario, UserAdmin)





