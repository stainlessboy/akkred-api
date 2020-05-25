from django.contrib import admin
from main.models import Document \
    , DocumentForm


class DocumentFormInline(admin.TabularInline):
    model = DocumentForm
    fields = [
        'category',
        'title_ru',
        'title_uz',
        'file',
        'order',
    ]


@admin.register(Document)
class Admin(admin.ModelAdmin):
    list_display = ['name', 'description']
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
        'parents',
        'type',
        'status',
        'file',
    ]
