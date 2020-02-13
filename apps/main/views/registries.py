from rest_framework.decorators import action

from main.filters.reestr import ReestrFilterSet
from main.models.registries import Registries
from rest_framework import viewsets, permissions, status
from main.serializers.registries import RegistriesSerializer, RegistriesSearchSerializer
from rest_framework.response import Response


class RegistriesViewSet(viewsets.ModelViewSet):
    model = Registries
    queryset = Registries.objects.all()
    serializer_class = RegistriesSerializer
    search_fields = ['number', 'inn', 'title_yurd_lisa', 'address_yurd_lisa', 'phone', 'email', 'web_site',
                     'title_organ', 'address_organ',
                     'full_name_supervisor_ao', 'phone_ao', 'email_ao', 'code', 'keywords', 'text', 'area']
    filter_class = ReestrFilterSet
    ordering_fields = ['id', 'create_date']

    lookup_field = 'area'

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

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # @action(['GET'], detail=False, permission_classes=[permissions.AllowAny])
    # def static(self, request):
    #     queryset = self.get_queryset()
    #     queryset = queryset.filter(status__in=['paused', 'extended']).all()
    #     serializer = RegistriesSerializer(queryset, many=True)
    #     data = {
    #         'results': serializer.data,
    #     }
    #     return Response(data)
