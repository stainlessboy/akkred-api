from django.contrib import admin
from main.models import InspectionControl


@admin.register(InspectionControl)
class Admin(admin.ModelAdmin):
    list_display = ['name', 'name_uz']

    fields = [
        'name_en',
        'name_ru',
        'name_uz',
        'category',
        'file',
    ]
