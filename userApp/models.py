from django.db import models
from django.contrib.auth.models import AbstractUser


class Profil(AbstractUser):
    tel = models.CharField(max_length=255, blank=True)
    davlat = models.CharField(max_length=255, blank=True)
    jins = models.CharField(max_length=255, blank=True)
    shahar = models.CharField(max_length=255, blank=True)
    tasdiqlash_kodi = models.CharField(max_length=255, blank=True)
    tasdiqlangan = models.BooleanField(default=False)
    manzil = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=255, blank=True)
    rasm = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.username
