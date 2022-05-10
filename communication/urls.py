from django.urls import path
from . import views
from .views import RegisterAPI,LoginAPI
from knox import views as knox_views


urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('api/login', LoginAPI.as_view(),name="login"),
    path('api/signup/', RegisterAPI.as_view(), name='signup'),
    path('api/logout', knox_views.LogoutView, name='logout'),
    path('api/profiles/', views.get_profiles, name="profiles"),
    path('api/posts/', views.get_posts, name="posts"),
    path('api/groups/', views.get_groups, name="groups"),
    path('api/comments/', views.get_comments, name="comments"),
    path('api/profiles/<int:pk>/', views.get_profile, name="profile"),
    path('api/posts/<int:pk>/', views.get_post, name="post"),
    path('api/groups/<int:pk>/', views.get_group, name="group"),
    path('api/comments/<int:pk>/', views.get_comment, name="comment"),
    path('api/profiles/<int:pk>/delete/', views.delete_profile, name="delete_profile"),
    path('api/posts/<int:pk>/delete/', views.delete_post, name="delete_post"),
    path('api/groups/<int:pk>/delete/', views.delete_group, name="delete_group"),
    path('api/comments/<int:pk>/delete/', views.delete_comment, name="delete_comment"),
    path('api/profiles/<int:pk>/edit/', views.update_profile, name="update_profile"),
    path('api/posts/<int:pk>/edit/', views.update_post, name="update_post"),
    path('api/groups/<int:pk>/edit/', views.update_group, name="update_group"),
    path('api/comments/<int:pk>/edit/', views.update_comment, name="update_comment"),
    path('api/posts/new/', views.create_post, name="create_post"),
    path('api/groups/new/', views.create_group, name="create_group"),
    path('api/comments/new/', views.create_comment, name="create_comment"),  
]