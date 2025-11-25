from pets.apis.views import PetApiViewSet, get_pet_by_user
from django.urls import path
from rest_framework.routers import DefaultRouter


router_pet = DefaultRouter()
router_pet.register(prefix='', basename='pets', viewset=PetApiViewSet)


urlpatterns = [
    path('pet/by-user', get_pet_by_user),
]