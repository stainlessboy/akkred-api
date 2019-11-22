from django.contrib import admin
from main.models import Registries \
    , RegistriesStatus


class RegistriesStatusInline(admin.TabularInline):
    model = RegistriesStatus


@admin.register(Registries)
class Admin(admin.ModelAdmin):
    list_display = ['title_organ', 'type_organ']
    search_fields = ['type_organ', 'title_organ']
    list_filter = ['region', 'type_organ', 'status', 'is_fact_address', 'accreditation_date']
    inlines = [RegistriesStatusInline]
