from django.contrib import admin
from main.models import Document \
    , DocumentForm


class DocumentFormInline(admin.TabularInline):
    model = DocumentForm


@admin.register(Document)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'number']
    search_fields = ['title']
    list_filter = ['parents', 'type']
    inlines = [DocumentFormInline]
