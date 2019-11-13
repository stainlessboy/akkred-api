from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from main.serializers.laws import LawsModelSerializer, LawsCategoryModelSerializer
from main.models.laws import Laws, LawsCategory


class LawsViewSet(viewsets.ModelViewSet):
    model = Laws
    queryset = Laws.objects.all()
    serializer_class = LawsModelSerializer

    ordering_fields = ['id']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()


class LawsCategoryViewSet(viewsets.ModelViewSet):
    model = LawsCategory
    queryset = LawsCategory.objects.all()
    serializer_class = LawsCategoryModelSerializer

    ordering_fields = ['id']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()
