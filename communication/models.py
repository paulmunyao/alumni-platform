from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
# class Profile(models.Model):
#     username = models.OneToOneField(User,on_delete=models.CASCADE,default=0,related_name='profile')
#     bio = models.CharField(max_length=100)
#     profile_pic = models.ImageField(upload_to='images/')
#     useremail = models.EmailField(max_length=20)
    
    

#     def __str__(self):
#         return self.user.username

# @receiver(post_save, sender=User)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
