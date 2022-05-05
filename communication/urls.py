from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
# from communication.views import  signup_view


urlpatterns = [
    path('',views.index,name='home'),
    # path('update_profile', views.profile_update, name='profile_update'),
    # path('my_profile', views.profile_display, name='profile_display'),
    # # path('signup/', signup_view, name="signup")
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)