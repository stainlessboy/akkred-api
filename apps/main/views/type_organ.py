from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
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
        if self.action in ['list']:
            return [AllowAny()]
        return super().get_permissions()

    @action(['GET'], detail=False, permission_classes=[permissions.AllowAny])
    def static(self, request):
        queryset = self.get_queryset()
        queryset = queryset.filter(id__in=[1, 2, 3, 5, 6]).all()
        serializer = TypeOrganModelSerializer(queryset, many=True)
        data={
            'results':serializer.data
        }
        return Response(data)
