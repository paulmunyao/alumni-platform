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

        {'Endpoint': '/profiles/<int:pk>/',
        'method': 'GET',
        'body': 'None',
        'description': 'Get a profile'},

        {'Endpoint': '/posts/<int:pk>/',
        'method': 'GET',
        'body': 'None',
        'description': 'Get a post'},

        {'Endpoint': '/groups/<int:pk>/',
        'method': 'GET',
        'body': 'None',
        'description': 'Get a group'},

        {'Endpoint': '/comments/<int:pk>/',
        'method': 'GET',
        'body': 'None',
        'description': 'Get a comment'},

        {'Endpoint': '/profiles/<int:pk>/delete/',
        'method': 'DELETE',
        'body': 'None',
        'description': 'Delete a profile'},

        {'Endpoint': '/posts/<int:pk>/delete/',
        'method': 'DELETE',
        'body': 'None',
        'description': 'Delete a post'},

        {'Endpoint': '/groups/<int:pk>/delete/',
        'method': 'DELETE',
        'body': 'None',
        'description': 'Delete a group'},

        {'Endpoint': '/comments/<int:pk>/delete/',
        'method': 'DELETE',
        'body': 'None',
        'description': 'Delete a comment'},

        {'Endpoint': '/profiles/<int:pk>/update/',
        'method': 'PUT',
        'body': 'ProfileSerializer',
        'description': 'Update a profile'},
    ]