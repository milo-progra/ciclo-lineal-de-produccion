from django.contrib import admin
from .models import AreaEmpresa, Entrada, Nota, CicloArea, Empresa, Etapa, Opcion, Oportunidades, Salida


# Register your models here.

admin.site.register(AreaEmpresa)
admin.site.register(Empresa)
admin.site.register(Etapa)
#admin.site.register(Opcion)
# admin.site.register(Nota)
admin.site.register(CicloArea)


admin.site.register(Entrada)
admin.site.register(Salida)
admin.site.register(Oportunidades)

