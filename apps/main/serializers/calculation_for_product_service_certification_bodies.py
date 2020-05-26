from collections import defaultdict
from math import ceil

from rest_framework import serializers


def roundPrice(value):
    if (value % 1) > 0 and (value % 1) <= 0.5:
        bal = 0.5
    elif (value % 1) == 0:
        bal = 0
    else:
        bal = 1
    return int(value) + bal


def fixProblems(value):
    if (value <= 200):
        return 1
    elif (value <= 500):
        return 2
    else:
        return 3


def numberRecKL(value):
    if value <= 200:
        return 2
    elif value <= 500:
        return 3
    elif value <= 1000:
        return 4
    elif value <= 2000:
        return 5
    elif value <= 3500:
        return 6
    elif value <= 5500:
        return 7
    elif value <= 8000:
        return 8
    else:
        return 8 + ceil((value - 8000) / 3000)


def fixProblemsPL(value):
    if (value <= 100):
        return 1
    elif (value <= 300):
        return 2
    else:
        return 3


# Функция для ИК

def numberRecPL(value):
    if value <= 200:
        return 0.5
    elif value <= 500:
        return 1
    elif value <= 1000:
        return 1.5
    elif value <= 2000:
        return 2.0
    elif value <= 3500:
        return 2.5
    elif value <= 5500:
        return 3
    elif value <= 8000:
        return 3.5
    else:
        return 3.5 + ceil((value - 8000) / 3000) / 2


def numberRecOS(value):
    if value <= 200:
        return 2
    elif value <= 500:
        return 3
    elif value <= 1000:
        return 4
    elif value <= 2000:
        return 5
    elif value <= 3500:
        return 6
    elif value <= 5500:
        return 7
    elif value <= 8000:
        return 8
    else:
        return 8 + ceil((value - 8000) / 3000)


# ДЛЯ ОРГАНОВ ПО СЕРТИФИКАЦИИ ПРОДУКЦИИ И УСЛУГ
class CalculationFourSerializers(serializers.Serializer):
    type = serializers.CharField(write_only=True)
    calculation_type = serializers.CharField(write_only=True)
    number = serializers.FloatField(write_only=True)
    number_inspection = serializers.FloatField(write_only=True, required=False)
    sum = serializers.FloatField(required=False)

    def create(self, validated_data: dict):
        numObj = validated_data['numObj']
        numND = validated_data['numND']
        numStaff = validated_data['numStaff']

        sum = 0
        c = 1050000
        num_test = validated_data.get('number_inspection', None)

        if validated_data['type'] == 'accreditation':
            if validated_data['calculation_type'] == 'expertise':
                t = (numObj * 3 + numND * 10) / 480
                t = roundPrice(t)
                num_day_total = t + 3.5
                sum = num_day_total * c
            if validated_data['calculation_type'] == 'site':
                t1 = fixProblems(numND)
                t2 = roundPrice(numND / 240)
                t3 = roundPrice(numStaff / 2.67)
                num_day_total = t1 + t2 + t3 + 5
                sum = num_day_total * c

        # TODO expansion // входные данные - numObj, numND, numStaff
        if validated_data['type'] == 'expansion':
            if validated_data['calculation_type'] == 'expertise':
                t = (numObj * 3 + numND * 10) / 480
                t = roundPrice(t)
                num_day_total = t + 1.5
                sum = num_day_total * c
            if validated_data['calculation_type'] == 'site':
                t1 = fixProblems(numND)
                t2 = roundPrice(numND / 240)
                t3 = roundPrice(numStaff / 2.67)
                num_day_total = t1 + t2 + t3 + 3
                sum = num_day_total * c

        # TODO actualization // входные данные - numND
        if validated_data['type'] == 'actualization':
            t = roundPrice(numND / 240)
            num_day_total = t + 1
            sum = num_day_total * c
        # TODO inspection_control // входные данные - numStaff, num_test
        if validated_data['type'] == 'inspection_control':
            t1 = roundPrice(numStaff / 2.67)
            t2 = numberRecOS(num_test)
            num_day_total = t1 + t2 + 4
            sum = num_day_total * c

        validated_data.update(sum=sum)
        return validated_data
