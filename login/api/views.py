from rest_framework import viewsets
from login.models import ClienteProfile
from login.api.serializers import ClienteProfileSerializer

class clienteProfileViewSet(viewsets.ModelViewSet):
    queryset = ClienteProfile.objects.all()
    serializer_class = ClienteProfileSerializer