from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from main.models.type_organ import TypeOrgan
from main.serializers.type_organ import TypeOrganModelSerializer


class TypeOrganViewSet(viewsets.ModelViewSet):
    """
           retrieve:
           Return object of Region

           list:
           Return a list of Region objects

           create:
           Create a new  instance of Region

           update:
           Update fields of Region object
       """

    model = TypeOrgan
    queryset = TypeOrgan.objects.all()
    serializer_class = TypeOrganModelSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()

