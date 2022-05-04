from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, Post, Group, Comment
from .serializers import ProfileSerializer, PostSerializer, GroupSerializer, CommentSerializer

# Create your views here.
