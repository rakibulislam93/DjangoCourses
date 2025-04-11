from django.shortcuts import render,redirect
from rest_framework import viewsets
from . import serializers
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout


# for email varification
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
# Create your views here.



class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.PatientModel.objects.all()
    serializer_class = serializers.PatientSerializer


class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"

            subject = "Confirm Your Email"
            message = render_to_string('register_mail.html',{
                'confirm_link': confirm_link,
            })
            sent_mail = EmailMultiAlternatives(subject,to=[user.email])
            sent_mail.attach_alternative(message,"text/html")
            sent_mail.send()

            return Response("Check your mail for confirmation")
        
        return Response(serializer.errors)
    

def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)

    except(User.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')


class UserLoginApiView(APIView):
    def post(self,request):
        serializer = serializers.UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user:
                token,created= Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token': token.key,'user_id': user.id})
            else:
                return Response({'error':"Invalid Credential"})
        
        return Response(serializer.errors)



class UserLogoutView(APIView):
    
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        
        return redirect('login')