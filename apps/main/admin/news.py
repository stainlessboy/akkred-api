from django.contrib import admin
from main.models import News


@admin.register(News)
class Admin(admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ['id', 'title']
