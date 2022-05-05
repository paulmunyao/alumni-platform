from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import Textarea
from django.contrib.auth.forms import UserCreationForm
# from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

User._meta.get_field('email')._unique = True 


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profile_pic','useremail','bio']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
        'email', 'password1', 'password2',)