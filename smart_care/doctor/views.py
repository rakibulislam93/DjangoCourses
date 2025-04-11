from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
from rest_framework import filters,pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.


class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # item per page
    page_query_param = 'page_size'
    max_page_size = 100


class DoctorViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPagination

    queryset = models.DoctorModel.objects.all()
    serializer_class = serializers.DoctorSerializer



class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.DesignationModel.objects.all()
    serializer_class = serializers.DesignationSerializer

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.SpecializationModel.objects.all()
    serializer_class = serializers.SpecializationSerializer


class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctormodel=doctor_id)
        return queryset
class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer

    filter_backends = [AvailableTimeForSpecificDoctor]

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = models.ReviewModel.objects.all()
    serializer_class = serializers.ReviewSerializer

 


