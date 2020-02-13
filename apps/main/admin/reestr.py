from django.contrib import admin
from main.models import Registries \
    ,RegisterStatusLog


class RegistriesStatusInline(admin.TabularInline):
    model = RegisterStatusLog
    fields = [
        'paused_date',
        'restore_date',
        'inactive_date',
        'extended_date',
        'renewal_date',
        'case_type',
        'note',

    ]


@admin.register(Registries)
class Admin(admin.ModelAdmin):
    list_display = ['title_organ', 'type_organ', 'number']
    search_fields = ['number', 'title_organ', 'inn', 'id']
    list_filter = ['region', 'type_organ', 'status', 'is_fact_address', 'accreditation_date']
    inlines = [RegistriesStatusInline]
