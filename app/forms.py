from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Entrada, Salida, Oportunidades

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = 'nombre',


class SalidaForm(forms.ModelForm):
    class Meta:
        model = Salida
        fields = 'nombre',


class OportunidadForm(forms.ModelForm):
    class Meta:
        model = Oportunidades
        fields = 'nombre',