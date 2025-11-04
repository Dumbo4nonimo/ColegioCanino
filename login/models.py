from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('cliente', 'Cliente'),
        ('trainer', 'Entrenador'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class ClienteProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField
    telefono = models.CharField(max_length=15)
    reporte_deudas = models.CharField(max_length=100)
    recomendaciones = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if self.user.role != 'cliente':
            raise ValueError("Solo usuarios con rol 'cliente' pueden tener este perfil")
        super().save(*args, **kwargs)

class EntrenadorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.user.role != 'trainer':
            raise ValueError("Solo usuarios con rol 'trainer' pueden tener este perfil")
        super().save(*args, **kwargs)
