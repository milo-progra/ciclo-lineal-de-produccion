from django.urls import include, path
from .views import *

urlpatterns = [
    path('view_usuarios/', User_APIView.as_view()),
    path('api_authorization/', include('rest_framework.urls')),
]
