"""comsplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
# from communication.views import  signup_view
# from communication.views import signup_view, activation_sent_view, activate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('communication.urls')),
    path('',include('roomchat.urls')),
    # path('',include('fundraiser.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('signup/', signup_view, name="signup"),
    # path('sent/', activation_sent_view, name="activation_sent"),
    # path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),


    path('login', views.redirect_to_login,{"next_page": 'home'}),
]
