# login/api/serializers.py
from rest_framework import serializers
from login.models import ClienteProfile
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class ClienteProfileSerializer(serializers.ModelSerializer):
    # Campos del usuario (solo los que quieres)
    nombre = serializers.CharField(source='first_name')
    apellido = serializers.CharField(source='last_name')
    correo = serializers.EmailField(source='email')

    class Meta:
        model = ClienteProfile
        # Solo los campos que quieres mostrar
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion']  # agrega tus campos de ClienteProfile
