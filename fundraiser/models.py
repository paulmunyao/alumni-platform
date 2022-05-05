from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from roomchat.views import group

# Create your models here.
class Fundroom(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

class fundchat(models.Model):
     text = models.TextField()
     group = models.ForeignKey(Fundroom,on_delete=models.CASCADE,blank=True,related_name='group')
     author=models.CharField(max_length=50)
     date = models.DateTimeField(default=datetime.now, blank=True)
