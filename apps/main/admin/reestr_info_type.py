from django.contrib import admin
from main.models import CategoryReestrInfoUser


@admin.register(CategoryReestrInfoUser)
class Admin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
