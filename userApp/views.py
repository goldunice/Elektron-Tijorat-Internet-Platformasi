from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from .models import Profil
import random
from eskiz.client import SMSClient


class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is None:
            return redirect('/user/login/')
        login(request, user)
        return redirect('/asosiy/home/')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/user/logout/')


class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        profil = Profil.objects.create_user(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            tel=request.POST.get('username'),
            username=request.POST.get('username'),
            password=request.POST.get('password1'),
            jins=request.POST.get('gender'),
            davlat=request.POST.get('country'),
            shahar=request.POST.get('city'),
            tasdiqlash_kodi=str(random.randrange(10000, 100000))
        )
        mijoz = SMSClient(
            api_url="https://notify.eskiz.uz/api/",
            email=settings.ESKIZ_GMAIL,
            password=settings.ESKIZ_PAROL,
        )
        mijoz._send_sms(
            phone_number=profil.tel,
            message=f"Tasdiqlash kodi {profil.tasdiqlash_kodi}"
        )
        login(request, profil)
        return redirect('/user/tasdiqlash/')


class KodTasdiqlash(View):
    def get(self, request):
        return render(request, 'tasdiqlash.html')

    def post(self, request):
        profil = Profil.objects.get(id=request.user.id)
        if profil.tasdiqlash_kodi == request.POST.get('kod'):
            profil.tasdiqlangan = True
            profil.save()
            return redirect('/user/login/')
        return redirect('/user/tasdiqlash/')
