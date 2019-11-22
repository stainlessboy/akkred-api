from django.contrib import admin
from main.models import News \
    , NewsGallery


class NewsGalleryInline(admin.TabularInline):
    model = NewsGallery
    fields = ['image']


@admin.register(News)
class Admin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    fields = [
        'title_en',
        'title_ru',
        'title_uz',

        'text_en',
        'text_ru',
        'text_uz',
    ]
    inlines = [NewsGalleryInline]


@admin.register(NewsGallery)
class Admin(admin.ModelAdmin):
    fields = ['news']
    # inlines = [NewsGalleryInline]
