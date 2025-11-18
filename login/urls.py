# miapp/urls.py
from django.urls import path
from .views import RegisterView, ClienteProfileView, EntrenadorProfileView, AdminOnlyView
from .token_views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('profile/cliente/', ClienteProfileView.as_view(), name='cliente_profile'),
    path('profile/entrenador/', EntrenadorProfileView.as_view(), name='entrenador_profile'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin_only'),
]
