from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Libro, Merchandising, Consulta, User

class LibroForm(forms.ModelForm):
    """ Formulario para crear o editar un libro. Hereda de ModelForm y utiliza el modelo Libro."""
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'precio', 'imagen', 'texto', 'es_novedad']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class MerchandisingForm(forms.ModelForm):
    """ Formulario para crear o editar merchandising. Hereda de ModelForm y utiliza el modelo Merchandising."""
    class Meta:
        model = Merchandising
        fields = ['titulo', 'precio', 'imagen', 'texto', 'es_novedad']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ConsultaForm(forms.ModelForm):
    """ Formulario para enviar una consulta. Hereda de ModelForm y utiliza el modelo Consulta."""
    class Meta:
        model = Consulta
        fields = ['nombre', 'email', 'consulta']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'consulta': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class RegistroForm(UserCreationForm):
    """ Formulario para registrar un nuevo usuario. Hereda de UserCreationForm y utiliza el modelo User."""
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
        # Para que se vea bien con bootstrap
        for field_name in fields:
            widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control'}),
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
            }