from rest_framework.decorators import action

from main.filters.reestr_confirm import ConfirmReestrFilterSet
from main.models.confirm_reestr import ConfirmReestr
from main.serializers.confirm_reestr import ConfirmReestrModelSerializer
from core.printable.akkred import AkkredPDF
from core.rest_framework.printable_responses import pdf_response
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status

from main.serializers.registries import RegistriesConfirmSearchSerializer


class ConfirmReestrViewSet(viewsets.ModelViewSet):
    model = ConfirmReestr
    queryset = ConfirmReestr.objects.filter(is_public=True).all()
    serializer_class = ConfirmReestrModelSerializer
    ordering_fields = ['id']

    search_fields = ['number',
                     'inn',
                     'phone',
                     'email',
                     'title_organ',
                     'text', ]

    lookup_field = 'area'
    filter_class = ConfirmReestrFilterSet
    ordering = ['-number']

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'pdf']:
            return [permissions.AllowAny()]
        return super(ConfirmReestrViewSet, self).get_permissions()

    def get_queryset(self):
        qs = super().get_queryset()
        search_serializer = RegistriesConfirmSearchSerializer(
            data=self.request.GET)
        search_serializer.is_valid(raise_exception=True)
        if search_serializer.validated_data:
            qs = qs.filter(**search_serializer.validated_data)
        return qs

    @action(['GET'], detail=True)
    def pdf(self, request, area):
        queryset = self.get_queryset()
        try:
            instance = queryset.get(area=area)
            pdf_file = AkkredPDF(instance, request)
            pdf_file.generate()
            return pdf_response(pdf_file.get_output(), f' Akkred.pdf')
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
