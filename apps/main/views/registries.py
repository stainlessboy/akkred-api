from main.filters.reestr import ReestrFilterSet
from main.models.registries import Registries
from rest_framework import viewsets, permissions
from main.serializers.registries import RegistriesSerializer, RegistriesSearchSerializer


class RegistriesViewSet(viewsets.ModelViewSet):
    model = Registries
    queryset = Registries.objects.all()
    serializer_class = RegistriesSerializer
    search_fields = ['title_organ', 'inn', 'text', 'area']
    filter_class = ReestrFilterSet
    ordering_fields = ['id', 'create_date']

    # lookup_field = 'area'

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'pdf']:
            return [permissions.AllowAny()]
        return super(RegistriesViewSet, self).get_permissions()

    def get_queryset(self):
        qs = super(RegistriesViewSet, self).get_queryset()
        search_serializer = RegistriesSearchSerializer(data=self.request.GET)
        search_serializer.is_valid(raise_exception=True)
        if search_serializer.validated_data:
            qs = qs.filter(**search_serializer.validated_data)
        return qs
