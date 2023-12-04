from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    cpf_cnpj = models.CharField(max_length=14, unique=True, null=False)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    is_shopkeeper = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username