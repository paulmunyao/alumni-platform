from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Alumni Platform",
#         default_version='v1',
#         description="A web application that allows Alumni's to keep in touch with one another.<br/>For this part of the project it contains the backend logic which also has the endpoints for each and every API that is called on the front-end.",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="paulmunyao094@gmail.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('communication.urls')),
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs", SpectacularSwaggerView.as_view(url_name="schema")),
#      path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
