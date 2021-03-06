from django.contrib import admin
from main.models import Slider


@admin.register(Slider)
class Admin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'title_uz', 'title_ru', 'title_en']
    fields = [
        'admin_photo',
        'title_en',
        'title_ru',
        'title_uz',
        'image',
        'link',
    ]
    readonly_fields = ['admin_photo']