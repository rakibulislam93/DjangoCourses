from rest_framework import serializers
from . import models


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    designation= serializers.StringRelatedField(many=True)
    specialization= serializers.StringRelatedField(many=True)
    available_time= serializers.StringRelatedField(many=True)
    class Meta:
        model = models.DoctorModel
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.DesignationModel
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.SpecializationModel
        fields = '__all__'

class AvailableTimeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = models.AvailableTime
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = models.ReviewModel
        fields = '__all__'