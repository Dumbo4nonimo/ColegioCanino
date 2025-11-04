# login/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteProfileViewSet, EntrenadorProfileViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteProfileViewSet, basename='clientes')
router.register(r'entrenadores', EntrenadorProfileViewSet, basename='entrenadores')

urlpatterns = [
    path('', include(router.urls)),
]
