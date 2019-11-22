from django.contrib import admin
from main.models import ReestrInfoUser


@admin.register(ReestrInfoUser)
class Admin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['type']
