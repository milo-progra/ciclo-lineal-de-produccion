from django.urls import include, path
from .views import *

urlpatterns = [
    path('api_authorization/', include('rest_framework.urls')),
    path('home_api', home_api, name="Home_api"),
    path('view_usuarios/', User_APIView.as_view(), name="api_usuarios"),
    path('view_ubicacion/', Ubicacion_APIView.as_view(), name="api_ubicacion"),
]
