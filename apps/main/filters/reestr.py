from django_filters.rest_framework import CharFilter

from core.rest_framework.filter import BaseFilter
from core.utils.helpers import is_int
from main.models.registries import Registries, RegistriesStatus


class ReestrFilterSet(BaseFilter):
    region = CharFilter(method='filter_region')
    type_organ = CharFilter(method='filter_type_organ')
    status = CharFilter(method='filter_status')

    class Meta:
        model = Registries
        fields = [
            'code_nd__cod_tnved', 'itt_cd', 'inn'
        ]

    def filter_type_organ(self, query, name, value: str):
        value_list = value.split('-')
        if all(is_int(val) for val in value_list):
            return query.filter(type_organ__in=value_list)
        return query

    def filter_status(self, query, name, value: str):
        value_list = value.split('-')
        if value_list:
            return query.filter(status__in=value_list)
        return query

    def filter_region(self, query, name, value: str):
        value_list = value.split('-')
        if all(is_int(val) for val in value_list):
            return query.filter(region__in=value_list)
        return query


class ReestrStatusFilterSet(BaseFilter):
    status = CharFilter(method='filter_status')

    class Meta:
        model = RegistriesStatus
        fields = []

    def filter_status(self, queryset, name, value):
        if value == '0':
            return queryset.all()
        return queryset.filter(status=value)
