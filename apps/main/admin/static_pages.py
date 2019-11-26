from django.contrib import admin
from main.models import StaticPage


@admin.register(StaticPage)
class Admin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    fields = [
        'key_name',
        'name_en',
        'name_ru',
        'name_uz',
        'body_en',
        'body_ru',
        'body_uz',

    ]