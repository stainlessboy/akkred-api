from django.contrib import admin
from main.models import Registries


@admin.register(Registries)
class Admin(admin.ModelAdmin):
    pass
