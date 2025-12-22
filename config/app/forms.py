from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Register(UserCreationForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password", "password2"]  