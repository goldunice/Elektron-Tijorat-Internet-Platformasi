from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from .models import Profil


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


class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        try:
            Profil.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                username=request.POST.get('username'),  # Using email as the default username
                password=request.POST.get('password'),
                jins=request.POST.get('gender'),
                davlat=request.POST.get('country'),
                shahar=request.POST.get('city')
            )
        except Exception:
            error_message = 'An error occurred during registration. Please try again.'
            return render(request, 'page-user-register.html', {'error_message': error_message})
        else:
            return redirect('/user/login/')
