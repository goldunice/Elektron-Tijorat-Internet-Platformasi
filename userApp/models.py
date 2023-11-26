from django.db import models
from django.contrib.auth.models import AbstractUser


class Profil(AbstractUser):
    tel = models.CharField(max_length=255, blank=True)
    davlat = models.CharField(max_length=255, blank=True)
    jins = models.CharField(max_length=255, blank=True)
    shahar = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
