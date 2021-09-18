from django.urls import path, include
from .views import create_email
urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('create_email', create_email.as_view())
]
