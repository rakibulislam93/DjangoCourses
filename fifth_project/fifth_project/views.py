from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse('This is home page')
    return render(request,'base.html')