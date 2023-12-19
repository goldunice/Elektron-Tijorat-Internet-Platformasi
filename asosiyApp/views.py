from django.shortcuts import render, redirect
from django.views import View
from buyurtmaApp.models import *
from buyurtmaApp.models import SavatItem
from .models import *
from django.db.models import Avg


class ProfileView(View):
    def get(self, request):
        content = {
            'profil': Profil.objects.get(id=request.user.id),
            'tanlanganlar_soni': len(Tanlangan.objects.filter(profil=request.user)),
            'buyurtmalar': Buyurtma.objects.filter(savat=Savat.objects.get(profil=request.user))[:4],
            'buyurtmalar_soni': len(Buyurtma.objects.filter(savat=Savat.objects.get(profil=request.user))),
        }
        return render(request, 'page-profile-main.html', content)


class HomeLoginsizView(View):
    def get(self, request):
        return render(request, "page-index-2.html")


class HomeView(View):
    def get(self, request):
        content = {
            "bolimlar": Bolim.objects.all()[:8],
            "mahsulotlar": Mahsulot.objects.all()[3:6],
            "maxsulotlar": Mahsulot.objects.all()[:12],
        }
        return render(request, "page-index.html", content)


class BolimlarView(View):
    def get(self, request):
        content = {
            "bolimlar": Bolim.objects.all()
        }
        return render(request, 'page-category.html', content)


class MahsulotlarView(View):
    def get(self, request, id):
        content = {
            "mahsulotlar": Mahsulot.objects.filter(bolim__id=id)
        }
        return render(request, 'page-listing-grid.html', content)


class MahsulotView(View):
    def get(self, request, id):
        izohlar = Izoh.objects.filter(mahsulot__id=id)
        ortachasi = izohlar.aggregate(Avg("baho")).get("baho__avg")
        if ortachasi:
            ortachasi *= 20
        else:
            ortachasi = 0
        content = {
            "mahsulot": Mahsulot.objects.get(id=id),
            "ortachasi": ortachasi
        }
        return render(request, 'page-detail-product.html', content)

    def post(self, request, id):
        from datetime import date
        Izoh.objects.create(
            baho=request.POST.get('rating'),
            matn=request.POST.get('comment'),
            sana=date.today(),
            mahsulot=Mahsulot.objects.filter(id=id).first(),
            profil=request.user,
        )
        return redirect(f'/asosiy/mahsulot/{id}/')
