
from dataclasses import field, fields
from pyexpat import model
from xml.dom.minidom import Attr
from django import forms
from .models import Usuario
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from app.models import RegistroTrabajador, Empresa, AreaEmpresa
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(forms.ModelForm):

    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'username'
        }))

    first_name = forms.CharField(label=' ingrese su nombre', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'first_name'
        }))

    last_name = forms.CharField(label=' ingrese su apellido', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'last_name'
        }))

    email = forms.EmailField(label='correo electronico', widget=forms.EmailInput(attrs={
        'class': 'form-control mb-2',
        'placeholder': 'Ingrese su correo electronico',
        'id': 'email'
    }))

    telefono = forms.IntegerField(label='Telefono', widget=forms.NumberInput(attrs={
        'class': 'form-control mb-2',
        'placeholder': 'Ingrese Telefono',
        'id': 'telefono'
    }))

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese Contraseña',
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

    def save(self, commit=True):
        # guardar la informacion del registro en la variable user
        user = super().save(commit=False)
        # encriptar contraseña
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class RegistroTrabajadorForm(forms.ModelForm):

    descripcion = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'descripcion'
    }))

    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    id_area = forms.ModelChoiceField(queryset=AreaEmpresa.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control', 'hidden': 'true'
    }), label='AreaEmpresa')

    class Meta:
        model = RegistroTrabajador
        fields = 'descripcion', 'empresa', 'id_area'


# Form usuario por consola

class FormaRegistro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = Usuario.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username ya registrado")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return password2

  # Form para crear usuario por vista admin django


class AdminFormaCreacionUsuario(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'telefono')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return password2

    def save(self, commit=True):
        usuario = super(AdminFormaCreacionUsuario, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario


class AdminFormaActualizar(forms.ModelForm):
    # variable para que el admin solo pueda ver la contraseña
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'telefono', 'password')

    def clean_password(self):
        return self.initial['password']


# //////////////////////////////////// forms para registrar telegram ///////////////////////////////////////

class TelegramForm(forms.ModelForm):

    id_telegram = forms.CharField(label='ID Telegram', widget=forms.TextInput(
        attrs={
            'placeholder': 'Ingrese su ID de telegram',
            'id': 'id_telegram'
        }))

    class Meta:
        model = Usuario
        fields = ('id_telegram', )



