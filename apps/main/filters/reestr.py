from django_filters.rest_framework import CharFilter, NumberFilter, DateFilter

from core.rest_framework.filter import BaseFilter
from core.utils.helpers import is_int
from main.models.registries import Registries


# test
class ReestrFilterSet(BaseFilter):
    region = NumberFilter(method='filter_region')
    type_organ = NumberFilter(method='filter_type_organ')
    status = CharFilter(method='filter_status')
    info = CharFilter(method='filter_info')

    class Meta:
        model = Registries
        fields = []

    def filter_type_organ(self, queryset, name, value):
        if value == 0:
            return queryset.all()
        return queryset.filter(type_organ=value)

    def filter_status(self, queryset, name, value):
        if value == '0':
            return queryset.all()
        return queryset.filter(status=value)

    def filter_info(self, queryset, name, value):
        if value == '0':
            return queryset.filter(status__in=['paused', 'inactive']).all()
        return queryset.all()

    def filter_region(self, queryset, name, value):
        if value == 0:
            return queryset.all()
        return queryset.filter(region=value)
