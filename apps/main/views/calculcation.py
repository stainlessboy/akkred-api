from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from main.serializers.calculation import CalculationSerializers


class Calculation(GenericViewSet):
    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def calculation(self, request):
        serializer = CalculationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': serializer.data})
