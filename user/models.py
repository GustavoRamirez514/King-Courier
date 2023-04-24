from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    num_phone = models.CharField("Telefono", max_length=10)
    address = models.CharField("Direccion", max_length=100)
    city = models.CharField("Ciudad", max_length=100)
