from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from main.filters.reestr import ReestrFilterSet
from main.models.registries import Registries
from rest_framework import viewsets, permissions
from main.serializers.registries import RegistriesSerializer, RegistriesSearchSerializer
from rest_framework.permissions import AllowAny


class RegistriesViewSet(viewsets.ModelViewSet):
    model = Registries
    queryset = Registries.objects.all()
    serializer_class = RegistriesSerializer
    search_fields = ['title_organ', 'inn', 'text', 'area']
    # search_fields = ['area']
    filter_fields = ['region', 'type_organ', 'status','id']
    ordering_fields = ['id', 'create_date']

    lookup_field = 'area'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super(RegistriesViewSet, self).get_permissions()

    def get_queryset(self):
        qs = super(RegistriesViewSet, self).get_queryset()
        search_serializer = RegistriesSearchSerializer(data=self.request.GET)
        search_serializer.is_valid(raise_exception=True)
        print(search_serializer.validated_data)
        if search_serializer.validated_data:
            qs = qs.filter(**search_serializer.validated_data)
        return qs

    # def list(self, request, a_slug=None, b_slug=None):
    #     qs = super(RegistriesViewSet, self).get_queryset()
    #     search_serializer = RegistriesSearchSerializer(data=self.request.GET)
    #     search_serializer.is_valid(raise_exception=True)
    #     if search_serializer.validated_data:
    #         qs = qs.filter(**search_serializer.data)
    #     return qs
