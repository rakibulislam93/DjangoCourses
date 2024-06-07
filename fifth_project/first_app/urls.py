
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home,name='homepage'),
    path('about/',views.about,name='aboutpage'),
    path('contact/',views.contact,name='contactpage'),
    path('form/',views.submit_form,name='submit_form'),
    path('django_form/',views.DjangoForm,name='django_forms'),
    # path('student_form/',views.djangoStudentForm,name='student_form'),
    path('student_form/',views.passwordValidation,name='student_form'),

]