from django.contrib import admin
from main.models import Code, CodeType, Registries

from import_export.admin import ImportExportModelAdmin


# def find_all_area(self, **_):
#     registries = Registries.objects.all()
#     for registrie in registries:
#         res = Code.objects.filter(organ_number=registrie.area)
#         if res.exists():
#             registrie.code_nd.set(res)


def export_csv(modeladmin, request, queryset):
    registries = Registries.objects.all()
    for registrie in registries:
        res = Code.objects.filter(organ_number=registrie.area)
        if res.exists():
            registrie.code_nd.set(res)


export_csv.short_description = u"Done all"


@admin.register(Code)
class Admin(ImportExportModelAdmin):
    actions = [export_csv]
    list_filter = ['organ_number']

    list_display = ['cod_tnved', 'organ_number']
    search_fields = ['cod_tnved', 'organ_number']
