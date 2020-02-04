from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from main.models import DocParent, DocType, CategoryDocumentForm
from main.serializers.doc_parents import DocParentSerializer, DocTypeSerializer
from main.serializers.document_form_category import CategoryDocumentFormSerializer


class DocParentViewSet(viewsets.ModelViewSet):
    """
        retrieve:
        Return object of StaticPage

        list:
        Return a list of StaticPage objects

        create:
        Create a new  instance of StaticPage

        update:
        Update fields of StaticPage object
    """
    model = DocParent
    queryset = DocParent.objects.all()
    serializer_class = DocParentSerializer
    ordering = ['id']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super().get_permissions()


class DocTypeViewSet(viewsets.ModelViewSet):
    """
        retrieve:
        Return object of StaticPage

        list:
        Return a list of StaticPage objects

        create:
        Create a new  instance of StaticPage

        update:
        Update fields of StaticPage object
    """
    model = DocType
    queryset = DocType.objects.all()
    serializer_class = DocTypeSerializer
    ordering = ['order']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super().get_permissions()


class CategoryDocumentFormViewSet(viewsets.ModelViewSet):
    model = CategoryDocumentForm
    queryset = CategoryDocumentForm.objects.all()
    serializer_class = CategoryDocumentFormSerializer
    ordering = ['order']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super().get_permissions()
