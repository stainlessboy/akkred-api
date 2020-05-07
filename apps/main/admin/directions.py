from django.contrib import admin
from main.models import Directions


@admin.register(Directions)
class Admin(admin.ModelAdmin):
    list_display = ['name']
    fields = [
        'name',
    ]
