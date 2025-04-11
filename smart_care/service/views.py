from django.shortcuts import render
from rest_framework import viewsets
from .models import ServiceModel
from .serializers import ServiceSerializer
# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer