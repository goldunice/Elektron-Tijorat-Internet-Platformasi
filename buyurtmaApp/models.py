from django.db import models

from asosiyApp.models import *


class Tanlangan(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)


class Savat(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    total_sum = models.PositiveIntegerField(default=0)
    holat = models.CharField(max_length=255, blank=True)


class SavatItem(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField(default=1)
    summa = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        chegirma = (self.mahsulot.narx * self.mahsulot.chegirma) / 100
        narx = self.mahsulot.narx - chegirma
        self.summa = narx * self.miqdor
        savat = Savat.objects.get(id=self.savat.id)
        total = self.summa
        for item in savat.savatitem_set.exclude(id=self.id):
            total += item.summa
        savat.total_sum = total
        savat.save()
        super(SavatItem, self).save(*args, **kwargs)


class Buyurtma(models.Model):
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    yetkazish_puli = models.PositiveIntegerField(default=5)
    sana = models.DateField(auto_now_add=True)
    umumiy_summa = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.umumiy_summa = self.yetkazish_puli + self.savat.total_sum
        super(Buyurtma, self).save(*args, **kwargs)
