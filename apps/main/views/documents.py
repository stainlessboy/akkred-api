from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from main.serializers.documents import DocumentSerializer
from main.models.documents import Document


class DocumentViewSet(viewsets.ModelViewSet):
    model = Document
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    search_fields = ['title']
    filter_fields = ['title', 'created_date', 'parents']
    ordering_fields = ['id', 'created_date']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()
