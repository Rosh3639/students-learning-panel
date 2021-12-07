from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'desc']


class PanelForm(forms.Form):
    text = forms.CharField(max_length=200, label="Enter Something To Search ")


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_finished']


class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
