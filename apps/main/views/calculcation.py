from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from main.serializers.calculation import CalculationSerializers
from main.serializers.calculation_for_calibration_laboratories import CalculationTwoSerializers
from main.serializers.calculation_for_verification_laboratories import CalculationThreeSerializers
from main.serializers.calculation_four import CalculationFourSerializers


class Calculation(GenericViewSet):
    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def calculation(self, request):
        serializer = CalculationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'results': serializer.data})

    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def calculation_two(self, request):
        serializer = CalculationTwoSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'results': serializer.data})

    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def calculation_three(self, request):
        serializer = CalculationThreeSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'results': serializer.data})

    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def calculation_four(self, request):
        serializer = CalculationFourSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'results': serializer.data})
