from django.contrib import admin
from .models import Profile, Post, Group, Comment

# Register your models here.
admin.site.register (Profile)
admin.site.register (Post)
admin.site.register (Group)
admin.site.register (Comment)
