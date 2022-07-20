from django.shortcuts import get_object_or_404, render
from .models import Nota, Etapa                

# Create your views here.
def home(request):

    notas = Nota.objects.all().filter(etapa = 1)

    #etapa = get_object_or_404(Etapa, activo = 1 )
    etapas = Etapa.objects.filter(activo = 1)
    
    return render(request,'home.html', {'notas':notas, 'etapas':etapas})



