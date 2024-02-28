from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    username=forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
