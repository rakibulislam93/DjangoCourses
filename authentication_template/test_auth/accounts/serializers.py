from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from . import models


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = models.CustomUser
        fields = ['id','username','email','password','confirm_password','user_role']
        extra_kwargs = {
            'password':{'write_only':True},
        }
    
    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('confirm_password')
        
        if password1 != password2:
            raise serializers.ValidationError({'error':'Two password does not match.!'})
        
        return attrs
    
    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password')
        password = validated_data['password']
        user = models.CustomUser(**validated_data)
        user.is_active = False
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()
    
    def validate(self, attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')
        
        user = self.context['request'].user
        
        if not user.check_password(old_password):
            raise serializers.ValidationError({'error':'Old password does not match'})
        if new_password != confirm_password:
            raise serializers.ValidationError({'error':'Two password does not match'})
        validate_password(new_password,user)
         
        return attrs
    

class PassResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    

class SetResetPassword(serializers.Serializer):
    new_password = serializers.CharField()