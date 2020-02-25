import datetime

from django_filters.rest_framework import CharFilter, NumberFilter, DateFilter

from core.rest_framework.filter import BaseFilter
from core.utils.helpers import is_int
from main.models.registries import Registries, RegistriesStatus


# test
class ReestrFilterSet(BaseFilter):
    region = NumberFilter(method='filter_region')
    type_organ = NumberFilter(method='filter_type_organ')
    status = CharFilter(method='filter_status')
    info = CharFilter(method='filter_info')
    month = CharFilter(method='filter_month')
    stif = CharFilter(method='filter_info_status')

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

    def filter_info_status(self, queryset, name, value):
        if value == 'active':
            return queryset.filter(reestr_logs__restore_date__isnull=False)
        if value == 'inactive':
            return queryset.filter(reestr_logs__inactive_date__isnull=False)
        if value == 'paused':
            return queryset.filter(reestr_logs__paused_date__isnull=False)
        return queryset.all()

    def filter_month(self, queryset, name, value):
        if value == '1':
            present_month = datetime.date.today()
            prev_month = present_month.month - 3
            if prev_month >= 0:
                prev_month = prev_month
            else:
                prev_month = 1
            prev_date = datetime.date(2020, prev_month, 1)
            return queryset.filter(reestr_logs__paused_date__gte=prev_date,
                                   reestr_logs__paused_date__lte=present_month)
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
