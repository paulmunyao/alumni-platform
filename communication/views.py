from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, Post, Group, Comment
from .serializers import ProfileSerializer, PostSerializer, GroupSerializer, CommentSerializer

# Create your views here.

@api_view(['GET'])
def get_routes(request):

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

#getting an item
@api_view(['GET'])
def get_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_groups(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

#getting a single item
@api_view(['GET'])
def get_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['GET'])
def get_post(request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['GET'])
def get_group(request, pk):
    group = Group.objects.get(pk=pk)
    serializer = GroupSerializer(group)
    return Response(serializer.data)

@api_view(['GET'])
def get_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

#deleting a single item
@api_view(['DELETE'])
def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    profile.delete()
    return Response('Profile deleted successfully!')

@api_view(['DELETE'])
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response('Post deleted successfully!')

@api_view(['DELETE'])
def delete_group(request, pk):
    group = Group.objects.get(pk=pk)
    group.delete()
    return Response('Group deleted successfully!')

@api_view(['DELETE'])
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return Response('Comment deleted successfully!')

#Updating an item
@api_view(['PUT'])
def update_profile(request, pk):
    data = request.data
    profile = Profile.objects.get(pk=pk)
    serializer = ProfileSerializer(instance=profile, data=data)   # instance=profile is used to update the instance
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_post(request, pk):
    data = request.data
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(instance=post, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_group(request, pk):
    data = request.data
    group = Group.objects.get(pk=pk)
    serializer = GroupSerializer(instance=group, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_comment(request, pk):
    data = request.data
    comment = Comment.objects.get(pk=pk)
    serializer = CommentSerializer(instance=comment, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        
# POST is used to create a new item
@api_view(['POST'])  
def create_post(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 

@api_view(['POST'])
def create_group(request):
    data = request.data
    serializer = GroupSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def create_comment(request):
    data = request.data
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def create_comment(request):
    data = request.data
    serializer = CommentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

