from django.contrib import admin
from .models import Area, Nota, Ciclo, Empresa, Entrada, Etapa, Opcion, Oportunidades, Salida


# Register your models here.

admin.site.register(Area)
admin.site.register(Empresa)
admin.site.register(Etapa)
admin.site.register(Opcion)
admin.site.register(Nota)
admin.site.register(Ciclo)


# admin.site.register(Entrada)
# admin.site.register(Salida)
# admin.site.register(Oportunidades)

