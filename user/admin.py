from django.contrib import admin
from .models    import Usuario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import AdminFormaCreacionUsuario, AdminFormaActualizar
# Register your models here.




class UserAdmin(BaseUserAdmin):
    
    form = AdminFormaActualizar
    add_form = AdminFormaCreacionUsuario


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



