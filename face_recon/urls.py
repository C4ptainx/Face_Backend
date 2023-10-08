from django.urls import path
from face_recon.views import SendPasswordResetEmailView, UserChangePasswordView, AsistenciaListView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView
from rest_framework_simplejwt.views import (  TokenRefreshView)
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('asistencia/', AsistenciaListView.as_view(), name='asistencia-list'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]