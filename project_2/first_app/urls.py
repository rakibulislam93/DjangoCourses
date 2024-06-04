
from django.urls import path

# 3 way the import kora jai
# from first_app import views
# from first_app.views import home
from . import views

urlpatterns = [
    
    path('', views.home),
]
