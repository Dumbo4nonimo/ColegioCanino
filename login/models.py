from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    ROLE_CHOICES = (
        ('cliente', 'Cliente'),
        ('entrenador', 'Entrenador'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(_('email address'), unique=True)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cliente')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 
    
    def __str__(self):
        return f"{self.username} ({self.role})"

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente_profile')
    telefono = models.CharField(max_length=20, blank=True)
    edad = models.PositiveIntegerField(null=True, blank=True)
    reporte_deudas = models.CharField(max_length=100, blank=True)
    recomendaciones = models.TextField(max_length=100,blank=True)
    observaciones = models.TextField(max_length=100, blank=True)


    def __str__(self):
        return f"Cliente: {self.user.username}"    

class Entrenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='entrenador_profile')
    telefono = models.CharField(max_length=20, blank=True)
    especialidad = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Entrenador: {self.user.username}"