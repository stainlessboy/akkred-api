from django_filters.rest_framework import CharFilter

from core.rest_framework.filter import BaseFilter
from core.utils.helpers import is_int
from main.models.confirm_reestr import ConfirmReestr


class ConfirmReestrFilterSet(BaseFilter):
    region = CharFilter(method='filter_region')
    status = CharFilter(method='filter_status')

    class Meta:
        model = ConfirmReestr
        fields = [
            'status', 'region'
        ]

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
