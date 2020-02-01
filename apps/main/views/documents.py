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
    ordering = ['order']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()
