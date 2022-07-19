from django.contrib import admin
from .models import Area, Carta, Ciclo, Empresa, Entrada, Etapa, Opcion, Oportunidades, Salida


# Register your models here.

admin.site.register(Area)
admin.site.register(Empresa)
admin.site.register(Etapa)
admin.site.register(Opcion)
admin.site.register(Carta)
admin.site.register(Ciclo)


# admin.site.register(Entrada)
# admin.site.register(Salida)
# admin.site.register(Oportunidades)

