from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(auto_now=True, max_length=500, blank=True)
    def __str__(self):
        return self.user.username   

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    members = models.ManyToManyField(User, related_name='groups')
    def __str__(self):
        return self.name 

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField(auto_now=True, max_length=500, blank=True)
    def __str__(self):
        return self.user.username
        
                        