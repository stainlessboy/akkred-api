from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from main.serializers.calculation.calculation import CalculationSerializers
from main.serializers.calculation.calculation_for_calibration_laboratories import \
    CalculationTwoSerializers
from main.serializers.calculation.calculation_for_verification_laboratories import \
    CalculationThreeSerializers
from main.serializers.calculation.calculation_four import \
    CalculationFourSerializers
from main.serializers.calculation.calculation_ok import \
    CalculationOkSerializers
from main.serializers.calculation.calculation_ospers import \
    CalculationOspersSerializers
from main.serializers.calculation.calculation_ossm import \
    CalculationOssmSerializers
from main.serializers.calculation.calculation_poi import \
    CalculationPoiSerializers


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

    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def calculation_poi(self, request):
        serializer = CalculationPoiSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'results': serializer.data})

    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def calculation_ossm(self, request):
        serializer = CalculationOssmSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'results': serializer.data})

    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def calculation_ospers(self, request):
        serializer = CalculationOspersSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'results': serializer.data})

    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def calculation_ok(self, request):
        serializer = CalculationOkSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'results': serializer.data})
