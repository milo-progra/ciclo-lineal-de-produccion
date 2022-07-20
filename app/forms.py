from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Nota

class FORMNAME(forms.Form):
    class meta:
        model = Nota
        fields = '__all__'

