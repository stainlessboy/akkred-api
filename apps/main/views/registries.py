from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from main.filters.reestr import ReestrFilterSet
from main.models.registries import Registries
from rest_framework import viewsets, permissions
from main.serializers.registries import RegistriesSerializer
from rest_framework.permissions import AllowAny


class RegistriesViewSet(viewsets.ModelViewSet):
    model = Registries
    queryset = Registries.objects.all()
    serializer_class = RegistriesSerializer
    # search_fields = ['title', 'inn', 'text']
    search_fields = ['title', 'inn', 'text']
    # filter_fields = ['region', 'type_organ', 'status']
    filter_backends = (DjangoFilterBackend, OrderingFilter)

    filter_class = ReestrFilterSet
    ordering_fields = ['id', 'create_date']
    # lookup_field = 'area'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super(RegistriesViewSet, self).get_permissions()
