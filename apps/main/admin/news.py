from django.contrib import admin
from main.models import News \
    , NewsGallery


class NewsGalleryInline(admin.TabularInline):
    model = NewsGallery
    fields = ['image', 'admin_photo']
    readonly_fields = ['admin_photo']


@admin.register(News)
class Admin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    fields = [
        'admin_photo',
        'title_en',
        'title_ru',
        'title_uz',
        'text_en',
        'text_ru',
        'text_uz',
        'image_main',
        'created_date_by_admin'

    ]
    inlines = [NewsGalleryInline]
    readonly_fields = ['admin_photo']


@admin.register(NewsGallery)
class Admin(admin.ModelAdmin):
    fields = ['news']
    # inlines = [NewsGalleryInline]
