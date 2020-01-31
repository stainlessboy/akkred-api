from rest_framework import viewsets, permissions

from main.models import InspectionControl, ICCategory
from main.serializers.inspection_control import InspectionControlSerializer, ICCategorySerializer


class ICCategoryViewSet(viewsets.ModelViewSet):
    queryset = ICCategory.objects.all()
    serializer_class = ICCategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super(ICCategoryViewSet, self).get_permissions()


class InspectionControlViewSet(viewsets.ModelViewSet):
    queryset = InspectionControl.objects.all()
    serializer_class = InspectionControlSerializer
    filter_fields = ['category']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super(InspectionControlViewSet, self).get_permissions()
