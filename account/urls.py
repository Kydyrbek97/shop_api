from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from account import views
from account.views import LogoutView

urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('forgot/', views.ForgotPasswordView.as_view()),
    path('restore/', views.RestorePasswordView.as_view()),
]