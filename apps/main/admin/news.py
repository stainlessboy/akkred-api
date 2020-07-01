from django.contrib import admin
from main.models import News


@admin.register(News)
class Admin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    fields = [
        'admin_photo',
        'title_en',
        'title_ru',
        'title_uz',
        'text_en',
        'text_ru',
        'text_uz',
        'image_main',
        'created_date_by_admin',

    ]
    readonly_fields = ['admin_photo']
