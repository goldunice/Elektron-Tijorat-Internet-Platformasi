from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.db.models import Avg


class HomeLoginsizView(View):
    def get(self, request):
        return render(request, "page-index-2.html")


class HomeView(View):
    def get(self, request):
        content = {
            "bolimlar": Bolim.objects.all()[:8]
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
