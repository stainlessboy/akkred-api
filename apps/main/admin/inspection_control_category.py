from django.contrib import admin
from main.models import ICCategory


@admin.register(ICCategory)
class Admin(admin.ModelAdmin):
    list_display = ['id']

