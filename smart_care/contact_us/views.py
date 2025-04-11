from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUsModel
from .serializers import ContactUsSerializer
# Create your views here.

class ContactusViewSet(viewsets.ModelViewSet):
    queryset = ContactUsModel.objects.all()
    serializer_class = ContactUsSerializer