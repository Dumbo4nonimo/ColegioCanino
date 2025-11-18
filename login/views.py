from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer, ClienteSerializer, EntrenadorSerializer
from .models import Cliente, Entrenador
from .permissions import IsRole

# Registro de usuario (open)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# Endpoint: obtener perfil cliente (solo role 'cliente')
from rest_framework.views import APIView

class ClienteProfileView(APIView):
    permission_classes = [IsAuthenticated, IsRole]
    allowed_roles = ['cliente']

    def get(self, request):
        try:
            cliente = request.user.cliente_profile
        except Cliente.DoesNotExist:
            return Response({"detail": "Perfil cliente no existe."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)


# Endpoint: obtener perfil entrenador (solo role 'entrenador')
class EntrenadorProfileView(APIView):
    permission_classes = [IsAuthenticated, IsRole]
    allowed_roles = ['entrenador']

    def get(self, request):
        try:
            entrenador = request.user.entrenador_profile
        except Entrenador.DoesNotExist:
            return Response({"detail": "Perfil entrenador no existe."}, status=status.HTTP_404_NOT_FOUND)
        serializer = EntrenadorSerializer(entrenador)
        return Response(serializer.data)


# Endpoint: ejemplo solo admin
class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsRole]
    allowed_roles = ['admin']

    def get(self, request):
        return Response({"mensaje": "Hola admin, puedes ver esto."})

# Create your views here.
