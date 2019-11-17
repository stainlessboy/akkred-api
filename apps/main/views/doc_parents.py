from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from main.models import DocParent,DocType
from main.serializers.doc_parents import DocParentSerializer,DocTypeSerializer


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

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super().get_permissions()