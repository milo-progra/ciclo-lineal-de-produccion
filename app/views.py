from django.shortcuts import render
from .models import Nota                

# Create your views here.
def home(request):
    notas = Nota.objects.filter(etapa = 1)
    # estado = notas.etapa.estado
    # print(estado)
    
    return render(request,'home.html', {'notas':notas})



