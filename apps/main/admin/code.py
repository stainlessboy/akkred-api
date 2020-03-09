from django.contrib import admin
from main.models import Code, CodeType

from import_export.admin import ImportExportModelAdmin


@admin.register(Code)
class Admin(ImportExportModelAdmin):
    list_display = ['cod_tnved', 'organ_number']
    search_fields = ['cod_tnved', 'organ_number']
