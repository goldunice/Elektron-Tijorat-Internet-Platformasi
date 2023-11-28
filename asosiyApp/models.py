from django.db import models

from userApp.models import Profil


class Bolim(models.Model):
    nom = models.CharField(max_length=255)
    rasm = models.FileField(upload_to="bolimlar")

    def __str__(self):
        return self.nom


class Mahsulot(models.Model):
    nom = models.CharField(max_length=255)
    brend = models.CharField(max_length=255)
    narx = models.PositiveIntegerField()
    chegirma = models.PositiveIntegerField(default=0)
    batafsil = models.TextField()
    kafolat = models.CharField(max_length=255)
    yetkazish = models.CharField(max_length=255)
    mavjud = models.BooleanField(default=True)
    davlat = models.CharField(max_length=255)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Media(models.Model):
    rasm = models.FileField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)


class Izoh(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    matn = models.TextField()
    baho = models.PositiveIntegerField(default=5)
    sana = models.DateField()
