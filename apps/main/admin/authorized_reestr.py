from main.models import AuthorizedReestr
from django.contrib import admin


@admin.register(AuthorizedReestr)
class Admin(admin.ModelAdmin):
    list_display = ['title_organ']
