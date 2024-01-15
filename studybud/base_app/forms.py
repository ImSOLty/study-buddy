from django import forms
from . import models
from django.contrib.auth.models import User


class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'email']