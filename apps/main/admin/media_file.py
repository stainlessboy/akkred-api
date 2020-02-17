from django.contrib import admin
from main.models import MediaFile


@admin.register(MediaFile)
class Admin(admin.ModelAdmin):
    list_display = ['id','name']
    fields = [
        'link',
        'name',
        'admin_photo',
        'file',

    ]
    readonly_fields = ['link', 'admin_photo']
