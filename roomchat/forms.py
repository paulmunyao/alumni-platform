from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from .models import Room,Roomchat
from django.contrib.auth.forms import UserCreationForm

class NewRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name','logo']
        exclude = ['admin']

class NewChatForm(forms.ModelForm):
    class Meta:
        model = Roomchat
        fields = '__all__'