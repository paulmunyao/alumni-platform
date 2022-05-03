from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('rooms',views.rooms,name='rooms'),
    path('newroom',views.new_room,name="newroom"),
    path('my_group/<int:id>',views.group,name='my_group'),
    path('new_chat/<int:id>',views.new_chat,name='new_chat'),
    
]