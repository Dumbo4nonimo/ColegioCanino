from django.db import models
from users.models import User


class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.TextField(max_length=255)
    breed = models.TextField(max_length=255)
    size = models.IntegerField()
    birth_day = models.DateField()