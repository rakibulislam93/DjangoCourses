from django.shortcuts import render
from rest_framework import generics
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator,PasswordResetTokenGenerator
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import login,logout,authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from . import models
from . import serializers
# Create your views here.


class RegisterView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    
    def perform_create(self, serializer):
        user = serializer.save()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        confirm_link = f'http://127.0.0.1:8000/account/verify_email/{uid}/{token}/'
        
        send_mail(
            subject='Email Verify',
            message=f'Hi, {user.username} Click this link and verify your account : {confirm_link}',
            from_email='rakibulislamarif793@gmail.com',
            recipient_list=[user.email]
            
        )
        
    

class Varify_account(APIView):
    
    def get(self,request,uidb64,token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = models.CustomUser.objects.get(pk=uid)
        except models.CustomUser.DoesNotExist:
            user = None
        
        if user and default_token_generator.check_token(user,token):
            user.is_active = True
            user.save()
            return Response({'message':'Account verify successful'},status=status.HTTP_200_OK)
        
        return Response({'error':'Invalid User or link'},status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    serializer_class = serializers.LoginSerializer
    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                refresh = RefreshToken.for_user(user)
                access = refresh.access_token
                return Response({
                    'refresh':str(refresh),
                    'access':str(access),
                    'message':'Login successful',
                },status=status.HTTP_200_OK)
            
            return Response({'error':'Invalid credentials.!'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                

class LogoutView(APIView):
    def post(self,request):
        logout(request)
        return Response({'message':'Logout successful.'},status=status.HTTP_200_OK)



class PasswordChangeView(APIView):
    serializer_class = serializers.PasswordChangeSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message':'Password change successful.'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ResetPassView(APIView):
    serializer_class = serializers.PassResetSerializer
    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            
            if models.CustomUser.objects.filter(email=email).exists():
                user = models.CustomUser.objects.get(email=email)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = PasswordResetTokenGenerator().make_token(user)
                reset_link = f'http://127.0.0.1:8000/account/reset_pass/{uid}/{token}/'
                
                send_mail(
                    subject='Password Reset',
                    message=f'Hi, {user.username} Please click this link and reset your password : {reset_link}',
                    from_email='rakibulislamarif793@gmail.com',
                    recipient_list=[email],
                    fail_silently=False,
                )
                return Response({'message':'Please check your mail and reset password.'},status=status.HTTP_200_OK)
            else:
                return Response({'error':'User not found with this email.!'},status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class SetPasswordView(APIView):
    serializer_class = serializers.SetResetPassword
    
    def post(self,request,uidb64,token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = models.CustomUser.objects.get(pk=uid)
        except models.CustomUser.DoesNotExist:
            user = None
        
        if user and PasswordResetTokenGenerator().check_token(user,token):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                password = serializer.validated_data['new_password']
                user.set_password(password)
                user.save()
                return Response({'message':'Password reset successful.'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'error':'Invalid User or Reset Link'},status=status.HTTP_400_BAD_REQUEST)