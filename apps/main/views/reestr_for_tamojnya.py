from main.filters.reestr import ReestrFilterSet
from main.models.registries import Registries
from rest_framework import viewsets, permissions, status
from main.serializers.registries import RegistriesSerializer, RegistriesSearchSerializer
from rest_framework.response import Response


class RegistriesForTamojnyaViewSet(viewsets.ModelViewSet):
    model = Registries
    queryset = Registries.objects.filter(itt_cd__isnull=False, type_organ=2)
    serializer_class = RegistriesSerializer
    search_fields = ['number', 'inn', 'title_yurd_lisa', 'address_yurd_lisa', 'phone', 'email', 'web_site',
                     'title_organ', 'address_organ',
                     'full_name_supervisor_ao', 'phone_ao', 'email_ao', 'code', 'keywords', 'text', 'area']
    filter_class = ReestrFilterSet
    lookup_field = 'area'

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'pdf']:
            return [permissions.AllowAny()]
        return super(RegistriesForTamojnyaViewSet, self).get_permissions()

    def get_queryset(self):
        qs = super(RegistriesForTamojnyaViewSet, self).get_queryset()
        search_serializer = RegistriesSearchSerializer(data=self.request.GET)
        search_serializer.is_valid(raise_exception=True)
        if search_serializer.validated_data:
            qs = qs.filter(**search_serializer.validated_data)
        return qs

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
