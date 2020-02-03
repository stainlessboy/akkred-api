from rest_framework import viewsets
from rest_framework.permissions import AllowAny

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
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super().get_permissions()
