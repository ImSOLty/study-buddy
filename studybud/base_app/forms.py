from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
