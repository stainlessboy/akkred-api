from django.contrib import admin
from main.models import Document \
    , DocumentForm


class DocumentFormInline(admin.TabularInline):
    model = DocumentForm
    fields = [
        'title_en',
        'title_ru',
        'title_uz',
        'file',
        'order',
    ]


@admin.register(Document)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'number', 'description']
    search_fields = ['name_en', 'name_ru', 'name_uz']
    list_filter = ['parents', 'type']
    inlines = [DocumentFormInline]
    fields = [
        'name_en',
        'name_ru',
        'name_uz',
        'description_en',
        'description_ru',
        'description_uz',
        'link',
        'order',
        'number',
        'title',
        'parents',
        'type',
        'status',
        'file',
    ]
