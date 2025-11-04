# login/api/views.py
from rest_framework import viewsets
from ..models import ClienteProfile, EntrenadorProfile
from .serializers import ClienteProfileSerializer, EntrenadorProfileSerializer

# CRUD para ClienteProfile
class ClienteProfileViewSet(viewsets.ModelViewSet):
    queryset = ClienteProfile.objects.all()
    serializer_class = ClienteProfileSerializer

# CRUD para EntrenadorProfile
class EntrenadorProfileViewSet(viewsets.ModelViewSet):
    queryset = EntrenadorProfile.objects.all()
    serializer_class = EntrenadorProfileSerializer
