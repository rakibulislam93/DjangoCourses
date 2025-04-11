from django.urls import path,include
from . import views
urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register'),
    path('verify_email/<uidb64>/<token>/',views.Varify_account.as_view(),name='account_verify'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('pass_change/',views.PasswordChangeView.as_view()),
    path('reset_pass/',views.ResetPassView.as_view()),
    path('reset_pass/<uidb64>/<token>/',views.SetPasswordView.as_view()),
]
