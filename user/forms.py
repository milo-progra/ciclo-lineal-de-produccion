
from django import forms
from .models import Usuario
from app.models import RegistroTrabajador, Empresa
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(forms.ModelForm):

    password = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder':'Ingrese Contraseña',
            'id': 'password'
        }))

    class Meta:
        model = Usuario
        fields = 'username', 'first_name', 'last_name', 'email', 'telefono', 'password'


    def clean_password(self):
        """ validacion de contraseña

        metodo que valida la contraseña 
        """
        password = self.cleaned_data.get('password')
        return password

    def save(self, commit = True):
        user = super().save(commit = False) # guardar la informacion del registro en la variable user
        user.set_password(self.cleaned_data['password']) #encriptar contraseña 
        if commit:
            user.save()
        return user      



class RegistroTrabajadorForm(forms.ModelForm):
    
    #empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), widget=Select(attrs ={}))

    class Meta:
        model = RegistroTrabajador
        fields ='__all__'