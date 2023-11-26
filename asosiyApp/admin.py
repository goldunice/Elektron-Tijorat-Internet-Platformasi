from django.contrib import admin

from asosiyApp.models import Bolim


@admin.register(Bolim)
class BolimAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'rasm']
    list_display_links = ['id', 'nom']
    list_filter = ['nom']
    search_fields = ['nom']

