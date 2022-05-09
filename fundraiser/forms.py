from django import forms
from .models import Fundroom,fundchat

class NewFundRoomForm(forms.ModelForm):
    class Meta:
        model = Fundroom
        fields = ['name','logo']
        exclude = ['admin']

class FundChatForm(forms.ModelForm):
    class Meta:
        model = fundchat
        exclude=["author","fundgroup"]
        fields = ['text','date']
