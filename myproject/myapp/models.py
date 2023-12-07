# myapp/models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)  # Usar un hash para la contraseña

    def __str__(self):
        return self.username
