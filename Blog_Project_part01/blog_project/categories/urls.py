from django.urls import path
from categories import views

urlpatterns = [
    path('add/',views.add_category,name='add_category'),
]
