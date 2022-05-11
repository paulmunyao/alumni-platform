from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField
from roomchat.views import group

# Create your models here.
class Fundroom(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

class fundchat(models.Model):
     text = models.TextField()
     fundgroup = models.ForeignKey(Fundroom,on_delete=models.CASCADE,blank=True,related_name='fundgroup')
     author=models.CharField(max_length=55)
     date = models.DateTimeField(default=datetime.now, blank=True)
     image = CloudinaryField('image',null=True)



