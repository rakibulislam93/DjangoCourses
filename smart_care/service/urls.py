from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet
from django.urls import path,include
router = DefaultRouter() # amader router

router.register('',ServiceViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
