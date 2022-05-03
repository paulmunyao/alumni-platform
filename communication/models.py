from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField



# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,default=0,related_name='profile')
    bio = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='images/')
    useremail = models.EmailField(max_length=20)
    
