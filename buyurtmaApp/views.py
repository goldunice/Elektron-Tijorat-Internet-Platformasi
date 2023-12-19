from django.shortcuts import render, redirect
from .models import *
from django.views import View


class TanlanganlarView(View):
    def get(self, request):
        content = {
            'tanlanganlar': Tanlangan.objects.filter(profil=request.user)
        }
        return render(request, 'page-profile-wishlist.html', content)


class TanlanganlargaQoshView(View):
    def get(self, request, pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        if mahsulot not in Tanlangan.objects.filter(profil=request.user):
            Tanlangan.objects.create(
                mahsulot=mahsulot,
                profil=request.user
            )
        return redirect('/buyurtma/savat/')


class AddTanlanganView(View):
    def get(self, request, pk):
        Tanlangan.objects.create(
            mahsulot=Mahsulot.objects.get(id=pk),
            profil=request.user
        )
        return redirect('/buyurtma/savat/')


class DeleteTanlanganItem(View):
    def get(self, request, pk):
        Tanlangan.objects.get(id=pk).delete()
        return redirect('/buyurtma/tanlanganlar/')


class SavatlarView(View):
    def get(self, request):
        savati = Savat.objects.filter(profil=request.user)
        if savati.exists():
            savati = savati.first()
        else:
            savati = Savat.objects.create(profil=request.user)
        itemlar = SavatItem.objects.filter(savat=savati)
        chegirma = 0
        for item in itemlar:
            chegirma += (item.mahsulot.narx * item.mahsulot.chegirma) // 100
        content = {
            'savat': savati,
            'itemlar': itemlar,
            'chg': chegirma,
            'sum': savati.total_sum + chegirma,
            'yakuniy': savati.total_sum
        }
        return render(request, 'page-shopping-cart.html', content)


class AddSavatItemView(View):
    def get(self, request, pk):
        savat = Savat.objects.filter(profil=request.user)
        if savat.exists():
            savat = savat.first()
        else:
            savat = Savat.objects.create(profil=request.user)
        item = SavatItem.objects.filter(mahsulot__id=pk, savat=savat)
        if item.exists():
            item = item.first()
            item.miqdor += 1
            item.save()
        else:
            SavatItem.objects.create(
                mahsulot=Mahsulot.objects.get(id=pk),
                savat=savat,
                summa=0
            )
        return redirect('/buyurtma/savat/')


class DeleteSavatItem(View):
    def get(self, request, pk):
        SavatItem.objects.get(id=pk).delete()
        return redirect('/buyurtma/savat/')


class MiqdorQosh(View):
    def get(self, request, pk):
        item = SavatItem.objects.get(id=pk)
        if item.miqdor != 5:
            item.miqdor += 1
        item.save()
        return redirect('/buyurtma/savat/')


class MiqdorKamaytir(View):
    def get(self, request, pk):
        item = SavatItem.objects.get(id=pk)
        if item.miqdor != 1:
            item.miqdor -= 1
        item.save()
        return redirect('/buyurtma/savat/')


class BuyurtmalarView(View):
    def get(self, request):
        content = {
            'buyurtmalar': Buyurtma.objects.filter(savat__profil=request.user)
        }
        return render(request, 'page-profile-orders.html', content)


class BuyurtmaQosh(View):
    def get(self, request):
        Buyurtma.objects.create(
            savat=Savat.objects.get(profil=request.user)
        )
        return redirect('/buyurtma/buyurtmalar/')
