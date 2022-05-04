from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('profiles/', views.get_profiles, name="profiles"),
    path('posts/', views.get_posts, name="posts"),
    path('groups/', views.get_groups, name="groups"),
    path('comments/', views.get_comments, name="comments"),
    path('profiles/<int:pk>/', views.get_profile, name="profile"),
    path('posts/<int:pk>/', views.get_post, name="post"),
    path('groups/<int:pk>/', views.get_group, name="group"),
    path('comments/<int:pk>/', views.get_comment, name="comment"),
    path('profiles/<int:pk>/delete/', views.delete_profile, name="delete_profile"),
    path('posts/<int:pk>/delete/', views.delete_post, name="delete_post"),
    path('groups/<int:pk>/delete/', views.delete_group, name="delete_group"),
    path('comments/<int:pk>/delete/', views.delete_comment, name="delete_comment"),
    path('profiles/<int:pk>/edit/', views.update_profile, name="update_profile"),
    path('posts/<int:pk>/edit/', views.update_post, name="update_post"),
    path('groups/<int:pk>/edit/', views.update_group, name="update_group"),
    path('comments/<int:pk>/edit/', views.update_comment, name="update_comment"),
    path('posts/new/', views.create_post, name="create_post"),
    path('groups/new/', views.create_group, name="create_group"),
    path('comments/new/', views.create_comment, name="create_comment"),  
]