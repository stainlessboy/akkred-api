from rest_framework.decorators import action

from main.models.confirm_reestr import ConfirmReestr
from main.serializers.confirm_reestr import ConfirmReestrModelSerializer
from core.printable.akkred import AkkredPDF
from core.rest_framework.printable_responses import pdf_response
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status


class ConfirmReestrViewSet(viewsets.ModelViewSet):
    model = ConfirmReestr
    queryset = ConfirmReestr.objects.filter(is_public=True).all()
    serializer_class = ConfirmReestrModelSerializer
    ordering_fields = ['id']

    lookup_field = 'area'
    ordering = ['-number']

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'pdf']:
            return [permissions.AllowAny()]
        return super(ConfirmReestrViewSet, self).get_permissions()

    @action(['GET'], detail=True)
    def pdf(self, request, pk):
        queryset = self.get_queryset()
        try:
            instance = queryset.get(pk=pk)
            pdf_file = AkkredPDF(instance, request)
            pdf_file.generate()
            return pdf_response(pdf_file.get_output(), f' Akkred.pdf')
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
