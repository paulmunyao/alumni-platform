from django.contrib import admin
from .models import Profile, Post, Group, Comment,Reply

# Register your models here.
admin.site.register (Profile)
admin.site.register (Post)
admin.site.register (Group)
admin.site.register (Comment)
admin.site.register(Reply)