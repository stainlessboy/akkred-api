import datetime

from django_filters.rest_framework import CharFilter

from core.rest_framework.filter import BaseFilter
from core.utils.helpers import is_int
from main.models.registries import Registries, RegistriesStatus


# test
class ReestrFilterSet(BaseFilter):
    region = CharFilter(method='filter_region')
    type_organ = CharFilter(method='filter_type_organ')
    status = CharFilter(method='filter_status')
    info = CharFilter(method='filter_info')
    stif = CharFilter(method='filter_info_status')

    class Meta:
        model = Registries
        fields = [
            'code_nd__cod_tnved', 'itt_cd'
        ]

    def filter_type_organ(self, query, name, value: str):
        value_list = value.split('-')
        if all(is_int(val) for val in value_list):
            return query.filter(type_organ__in=value_list)
        return query

    def filter_status(self, query, name, value: str):
        value_list = value.split('-')
        if all(is_int(val) for val in value_list):
            return query.filter(status__in=value_list)
        return query

    def filter_region(self, query, name, value: str):
        value_list = value.split('-')
        if all(is_int(val) for val in value_list):
            return query.filter(region__in=value_list)
        return query

    # def filter_type_organ(self, queryset, name, value):
    #     if value == 0:
    #         return queryset.all()
    #     return queryset.filter(type_organ=value)
    #
    # def filter_status(self, queryset, name, value):
    #     if value == '0':
    #         return queryset.all()
    #     return queryset.filter(status=value)
    #
    # def filter_region(self, queryset, name, value):
    #     if value == 0:
    #         return queryset.all()
    #     return queryset.filter(region=value)

    def filter_info(self, queryset, name, value):
        if value == '0':
            return queryset.filter(status__in=['paused', 'inactive']).all()
        return queryset.all()

    def filter_info_status(self, queryset, name, value):
        if value == 'active':
            return queryset.filter(reestr_logs__restore_date__isnull=False)
        if value == 'inactive':
            return queryset.filter(reestr_logs__inactive_date__isnull=False)
        if value == 'paused':
            return queryset.filter(reestr_logs__paused_date__isnull=False)
        return queryset.all()


class ReestrStatusFilterSet(BaseFilter):
    status = CharFilter(method='filter_status')

    class Meta:
        model = RegistriesStatus
        fields = []

    def filter_status(self, queryset, name, value):
        if value == '0':
            return queryset.all()
        return queryset.filter(status=value)
