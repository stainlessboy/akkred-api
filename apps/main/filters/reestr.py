from django_filters.rest_framework import CharFilter, NumberFilter, DateFilter

from core.rest_framework.filter import BaseFilter
from core.utils.helpers import is_int
from main.models.registries import Registries

#test
class ReestrFilterSet(BaseFilter):
    region = CharFilter(method='filter_region')
    status = CharFilter(method='filter_status')
    type_organ = CharFilter(method='filter_type_organ')

    class Meta:
        model = Registries
        fields = []

    def filter_region(self, queryset, name, value: str):
        value_list = value.split('-')
        if all(is_int(val) for val in value_list):
            return queryset.filter(region__in=value_list)
        return queryset

    def filter_status(self, queryset, name, value: str):
        value_list = value.split('-')
        if all(is_int(val) for val in value_list):
            return queryset.filter(status__in=value_list)
        return queryset

    def filter_type_organ(self, queryset, name, value: str):
        value_list = value.split('-')
        if all(is_int(val) for val in value_list):
            return queryset.filter(type_organ__in=value_list)
        return queryset
