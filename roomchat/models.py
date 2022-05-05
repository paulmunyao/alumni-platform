from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# from communication.models import Profile

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)


class Roomchat(models.Model):
     text = models.TextField()
     room = models.ForeignKey(Room,on_delete=models.CASCADE,blank=True,related_name='group',null=True)
     author=models.CharField(max_length=50)
     date = models.DateTimeField(default=datetime.now, blank=True)

