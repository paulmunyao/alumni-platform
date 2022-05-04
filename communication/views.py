from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, Post, Group, Comment
from .serializers import ProfileSerializer, PostSerializer, GroupSerializer, CommentSerializer

# Create your views here.

@api_view(['GET'])
def get_profiles(request):

    routes = [
        # creating endpoints for getting all the items
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

        # Endpoints for getting a single item
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

        # Endpoints for deleting a single item
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

        # Endpoints for updating a single item
        {'Endpoint': '/profiles/<int:pk>/update/',
        'method': 'PUT',
        'body': 'ProfileSerializer',
        'description': 'Update a profile'},

        {'Endpoint': '/posts/<int:pk>/update/',
        'method': 'PUT',
        'body': 'PostSerializer',
        'description': 'Update a post'},

        {'Endpoint': '/groups/<int:pk>/update/',
        'method': 'PUT',
        'body': 'GroupSerializer',
        'description': 'Update a group'},

        {'Endpoint': '/comments/<int:pk>/update/',
        'method': 'PUT',
        'body': 'CommentSerializer',
        'description': 'Update a comment'},

        # Endpoints for creating a single item
        {'Endpoint': '/posts/<int:pk>/create/',
        'method': 'POST',
        'body': 'PostSerializer',
        'description': 'Create a post'},

        {'Endpoint': '/groups/<int:pk>/create/',
        'method': 'POST',
        'body': 'GroupSerializer',
        'description': 'Create a group'},

        {'Endpoint': '/comments/<int:pk>/create/',
        'method': 'POST',
        'body': 'CommentSerializer',
        'description': 'Create a comment'},
    ]

    return Response(routes)