# login/api/serializers.py
from rest_framework import serializers
from ..models import ClienteProfile, EntrenadorProfile, CustomUser

# Serializer para CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name']

# Serializer para ClienteProfile
class ClienteProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # incluir datos del usuario
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.filter(role='cliente'),
        write_only=True,
        source='user'
    )

    class Meta:
        model = ClienteProfile
        fields = [
            'id',
            'user',       # datos del usuario para lectura
            'user_id',    
            'fecha_nacimiento',
            'telefono',
            'reporte_deudas',
            'recomendaciones',
            'observaciones'
        ]

# Serializer para EntrenadorProfile
class EntrenadorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.filter(role='trainer'),
        write_only=True,
        source='user'
    )

    class Meta:
        model = EntrenadorProfile
        fields = [
            'id',
            'user',
            'user_id',
            'especialidad'
        ]
