from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from main.models import StaticPage
from main.serializers.static_pages import StaticPageModelSerializer


class StaticPagesViewSet(viewsets.ModelViewSet):
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
    model = StaticPage
    queryset = StaticPage.objects.all()
    serializer_class = StaticPageModelSerializer
    lookup_field = 'key_name'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return super().get_permissions()
