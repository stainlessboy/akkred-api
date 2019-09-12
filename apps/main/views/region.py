from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from main.models.region import Region
from main.serializers.region import RegionModelSerializer


class RegionViewSet(viewsets.ModelViewSet):
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

    model = Region
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
    # ordering_fields = ['name', 'parent']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()

