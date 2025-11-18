# login/urls.py
from django.urls import path
from .views import LoginView, RegisterView, ClienteProfileView, EntrenadorProfileView, AdminOnlyView
from .token_views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from login.views import UserDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('profile/cliente/', ClienteProfileView.as_view(), name='cliente_profile'),
    path('profile/entrenador/', EntrenadorProfileView.as_view(), name='entrenador_profile'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin_only'),
    path('login/', LoginView.as_view(), name='login'),

    # borrar propio usuario
    path('users/me/', UserDeleteView.as_view()),
    # borrar por id (admin o propietario)
    path('users/<int:pk>/', UserDeleteView.as_view()),
]
