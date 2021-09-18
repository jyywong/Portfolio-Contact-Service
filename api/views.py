from django.shortcuts import render
from rest_framework import generics
from .serializers import ContactSerializer
from .models import Contact

# Create your views here.


class create_email(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
