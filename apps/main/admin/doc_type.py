
from django.contrib import admin
from main.models import DocType

@admin.register(DocType)
class Admin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['name_en', 'name_ru', 'name_uz']
    fields = [
        'name_en',
        'name_ru',
        'name_uz',
        'title',
        'order'
    ]