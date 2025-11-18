from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer, ClienteSerializer, EntrenadorSerializer
from .models import Cliente, Entrenador
from .permissions import IsRole
from rest_framework_simplejwt.tokens import RefreshToken
from login.models import User

# Registro de usuario (open)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # evita que se intente validar el token expirado


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

class LoginView(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if email is None or password is None:
            return Response(
                {"error": "Email y contraseña son obligatorios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "Credenciales incorrectas."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not user.check_password(password):
            return Response(
                {"error": "Credenciales incorrectas."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Generar tokens JWT
        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "role": user.role,
            "username": user.username,
            "email": user.email,
        }, status=status.HTTP_200_OK)

class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk=None):
        """
        DELETE /api/users/me/   -> elimina al usuario autenticado
        DELETE /api/users/<pk>/ -> elimina usuario por id (solo admin o propio usuario)
        """
        # borrar propio usuario
        if pk is None:
            user = request.user
        else:
            try:
                user = User.objects.get(pk=pk)
            except User.DoesNotExist:
                return Response({"detail": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

            # solo admin o propietario pueden borrar
            if request.user != user and request.user.role != "admin":
                return Response({"detail": "No autorizado."}, status=status.HTTP_403_FORBIDDEN)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)