from django.contrib import admin
from main.models import ICCategory


@admin.register(ICCategory)
class Admin(admin.ModelAdmin):
    list_display = ['id']
    fields = [
        'name_en',
        'name_ru',
        'name_uz',
        'order',
    ]
