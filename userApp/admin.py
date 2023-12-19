from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class ProfilAdmin(UserAdmin):
    model = Profil
    fieldsets = UserAdmin.fieldsets + (
        ('Profil', {'fields': ('davlat', 'shahar', 'tel', 'jins', 'tasdiqlangan', 'manzil', 'zipcode', 'rasm')}),)
    list_display = ['id', 'davlat', 'shahar', 'tel', 'jins', 'username', 'first_name', 'last_name', 'email', 'is_staff',
                    'is_active', 'is_superuser', 'tasdiqlangan', 'manzil', 'zipcode','rasm']


admin.site.register(Profil, ProfilAdmin)
