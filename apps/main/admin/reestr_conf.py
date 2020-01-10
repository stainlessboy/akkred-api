from django.contrib import admin
from main.models import ConfirmReestr


@admin.register(ConfirmReestr)
class Admin(admin.ModelAdmin):
    list_display = ['title_organ']
    search_fields = ['title_organ']
