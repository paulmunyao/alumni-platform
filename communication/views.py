from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, Post, Group, Comment
from .serializers import ProfileSerializer, PostSerializer, GroupSerializer, CommentSerializer

# Create your views here.

@api_view(['GET'])
def get_profiles(request):

    routes = [
        {'Endpoint': '/profiles/', 
        'method': 'GET', 
        'body': 'None',
        'description': 'Get all profiles'},

        {'Endpoint': '/posts/',
        'method': 'GET',
        'body': 'None',
        'description': 'Get all posts'},

        {'Endpoint': '/groups/',
        'method': 'GET',
        'body': 'None',
        'description': 'Get all groups'},

        {'Endpoint': '/comments/',
        'method': 'GET',
        'body': 'None',
        'description': 'Get all comments'},
    ]