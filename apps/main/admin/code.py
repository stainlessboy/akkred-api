from django.contrib import admin
from main.models import Code


@admin.register(Code)
class Admin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
