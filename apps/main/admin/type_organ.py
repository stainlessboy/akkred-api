from django.contrib import admin
from main.models import TypeOrgan


@admin.register(TypeOrgan)
class Admin(admin.ModelAdmin):
    list_display = ['name_ru', 'title']
    search_fields = ['name', 'name_uz', 'name_ru', 'name_en']
    fields = [
        'title',
        'name_en',
        'name_ru',
        'name_uz'
    ]
