from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task


class Register(UserCreationForm):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]  

class NewTask(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    completed = forms.BooleanField(required=False)
    created = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Task
        fields = ["title","description","completed"]

class UpdateTask(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    completed = forms.BooleanField(required=False)
    class Meta:
        model = Task
        fields = ["title","description","completed"]
