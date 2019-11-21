from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.db.models import Count

from main.serializers.documents import DocumentSerializer
from main.models.documents import Document


class DocumentViewSet(viewsets.ModelViewSet):
    model = Document
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    search_fields = ['title']
    filter_fields = ['title', 'created_date', 'parents', 'type']
    ordering_fields = ['id', 'created_date']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()

# class DocumentViewSet(ViewSet):
#     def get_permissions(self):
#         permissions = super(DocumentViewSet, self).get_permissions()
#         if self.action in ['list']:
#             permissions = [AllowAny()]
#         return permissions
#
#     # @action(['GET'], detail=False)
#     def list(self, request, **__):
#
#
#         queryset = Document.objects.all()
#         queryset = queryset.order_by()
#         queryset = queryset.values(
#             'parents__title',
#             'parents_id',
#             # 'parents__documents_id'
#         )
#         queryset = queryset.annotate(count=Count('*'))
#
#         queryset = queryset.values(
#             'parents__title',
#             'parents_id',
#             # 'id',
#             # 'title',
#
#             'count',
#         )
#         serializer = DocuemtnsListSerializer(
#             queryset, many=True)
#
#         return Response(serializer.data)
