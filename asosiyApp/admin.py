from django.contrib import admin

from asosiyApp.models import Bolim, Mahsulot, Izoh, Media


@admin.register(Bolim)
class BolimAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'rasm']
    list_display_links = ['id', 'nom']
    list_filter = ['nom']
    search_fields = ['nom']


@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'brend', 'narx', 'chegirma', 'batafsil', 'kafolat', 'yetkazish', 'mavjud', 'davlat',
                    'bolim']
    list_display_links = ['id', 'nom']
    list_filter = ['nom', 'brend', 'narx', 'chegirma', 'davlat']
    search_fields = ['nom', 'brend']


@admin.register(Izoh)
class IzohAdmin(admin.ModelAdmin):
    list_display = ['id', 'profil', 'mahsulot', 'matn', 'baho', 'sana']
    list_display_links = ['id', 'matn']
    list_filter = ['baho']


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'rasm', 'mahsulot']
