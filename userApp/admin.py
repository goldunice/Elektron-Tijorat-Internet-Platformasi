from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class ProfilAdmin(UserAdmin):
    model = Profil
    fieldsets = UserAdmin.fieldsets + (('Profil', {'fields': ('davlat', 'shahar', 'tel', 'jins')}),)
    list_display = ['id', 'davlat', 'shahar', 'tel', 'jins', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser']


admin.site.register(Profil, ProfilAdmin)
