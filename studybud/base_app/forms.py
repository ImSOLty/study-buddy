from django import forms
from . import models


class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = '__all__'
        exclude = ['host', 'participants']
