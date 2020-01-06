import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from rest_framework.decorators import action
from rest_framework.response import Response

from core.printable.akkred import AkkredPDF
from core.rest_framework.printable_responses import pdf_response
from main.filters.reestr import ReestrFilterSet
from main.models.registries import Registries
from rest_framework import viewsets, permissions, status
from main.serializers.registries import RegistriesSerializer, RegistriesSearchSerializer


# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

class RegistriesViewSet(viewsets.ModelViewSet):
    model = Registries
    queryset = Registries.objects.all()
    serializer_class = RegistriesSerializer
    search_fields = ['title_organ', 'inn', 'text', 'area']
    # search_fields = ['area']
    # filter_fields = ['region', 'type_organ', 'status', 'id']
    filter_class = ReestrFilterSet
    ordering_fields = ['id', 'create_date']

    # pagination_class = StandardResultsSetPagination
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

    # def list(self, request, a_slug=None, b_slug=None):
    #     qs = super(RegistriesViewSet, self).get_queryset()
    #     search_serializer = RegistriesSearchSerializer(data=self.request.GET)
    #     search_serializer.is_valid(raise_exception=True)
    #     if search_serializer.validated_data:
    #         qs = qs.filter(**search_serializer.data)
    #     return qsc
    # @action(['GET'], detail=False)
    # def pdf(self, request, pk=None):
    #     buffer = io.BytesIO()
    #
    #     # Create the PDF object, using the buffer as its "file."
    #     p = canvas.Canvas(buffer)
    #
    #     # Draw things on the PDF. Here's where the PDF generation happens.
    #     # See the ReportLab documentation for the full list of functionality.
    #     p.drawString(100, 100, "Hello world.")
    #
    #     # Close the PDF object cleanly, and we're done.
    #     p.showPage()
    #     p.save()
    #
    #     # FileResponse sets the Content-Disposition header so that browsers
    #     # present the option to save the file.
    #     buffer.seek(0)
    #     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

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
