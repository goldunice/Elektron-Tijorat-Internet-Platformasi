from django.db import models


class Bolim(models.Model):
    nom = models.CharField(max_length=255)
    rasm = models.FileField(upload_to="bolimlar")

    def __str__(self):
        return self.nom
