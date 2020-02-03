
from django.contrib import admin
from main.models import DocParent

@admin.register(DocParent)
class Admin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['name_en', 'name_ru', 'name_uz']
    fields = [
        'name_en',
        'name_ru',
        'name_uz',
        'title',
    ]