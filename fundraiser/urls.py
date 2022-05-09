from django.urls import path
from . import views

urlpatterns = [
    path('fundgroups',views.fundgroups,name='fundgroups'),
    path('newfundteam',views.new_fund,name='newfundteam'),
    path('my_fundteam/<int:id>',views.fundteam,name='my_fundteam'),
    path('fundchat/<int:id>',views.fund_chat,name='fundchat'),
]