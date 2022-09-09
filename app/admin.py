from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import AreaEmpresa, Empresa, Entrada, Etapa, Oportunidades, Salida, RegistroTrabajador




class RegistroTrabajadorResource(resources.ModelResource):

    class Meta:
        model  =  RegistroTrabajador 
        #import_id_fields = ('campo que sera la id',)
        fields = 'id', 'descripcion', 'id_area', 'usuario'   


class ResgitroTrabajadorAdmin(ImportExportModelAdmin):
    resource_class = RegistroTrabajadorResource

# Register your models here.

admin.site.register(AreaEmpresa)
admin.site.register(Empresa)
admin.site.register(Etapa)
#admin.site.register(Opcion)
# admin.site.register(Nota)
#admin.site.register(CicloArea)


admin.site.register(Entrada)
admin.site.register(Salida)
admin.site.register(Oportunidades)
admin.site.register(RegistroTrabajador, ResgitroTrabajadorAdmin)



